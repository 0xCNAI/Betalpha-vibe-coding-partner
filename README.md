# Betalpha Vibe Coding Partner

Drop this folder into a project and coding agents should automatically reuse and capture hard-won development insights.

It is designed for OpenClaw, Claude Code, Codex, Cowork, Cursor, and any tool that reads project instruction files.

## What you should experience

You should **not** need to remember commands.

A good agent will:

1. **Before writing a spec**: search prior insights and add relevant guardrails.
2. **Before implementation**: check known pitfalls / wrong paths / tool-choice lessons.
3. **After painful debugging**: notice the session is worth capturing, ask you for approval, then save a structured insight.
4. **When onboarding old projects**: scan git / GitHub history and produce reviewable candidate insights.

## Install into a project

Copy this whole folder into your project, or keep it as a shared submodule / folder, then run the full installer from inside the Betavibe pack:

```bash
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --self-test
```

The installer adds a managed root contract, agent skills, local hook wrappers, and initializes the registry. It writes managed blocks instead of overwriting existing instructions.

Recommended shared registry:

```bash
export BETAVIBE_REGISTRY="$HOME/.betalpha-vibe/registry"
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --registry "$BETAVIBE_REGISTRY" --self-test
```

If no shared registry is configured, it uses local `registry/`.

## Install and use by harness

The installer writes managed instruction blocks instead of replacing your existing files. In normal product repos, one install prepares all instruction-file based harnesses:

```bash
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --self-test
```

### Codex

Codex reads the root `AGENTS.md` and the generated `.codex/AGENTS.md`.

Installed files:

- `AGENTS.md`
- `.codex/AGENTS.md`
- `.betavibe/hooks/pre_spec.sh`
- `.betavibe/hooks/pre_implement.sh`
- `.betavibe/hooks/verify.sh`
- `.betavibe/hooks/learn.sh`

Expected agent behavior:

```bash
.betavibe/hooks/pre_spec.sh "<task/context>"
.betavibe/hooks/pre_implement.sh "<plan/files/risks>"
.betavibe/hooks/verify.sh --task "<bug task>" --no-fail -- <failing reproduction>
.betavibe/hooks/verify.sh --task "<bug task>" -- <passing verification>
.betavibe/hooks/learn.sh
```

`learn.sh` creates a pending lesson only. Codex must ask before `promote` or `capture --sync-gbrain`.

### Claude Code

Claude Code reads `CLAUDE.md`, `.claude/CLAUDE.md`, and the installed skill.

Installed files:

- `CLAUDE.md`
- `.claude/CLAUDE.md`
- `.claude/skills/betavibe-insight/SKILL.md`
- `skills/betavibe-insight/SKILL.md`
- `.betavibe/hooks/*.sh`

Expected agent behavior is the same lifecycle as Codex: run resolver hooks before spec/implementation, use `verify.sh` for failing and passing debug evidence, then `learn.sh` to create a human-reviewable pending lesson.

### OpenClaw

OpenClaw can use the same installed `AGENTS.md` contract. For stronger automatic behavior, enable the lifecycle plugin after installing Betavibe into the target project:

```bash
openclaw plugins install --link --dangerously-force-unsafe-install /path/to/project/Betalpha-vibe-coding-partner/adapters/openclaw/betavibe-lifecycle-plugin
openclaw plugins enable betavibe-lifecycle
openclaw config set plugins.entries.betavibe-lifecycle '{
  "enabled": true,
  "hooks": { "allowConversationAccess": true },
  "config": {
    "projectRoot": "/path/to/project",
    "betavibePath": "/path/to/project/Betalpha-vibe-coding-partner",
    "registry": "/path/to/project/.betavibe/registry",
    "enabled": true,
    "maxResolveMs": 2500,
    "maxPromptChars": 3500,
    "minDebugMinutes": 20,
    "maxSessionChecksMs": 3000,
    "dryRun": true
  }
}' --strict-json --merge
openclaw gateway restart
```

Verify OpenClaw wiring:

```bash
openclaw plugins inspect betavibe-lifecycle --json
cat /path/to/project/.betavibe/lifecycle-events.jsonl
```

The plugin injects resolver context before coding/spec turns and checks whether a debugging session should be captured. It does not write reviewed insights automatically.

## Agent-facing contract

Agents should read the root managed contract and/or the installed `betavibe-insight` skill, then use resolver commands automatically:

```bash
python3 -m betavibe resolve pre_spec --context "<task>"
python3 -m betavibe resolve pre_implement --context "<plan and files>"
python3 -m betavibe should-capture --debug-minutes 35 --attempts 3 --had-error-log --final-fix-verified --context "<bug summary>"
```

Registry routing is project-first: if `--registry` / `BETAVIBE_REGISTRY` is omitted, Betavibe walks upward from the current working directory and uses the nearest `.betavibe/registry`. This prevents vendored installs from accidentally writing runtime evidence into `vendor/Betalpha-vibe-coding-partner/registry`.

If capture is recommended, the agent asks you for approval in chat, then writes the insight.

## Human-facing commands, only when needed

Check relevant insights:

```bash
python3 -m betavibe advise "oauth line bot refresh token"
```

Capture a reviewed lesson:

```bash
python3 -m betavibe capture \
  --type pitfall \
  --title "LINE OAuth token refresh silently kills webhook" \
  --summary "Token rotation caused webhook delivery to stop until self-test revalidation was added." \
  --tags "oauth,line-bot,webhook" \
  --tech "node,line" \
  --symptom "Webhook stopped receiving events after token refresh." \
  --root-cause "Refresh flow updated credentials without revalidating delivery." \
  --wrong-paths "Rotating only the token did not prove webhook delivery still worked." \
  --fix "Add webhook self-test after token refresh and fail deploy if it does not pass." \
  --prevention-signal "Before deploying any LINE OAuth refresh flow, add or run webhook delivery self-test." \
  --verify-trigger "When LINE Messaging API auth behavior changes."
```

Scan a project’s evolution for candidate insights:

```bash
python3 -m betavibe scan-git /path/to/project --with-github --since "1 year ago"
python3 -m betavibe pending
python3 -m betavibe promote <pending-id>
```

Run the dogfood loop against a real repo and produce a usefulness report:

```bash
python3 -m betavibe dogfood /path/to/project --out /tmp/betavibe-dogfood.md
```

`dogfood` mines local git history, writes pending candidates, probes `pre_spec` and `pre_implement` resolver behavior, and emits a markdown report. It does not need GitHub, GBrain, or network access unless `--with-github` is explicitly passed.

Run an end-to-end acceptance demo that proves the installed workflow:

```bash
python3 -m betavibe acceptance-demo /tmp/betavibe-acceptance --force
```

`acceptance-demo` creates a temporary git project, installs Betavibe, reproduces a failing test through `.betavibe/hooks/verify.sh`, fixes it, captures the passing verification, runs `.betavibe/hooks/learn.sh`, preserves the pending runtime lesson as an artifact, simulates human approval by promoting it without GBrain sync, and writes a report with Codex / Claude Code / OpenClaw installation evidence plus `pre_spec` and `pre_implement` resolver output.

For already-built projects, use forensic excavation instead of raw candidate review:

```bash
python3 -m betavibe excavate /path/to/project --out /tmp/betavibe-excavation.md
```

`excavate` groups fix/regression commits with adjacent context commits and stores evidence-backed pending drafts. This reduces human work from writing lessons to approving/rejecting inferred lessons.

Check cross-harness memory wiring:

```bash
python3 -m betavibe doctor
```

Betavibe's source of truth is the local `registry/` committed to git. GBrain is optional semantic recall: if installed and healthy, `--sync-gbrain` mirrors reviewed insights there; if missing, agents keep working from local registry and `doctor` explains the setup gap.

After promoting reviewed insights, sync them across devices/harnesses by committing the registry:

```bash
python3 -m betavibe sync --repo /path/to/project --push
```

Runtime capture records implementation evidence while work happens:

```bash
RUN_ID=$(python3 -m betavibe run-start --task "fix auth bootstrap" --harness openclaw --repo /path/to/project)
python3 -m betavibe run-exec "$RUN_ID" --cwd /path/to/project -- npm test -- --runInBand
python3 -m betavibe run-exec "$RUN_ID" --cwd /path/to/project -- npm run build
python3 -m betavibe run-finish "$RUN_ID" --repo /path/to/project --json
```

A high-confidence runtime draft needs failed command evidence plus a later passing verification. Human review should be reduced to approve / edit one sentence / discard.

For zero-reminder harness compliance, install strict runtime enforcement:

```bash
python3 -m betavibe install --project /path/to/project --pack-path Betalpha-vibe-coding-partner --enforce-runtime
```

This installs lightweight git gates. The pre-commit hook requires recent passing verification for normal work. A commit-msg hook becomes stricter only when the commit message looks like bugfix/regression/auth/migration/schema/deploy/security work; those high-risk commits require both failed-command evidence and later passing verification. This keeps Betavibe as an immune system, not a full-time flight recorder. Use `--strict-runtime` only for focused debugging drills where every commit should require failed+passed evidence.

Install also writes `.betavibe/GBRAIN_STATUS.md`. Agents must read it instead of silently assuming GBrain exists. If GBrain is missing/unhealthy, Betavibe keeps working from the local git registry, but semantic sync/recall is disabled until `gbrain doctor` passes.

## Insight types

- `pitfall`: hard-won bug / failure mode and verified fix.
- `decision`: choice among options and accepted trade-offs.
- `pattern`: reusable implementation / delivery pattern.
- `tool_choice`: when to use OpenClaw / Claude Code / Codex / Cowork / local scripts / browser / APIs.
- `spec_guardrail`: checklist item that should shape future specs.

## Why approval is required

Bad memory is worse than missing memory. Git history and agents can draft candidates, but only reviewed insights should enter `registry/insights/`.

## Hybrid with GBrain

Betavibe is the workflow / schema / resolver layer. GBrain is the semantic memory backend.

- `capture --sync-gbrain` writes reviewed insights to local markdown and GBrain when available.
- `resolve` searches local reviewed insights and also queries GBrain semantic memory unless `--no-gbrain` is passed.
- Local markdown remains the source of truth; GBrain improves recall across wording, projects, and related concepts.

## Testing whether it is useful

Read `docs/USEFULNESS_TESTING.md`. The short version: test against old painful bugs and compare resolver-assisted vs non-assisted agents. If it only creates nicer notes but does not avoid wrong paths, improve it or kill it.

## Key files

- `AGENTS.md` — main drop-in instructions for all agents.
- `CLAUDE.md`, `.claude/CLAUDE.md` — Claude Code entrypoints.
- `.codex/AGENTS.md` — Codex entrypoint.
- `COWORK.md` — Cowork-readable guidance.
- `docs/RESOLVERS.md` — lifecycle resolver behavior.
- `docs/USEFULNESS_TESTING.md` — A/B tests for real usefulness.
- `skills/betavibe-insight/SKILL.md` — bundled agent skill for correct capture workflow.
- `.betavibe/hooks/` after install — deterministic wrappers agents/hooks can call.
- `docs/OPENCLAW_LIFECYCLE.md` — optional OpenClaw plugin integration for automatic resolver/capture lifecycle hooks.
- `betavibe/` — resolver CLI.
- `registry/insights/` — reviewed insight database.
- `registry/pending/` — auto-mined candidates awaiting review.
