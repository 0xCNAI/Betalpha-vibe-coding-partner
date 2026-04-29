import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import { spawn } from "node:child_process";
import { existsSync, appendFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";

const ID = "betavibe-lifecycle";
const stateByRun = new Map();
const promptCache = new Map();

function cfg(event = {}, ctx = {}, fallbackConfig = {}) {
  const c = event?.context?.pluginConfig ?? ctx?.pluginConfig ?? fallbackConfig ?? {};
  const projectRoot = resolve(String(c.projectRoot || ctx.workspaceDir || process.cwd()));
  const betavibePath = resolve(projectRoot, String(c.betavibePath || "."));
  return {
    enabled: c.enabled !== false,
    projectRoot,
    betavibePath,
    registry: c.registry ? String(c.registry) : undefined,
    maxResolveMs: Number(c.maxResolveMs || 2500),
    maxPromptChars: Number(c.maxPromptChars || 3500),
    minDebugMinutes: Number(c.minDebugMinutes || 20),
    maxSessionChecksMs: Number(c.maxSessionChecksMs || 3000),
    dryRun: c.dryRun !== false,
  };
}

function runBetavibe(c, args, timeoutMs) {
  return new Promise((resolvePromise) => {
    const env = { ...process.env };
    if (c.registry) env.BETAVIBE_REGISTRY = c.registry;
    const child = spawn("python3", ["-m", "betavibe", ...args], {
      cwd: c.betavibePath,
      env,
      stdio: ["ignore", "pipe", "pipe"],
    });
    let stdout = "";
    let stderr = "";
    const timer = setTimeout(() => {
      child.kill("SIGTERM");
      resolvePromise({ ok: false, timeout: true, stdout, stderr });
    }, Math.max(500, timeoutMs));
    child.stdout.on("data", (d) => { stdout += d.toString(); });
    child.stderr.on("data", (d) => { stderr += d.toString(); });
    child.on("error", (err) => {
      clearTimeout(timer);
      resolvePromise({ ok: false, error: String(err), stdout, stderr });
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      resolvePromise({ ok: code === 0, code, stdout, stderr });
    });
  });
}

function textOf(value, limit = 6000) {
  if (typeof value === "string") return value.slice(0, limit);
  try { return JSON.stringify(value).slice(0, limit); } catch { return String(value).slice(0, limit); }
}

function stripNoise(text) {
  return String(text || "")
    .replace(/<<<BEGIN_OPENCLAW_INTERNAL_CONTEXT>>>[\s\S]*?<<<END_OPENCLAW_INTERNAL_CONTEXT>>>/g, " ")
    .replace(/\[Betavibe [\s\S]*?\[\/Betavibe context\]/g, " ")
    .replace(/Sender \(untrusted metadata\):[\s\S]*?```/g, " ")
    .replace(/"thinkingSignature"\s*:\s*"[^"]*"/g, " ")
    .replace(/"encrypted_content"\s*:\s*"[^"]*"/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function messageText(msg) {
  if (!msg || msg.role !== "user") return "";
  const content = msg.content;
  if (typeof content === "string") return content;
  if (Array.isArray(content)) {
    return content.filter((part) => part?.type === "text" && typeof part.text === "string").map((part) => part.text).join("\n");
  }
  return "";
}

function latestUserPrompt(event) {
  const direct = stripNoise(event?.prompt ?? event?.input ?? event?.message ?? "");
  if (direct) return direct;
  const messages = Array.isArray(event?.messages) ? event.messages : [];
  for (let i = messages.length - 1; i >= 0; i -= 1) {
    const text = stripNoise(messageText(messages[i]));
    if (text) return text;
  }
  return "";
}

function classifyPrompt(prompt) {
  const p = textOf(prompt, 4000).toLowerCase();
  const coding = /(implement|fix|debug|refactor|test|spec|migration|hook|plugin|api|cli|github|deploy|database|schema|寫|修|接|測試|規格|實作)/.test(p);
  if (!coding) return null;
  const trivial = /(typo|拼字|readme typo|format only|只改文案)/.test(p);
  if (trivial) return null;
  if (/(spec|design|plan|architecture|規格|設計|規劃)/.test(p)) return "pre_spec";
  return "pre_implement";
}

function runKey(ctx, event) {
  return ctx?.runId || event?.runId || ctx?.sessionKey || ctx?.sessionId || "unknown";
}

function record(runId, patch) {
  const prev = stateByRun.get(runId) || { startedAt: Date.now(), toolCalls: 0, errors: 0, attempts: 0, filesTouched: new Set(), snippets: [] };
  const next = { ...prev, ...patch };
  if (patch.filesTouched) next.filesTouched = new Set([...(prev.filesTouched || []), ...patch.filesTouched]);
  if (patch.snippet) next.snippets = [...(prev.snippets || []), patch.snippet].slice(-8);
  stateByRun.set(runId, next);
  return next;
}

function appendAudit(c, obj) {
  const path = resolve(c.projectRoot, ".betavibe", "lifecycle-events.jsonl");
  mkdirSync(dirname(path), { recursive: true });
  appendFileSync(path, JSON.stringify({ ts: new Date().toISOString(), ...obj }) + "\n");
}

export default definePluginEntry({
  id: ID,
  name: "Betavibe Lifecycle",
  description: "Betavibe resolver/capture lifecycle hooks for OpenClaw.",
  register(api) {
    const fallbackConfig = api.pluginConfig ?? {};
    api.on("before_prompt_build", async (event, ctx) => {
      const c = cfg(event, ctx, fallbackConfig);
      if (!c.enabled || !existsSync(c.betavibePath)) return;
      const prompt = latestUserPrompt(event);
      const phase = classifyPrompt(prompt);
      if (!phase) return;
      const context = textOf(prompt, 1200).replace(/\s+/g, " ").trim();
      const cacheKey = `${phase}:${context.slice(0, 240)}`;
      let output = promptCache.get(cacheKey);
      if (!output) {
        const started = Date.now();
        const res = await runBetavibe(c, ["resolve", phase, "--context", context, "--limit", "3", "--gbrain-limit", "3"], c.maxResolveMs);
        const durationMs = Date.now() - started;
        appendAudit(c, { type: "resolver", phase, durationMs, ok: res.ok, timeout: !!res.timeout });
        if (!res.ok || res.timeout) return { prependContext: `\n[Betavibe skipped: resolver exceeded ${c.maxResolveMs}ms or failed; continue without blocking.]\n` };
        output = res.stdout.slice(0, c.maxPromptChars);
        promptCache.set(cacheKey, output);
        if (promptCache.size > 50) promptCache.delete(promptCache.keys().next().value);
      }
      return { prependContext: `\n\n[Betavibe ${phase} context — apply before proceeding, do not quote verbatim if irrelevant]\n${output}\n[/Betavibe context]\n` };
    }, { priority: 40 });

    api.on("after_tool_call", async (event, ctx) => {
      const c = cfg(event, ctx, fallbackConfig);
      if (!c.enabled) return;
      const runId = runKey(ctx, event);
      const blob = textOf(event, 5000);
      const errorish = /(traceback|exception|error|failed|exit code [1-9]|timed out|timeout|permission denied|not found)/i.test(blob);
      const files = [];
      const params = event?.params || {};
      for (const k of ["path", "file", "workdir"]) if (typeof params[k] === "string") files.push(params[k]);
      record(runId, { toolCalls: (stateByRun.get(runId)?.toolCalls || 0) + 1, errors: (stateByRun.get(runId)?.errors || 0) + (errorish ? 1 : 0), attempts: (stateByRun.get(runId)?.attempts || 0) + (errorish ? 1 : 0), filesTouched: files, snippet: errorish ? blob.slice(0, 700) : undefined });
    }, { priority: 0 });

    api.on("agent_end", async (event, ctx) => {
      const c = cfg(event, ctx, fallbackConfig);
      if (!c.enabled || !existsSync(c.betavibePath)) return;
      const runId = runKey(ctx, event);
      const s = stateByRun.get(runId) || { startedAt: Date.now(), toolCalls: 0, errors: 0, attempts: 0, filesTouched: new Set(), snippets: [] };
      const durationMs = Number(event?.durationMs || (Date.now() - s.startedAt));
      const minutes = Math.max(0, Math.round(durationMs / 60000));
      const finalText = textOf(event?.finalMessage || event?.reply || event, 3000);
      const verified = /(test.*pass|tests? passed|build.*pass|verified|驗證|測試通過|ci.*success|github actions.*success)/i.test(finalText);
      const risky = /(auth|oauth|token|billing|deploy|ci|cron|database|migration|schema|config|external api|webhook|hook|plugin)/i.test(finalText + " " + (s.snippets || []).join(" "));
      if (minutes < c.minDebugMinutes && s.errors < 2 && !risky) return;
      const context = [`duration=${minutes}m`, `errors=${s.errors}`, `tools=${s.toolCalls}`, `files=${[...(s.filesTouched || [])].slice(0, 8).join(",")}`, finalText.slice(0, 900), ...(s.snippets || []).slice(-3)].join("\n");
      const args = ["should-capture", "--debug-minutes", String(minutes), "--attempts", String(Math.max(0, s.attempts || s.errors || 0)), "--context", context];
      if (s.errors > 0) args.splice(5, 0, "--had-error-log");
      if (verified) args.splice(5, 0, "--final-fix-verified");
      if (risky) args.splice(5, 0, "--affects-spec-or-tool-choice");
      const started = Date.now();
      const res = await runBetavibe(c, args, c.maxSessionChecksMs);
      const decision = res.stdout.includes("CAPTURE_RECOMMENDED") ? "CAPTURE_RECOMMENDED" : res.stdout.includes("CAPTURE_AFTER_VERIFICATION") ? "CAPTURE_AFTER_VERIFICATION" : "DO_NOT_CAPTURE_YET";
      appendAudit(c, { type: "post_run_capture_check", runId, durationMs: Date.now() - started, decision, dryRun: c.dryRun, minutes, errors: s.errors, attempts: s.attempts, verified });
      stateByRun.delete(runId);
      if (decision === "CAPTURE_RECOMMENDED" || decision === "CAPTURE_AFTER_VERIFICATION") {
        try {
          api.enqueueNextTurnInjection?.({
            sessionKey: ctx.sessionKey,
            idempotencyKey: `${ID}:${runId}:${decision}`,
            ttlMs: 24 * 60 * 60 * 1000,
            placement: "append_context",
            text: `[Betavibe ${decision}] A hard-won debugging lesson may need human-approved capture. Ask approval before writing reviewed registry. Detector output:\n${res.stdout.slice(0, 1200)}`,
          });
        } catch {}
      }
    }, { priority: 0 });
  },
});
