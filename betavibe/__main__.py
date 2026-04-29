from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from .gitmine import mine_git
from .excavate import excavate, write_report as write_excavation_report
from .models import Insight
from .registry import init_registry, list_insights, list_pending, resolve_registry, write_insight, write_pending
from .search import search_insights
from . import gbrain_adapter
from .install import install_contract as install_agent_contract, install_all
from .sync import commit_registry
from .runtime_capture import start_run, run_command, finish_run, verify_command, learn_from_run
from .enforce import check_runtime_required


def csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [x.strip() for x in value.split(",") if x.strip()]


def cmd_init(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    print(f"initialized registry: {registry}")
    return 0


def cmd_advise(args) -> int:
    registry = resolve_registry(args.registry)
    insights = list_insights(registry)
    hits = search_insights(insights, args.query, limit=args.limit)
    if args.json:
        print(json.dumps([{"score": s, "path": str(i.path), "title": i.title, "type": i.type, "matched": m, "prevention_signal": i.prevention_signal, "summary": i.summary} for s, i, m in hits], ensure_ascii=False, indent=2))
        return 0
    if not hits:
        print(f"No relevant insights found for: {args.query}")
        return 0
    print(f"Found {len(hits)} relevant insights for: {args.query}\n")
    for score, insight, matched in hits:
        print(f"## [{insight.type}] {insight.title}")
        print(f"score: {score:.2f} | matched: {', '.join(matched)}")
        print(f"summary: {insight.summary}")
        print(f"prevention_signal: {insight.prevention_signal}")
        if insight.path:
            print(f"path: {insight.path}")
        print("")
    return 0


def cmd_capture(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    body = {
        "symptom": args.symptom or "",
        "root_cause": args.root_cause or "",
        "wrong_paths": args.wrong_paths or "",
        "fix": args.fix or "",
        "decision": args.decision or "",
        "tradeoffs": args.tradeoffs or "",
        "pattern": args.pattern or "",
        "tool_guidance": args.tool_guidance or "",
        "evidence": args.evidence or "",
    }
    insight = Insight(
        title=args.title,
        type=args.type,
        tags=csv(args.tags),
        tech_stack=csv(args.tech),
        summary=args.summary or args.title,
        prevention_signal=args.prevention_signal,
        verify_trigger=args.verify_trigger,
        source={"kind": "manual", "created_by": os.environ.get("USER", "unknown")},
        body=body,
    )
    path = write_insight(insight, registry)
    print(f"wrote insight: {path}")
    if args.sync_gbrain:
        slug = gbrain_adapter.sync_insight(insight)
        if slug:
            print(f"synced to gbrain: {slug}")
        else:
            print("gbrain sync skipped/failed; local registry remains source of truth")
    return 0


def cmd_scan_git(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    repo = Path(args.repo).expanduser().resolve()
    candidates = mine_git(repo, since=args.since, max_commits=args.max_commits, with_github=args.with_github)
    for c in candidates[: args.limit]:
        write_pending(c, registry)
    print(f"scanned {repo}")
    print(f"wrote {min(len(candidates), args.limit)} pending candidates to {registry / 'pending'}")
    if candidates:
        print("\nTop candidates:")
        for c in candidates[: min(5, args.limit)]:
            print(f"- {c['id']} [{c['score']}] {c['title']} — {', '.join(c['reasons'])}")
    return 0


def _candidate_context(candidates: list[dict], fallback: str) -> str:
    if not candidates:
        return fallback
    lines = []
    for c in candidates[:3]:
        reasons = "; ".join(c.get("reasons", [])) or "git history signal"
        files = ", ".join(c.get("source", {}).get("files", [])[:5])
        if files:
            lines.append(f"{c.get('title')} | reasons: {reasons} | files: {files}")
        else:
            lines.append(f"{c.get('title')} | reasons: {reasons}")
    return "\n".join(lines)


def _local_resolver_section(phase: str, context: str, insights: list[Insight], limit: int = 5) -> str:
    phase_terms = {
        "pre_spec": "spec guardrail decision pattern tool choice architecture migration integration",
        "pre_implement": "pitfall wrong paths fix implementation test deploy config migration",
    }
    hits = search_insights(insights, f"{context} {phase_terms.get(phase, '')}", limit=limit)
    lines = [f"### {phase}", "", "```text", context, "```", ""]
    if not hits:
        lines.extend([
            "No matching local reviewed insights.",
            "",
            "Default verification: add a test/build/run/manual reproduction gate before claiming done.",
            "",
        ])
        return "\n".join(lines)
    lines.append(f"Relevant local reviewed insights: {len(hits)}")
    lines.append("")
    for score, insight, matched in hits:
        lines.append(f"- **[{insight.type}] {insight.title}** — score {score:.2f}; matched: {', '.join(matched)}")
        lines.append(f"  - prevention: {insight.prevention_signal}")
        lines.append(f"  - verify: {insight.verify_trigger}")
        if insight.path:
            lines.append(f"  - path: `{insight.path}`")
    lines.append("")
    return "\n".join(lines)


def cmd_dogfood(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    repo = Path(args.repo).expanduser().resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"not a git repository: {repo}")

    candidates = mine_git(repo, since=args.since, max_commits=args.max_commits, with_github=args.with_github)
    selected = candidates[: args.limit]
    for c in selected:
        write_pending(c, registry)

    insights = list_insights(registry)
    pending = list_pending(registry)
    pre_spec_context = args.pre_spec_context or _candidate_context(
        selected,
        f"Plan the next change in {repo.name}; check prior decisions, guardrails, risky subsystems, and verification before writing a spec.",
    )
    pre_implement_context = args.pre_implement_context or _candidate_context(
        selected,
        f"Implement the next change in {repo.name}; check pitfalls, wrong paths, risky files, and required tests before editing.",
    )

    if args.out:
        out = Path(args.out).expanduser()
    else:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        out = repo / ".betavibe" / "reports" / f"dogfood-{stamp}.md"
    if not out.is_absolute():
        out = (Path.cwd() / out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Betavibe Dogfood Report",
        "",
        f"- repo: `{repo}`",
        f"- registry: `{registry}`",
        f"- local git candidates mined: {len(candidates)}",
        f"- pending candidates written this run: {len(selected)}",
        f"- reviewed insights available: {len(insights)}",
        f"- pending candidates in registry: {len(pending)}",
        f"- github mining: {'on' if args.with_github else 'off'}",
        "",
        "## Top mined candidates",
        "",
    ]
    if selected:
        for c in selected[:10]:
            lines.append(f"- `{c['id']}` [{c.get('score')}] {c.get('title')} — {'; '.join(c.get('reasons', []))}")
    else:
        lines.append("No candidates found from local git history. This can be fine for clean or tiny repos; usefulness should be tested on a repo with real failures.")
    lines.extend([
        "",
        "## Resolver probes",
        "",
        _local_resolver_section("pre_spec", pre_spec_context, insights, limit=args.resolve_limit),
        _local_resolver_section("pre_implement", pre_implement_context, insights, limit=args.resolve_limit),
        "## Readout",
        "",
    ])
    if selected and insights:
        lines.append("This repo has mined candidates and reviewed insights; compare the resolver probes against a no-memory baseline before trusting usefulness.")
    elif selected:
        lines.append("Candidates were mined, but reviewed insights are empty. Promote reviewed lessons before expecting resolver impact.")
    else:
        lines.append("No mined candidates. Try a larger `--max-commits`, an older repo, or `--with-github` if GitHub auth is available.")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")

    print(f"dogfood report: {out}")
    print(f"candidates mined: {len(candidates)}; written: {len(selected)}")
    print(f"reviewed insights: {len(insights)}; pending: {len(pending)}")
    return 0


def cmd_excavate(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    repo = Path(args.repo).expanduser().resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"not a git repository: {repo}")
    findings = excavate(repo, max_commits=args.max_commits, cluster_window=args.cluster_window, limit=args.limit, include_patch=not args.no_patch)
    for finding in findings:
        write_pending(finding, registry)
    if args.out:
        out = Path(args.out).expanduser()
    else:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        out = repo / ".betavibe" / "reports" / f"excavation-{stamp}.md"
    if not out.is_absolute():
        out = (Path.cwd() / out).resolve()
    write_excavation_report(findings, out, repo)
    print(f"excavation report: {out}")
    print(f"forensic findings: {len(findings)}; pending written: {len(findings)}")
    if findings:
        print("top findings:")
        for f in findings[: min(5, len(findings))]:
            print(f"- {f['id']} [{f['score']}/{f['confidence']}] {f['title']}")
    return 0


def cmd_doctor(args) -> int:
    registry = resolve_registry(args.registry)
    print("Betavibe doctor")
    print(f"- registry: {registry}")
    print(f"- reviewed insights: {len(list_insights(registry))}")
    print(f"- pending candidates: {len(list_pending(registry))}")
    g = gbrain_adapter.status()
    print(f"- gbrain installed: {'yes' if g.installed else 'no'}")
    print(f"- gbrain healthy: {'yes' if g.healthy else 'no'}")
    print(f"- gbrain binary: {g.binary or 'not found on PATH'}")
    print(f"- gbrain detail: {g.detail}")
    print(f"- gbrain guidance: {g.install_hint}")
    print("- cross-harness source of truth: local registry files committed to git")
    print("- semantic layer: GBrain optional; if missing, resolvers fall back to local registry")
    return 0 if (not args.require_gbrain or g.healthy) else 1


def cmd_enforce(args) -> int:
    registry = resolve_registry(args.registry)
    commit_message = args.commit_message
    if args.commit_message_file:
        try:
            commit_message = Path(args.commit_message_file).read_text(encoding="utf-8")
        except OSError as exc:
            print(f"Could not read commit message file: {exc}")
            return 1
    mode = args.mode or ("strict" if args.require_failed else "pass")
    ok, message = check_runtime_required(registry, max_age_minutes=args.max_age_minutes, require_failed=bool(args.require_failed), mode=mode, commit_message=commit_message)
    print(message)
    return 0 if ok else 1


def cmd_sync(args) -> int:
    registry = resolve_registry(args.registry)
    repo = Path(args.repo).expanduser().resolve()
    result = commit_registry(repo, registry, args.message, push=args.push)
    print(result.message)
    if result.changed:
        print("changed:")
        for path in result.changed:
            print(f"- {path}")
    if result.commit:
        print(f"commit: {result.commit}")
    if result.pushed:
        print("pushed: yes")
    return 0 if result.ok else 1


def cmd_run_start(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    repo = Path(args.repo).expanduser().resolve() if args.repo else None
    run_id = start_run(registry, args.task, harness=args.harness, repo=repo)
    print(run_id)
    return 0


def cmd_run_exec(args) -> int:
    registry = resolve_registry(args.registry)
    cwd = Path(args.cwd).expanduser().resolve() if args.cwd else Path.cwd()
    command = args.command[1:] if args.command and args.command[0] == "--" else args.command
    if not command:
        raise SystemExit("run-exec requires a command after --")
    code = run_command(registry, args.run_id, command, cwd=cwd)
    if args.no_fail:
        return 0
    return code


def cmd_run_finish(args) -> int:
    registry = resolve_registry(args.registry)
    repo = Path(args.repo).expanduser().resolve() if args.repo else None
    draft = finish_run(registry, args.run_id, repo=repo)
    if args.json:
        print(json.dumps(draft, ensure_ascii=False, indent=2))
    else:
        print(f"runtime draft: {draft['title']}")
        print(f"confidence: {draft['confidence']}")
        print(f"type: {draft['type']}")
        print(f"symptom: {draft['symptom']}")
        print(f"fix: {draft['fix']}")
        print(f"prevention_signal: {draft['prevention_signal']}")
    return 0


def cmd_pending(args) -> int:
    registry = resolve_registry(args.registry)
    pending = list_pending(registry)
    if args.json:
        print(json.dumps(pending, ensure_ascii=False, indent=2))
        return 0
    if not pending:
        print("No pending candidates.")
        return 0
    for p in pending[: args.limit]:
        print(f"## {p['id']} [{p.get('score')}] {p.get('title')}")
        print(p.get("summary", ""))
        print("reasons: " + "; ".join(p.get("reasons", [])))
        print(f"source: {p.get('source', {}).get('kind')} {p.get('source', {}).get('sha', '')[:12]}")
        print("")
    return 0


def cmd_promote(args) -> int:
    registry = resolve_registry(args.registry)
    matches = [p for p in list_pending(registry) if p["id"] == args.id]
    if not matches:
        raise SystemExit(f"pending id not found: {args.id}")
    p = matches[0]
    draft = p.get("draft", {})
    insight = Insight(
        title=args.title or p["title"],
        type=args.type or p.get("type", "pitfall"),
        tags=csv(args.tags) or p.get("tags", ["git-history"]),
        tech_stack=csv(args.tech) or p.get("tech_stack", []),
        summary=args.summary or p["summary"],
        prevention_signal=args.prevention_signal or draft.get("prevention_signal", "Review this candidate before similar changes."),
        verify_trigger=args.verify_trigger or draft.get("verify_trigger", "When related subsystem changes."),
        source=p.get("source", {}),
        body={
            "symptom": args.symptom or draft.get("symptom", ""),
            "root_cause": args.root_cause or draft.get("root_cause", ""),
            "wrong_paths": args.wrong_paths or draft.get("wrong_paths", ""),
            "fix": args.fix or draft.get("fix", ""),
            "evidence": draft.get("evidence", ""),
        },
    )
    path = write_insight(insight, registry)
    Path(p["_path"]).unlink(missing_ok=True)
    print(f"promoted pending candidate to: {path}")
    print("Review the file and refine root_cause/fix if git log alone was insufficient.")
    return 0



def cmd_recall(args) -> int:
    class Obj: pass
    o = Obj()
    o.phase = "pre_implement"
    o.context = args.context
    o.limit = args.limit
    o.gbrain_limit = args.gbrain_limit
    o.no_gbrain = args.no_gbrain
    return cmd_resolve(o)


def cmd_verify(args) -> int:
    registry = resolve_registry(args.registry)
    cwd = Path(args.cwd).expanduser().resolve() if args.cwd else Path.cwd()
    repo = Path(args.repo).expanduser().resolve() if args.repo else (cwd if (cwd / ".git").exists() else None)
    command = args.command[1:] if args.command and args.command[0] == "--" else args.command
    if not command:
        raise SystemExit("verify requires a command after --")
    code, run_id, draft = verify_command(registry, args.task, command, cwd=cwd, harness=args.harness, repo=repo, no_fail=args.no_fail, run_id=args.run_id)
    print(f"\nBetavibe verify captured run: {run_id}")
    print(f"confidence: {draft.get('confidence')}")
    print(f"failed evidence: {'yes' if any(not c.get('ok') for c in draft.get('evidence', {}).get('commands', [])) else 'no'}")
    print(f"changed_files: {len(draft.get('evidence', {}).get('changed_files', []))}")
    return code


def cmd_learn(args) -> int:
    registry = resolve_registry(args.registry)
    message, path = learn_from_run(registry, run_id=args.run_id)
    print(message)
    return 0 if (path or args.allow_noop) else 1


def cmd_resolve(args) -> int:
    registry = resolve_registry(args.registry)
    insights = list_insights(registry)
    phase_terms = {
        "pre_spec": "spec guardrail decision pattern tool choice architecture migration integration",
        "pre_implement": "pitfall wrong paths fix implementation test deploy config migration",
        "post_debug": "pitfall bug fix root cause wrong paths error regression timeout failure",
        "post_session": "decision pattern tool choice spec guardrail reusable lesson",
    }
    query = f"{args.context} {phase_terms.get(args.phase, '')}"
    hits = search_insights(insights, query, limit=args.limit)
    print(f"resolver: {args.phase}")
    print(f"context: {args.context}")
    print("")
    if not hits:
        print("No matching local reviewed insights.")
    else:
        print(f"Relevant local reviewed insights: {len(hits)}\n")
    spec_guardrails = []
    wrong_paths = []
    tool_notes = []
    verification = []
    for score, insight, matched in hits:
        print(f"## [{insight.type}] {insight.title}")
        print(f"matched: {', '.join(matched)} | score: {score:.2f}")
        print(f"summary: {insight.summary}")
        print(f"ACTION / prevention_signal: {insight.prevention_signal}")
        if insight.path:
            print(f"read: {insight.path}")
        print("")
        spec_guardrails.append(insight.prevention_signal)
        if insight.body.get("wrong_paths"):
            wrong_paths.append(insight.body["wrong_paths"][:300])
        if insight.type == "tool_choice" or insight.body.get("tool_guidance"):
            tool_notes.append(insight.body.get("tool_guidance") or insight.summary)
        verification.append(insight.verify_trigger)

    gbrain_hits = [] if args.no_gbrain else gbrain_adapter.query(query, limit=max(0, args.gbrain_limit))
    if gbrain_hits:
        print("## GBrain semantic hits")
        for h in gbrain_hits:
            stale = " STALE" if h.stale else ""
            print(f"- {h.slug} ({h.score:.3f}){stale}")
            print("  " + h.snippet.replace("\n", "\n  ")[:500])
        print("")

    if args.phase in ("pre_spec", "pre_implement"):
        print("# Spec-ready synthesis")
        print("## Spec guardrails")
        for item in spec_guardrails[:8] or ["No reviewed local guardrail found; define verification before implementation."]:
            print(f"- {item}")
        print("## Known wrong paths")
        for item in wrong_paths[:5] or ["No local wrong-path evidence found."]:
            print(f"- {item}")
        print("## Tools to prefer / avoid")
        for item in tool_notes[:5] or ["No specific prior tool-choice insight found; choose the simplest verifiable tool path."]:
            print(f"- {item}")
        print("## Verification requirements")
        for item in verification[:8] or ["Add a test/build/run/manual reproduction gate before claiming done."]:
            print(f"- Re-check when: {item}")
        print("\nAgent instruction: apply these before proceeding. Do not merely mention them.")
    return 0


def cmd_should_capture(args) -> int:
    score = 0
    reasons = []
    if args.debug_minutes >= 20:
        score += 3
        reasons.append(f"debugging took {args.debug_minutes} minutes")
    elif args.debug_minutes >= 10:
        score += 1
        reasons.append(f"debugging took {args.debug_minutes} minutes")
    if args.attempts >= 2:
        score += 3
        reasons.append(f"{args.attempts} wrong attempts")
    elif args.attempts == 1:
        score += 1
        reasons.append("one wrong attempt")
    if args.had_error_log:
        score += 2
        reasons.append("specific error/log/failed behavior observed")
    if args.final_fix_verified:
        score += 3
        reasons.append("final fix verified")
    risky_words = ["auth", "oauth", "token", "billing", "deploy", "ci", "cron", "database", "migration", "schema", "config", "external api", "webhook", "data loss"]
    if any(w in args.context.lower() for w in risky_words):
        score += 2
        reasons.append("risky subsystem")
    if args.affects_spec_or_tool_choice:
        score += 2
        reasons.append("would affect future spec/tool choice")

    print(f"capture_score: {score}")
    for r in reasons:
        print(f"- {r}")
    print("")
    if score >= 7 and args.final_fix_verified:
        print("CAPTURE_RECOMMENDED")
        print("Ask the human for approval, then capture symptom/root cause/wrong paths/fix/prevention_signal/verify_trigger.")
    elif score >= 7:
        print("CAPTURE_AFTER_VERIFICATION")
        print("This seems important, but do not save until the final fix is verified.")
    else:
        print("DO_NOT_CAPTURE_YET")
        print("Keep notes if useful, but avoid polluting the reviewed registry.")
    return 0


def cmd_install_agent_contract(args) -> int:
    project = Path(args.project).expanduser().resolve()
    changed = install_agent_contract(project, pack_path=args.pack_path)
    if changed:
        print("installed Betavibe agent contract into:")
        for path in changed:
            print(f"- {path}")
    else:
        print("Betavibe agent contract already up to date.")
    print("Now agents that read root AGENTS/CLAUDE/Codex instructions will automatically run resolvers.")
    return 0


def cmd_install(args) -> int:
    project = Path(args.project).expanduser().resolve()
    registry = resolve_registry(args.registry)
    init_registry(registry)
    result = install_all(project, pack_path=args.pack_path, enforce_runtime=args.enforce_runtime, strict_runtime=args.strict_runtime)
    print(f"initialized registry: {registry}")
    for section, paths in result.items():
        if paths:
            print(f"installed/updated {section}:")
            for path in paths:
                print(f"- {path}")
        else:
            print(f"{section}: already up to date")
    if args.self_test:
        print("")
        class Obj: pass
        t = Obj(); t.project = str(project); t.pack_path = args.pack_path
        return cmd_self_test(t)
    print("Run `python3 -m betavibe self-test --project <project>` to verify installation behavior.")
    return 0


def cmd_self_test(args) -> int:
    project = Path(args.project).expanduser().resolve() if args.project else Path.cwd()
    checks = []
    required = [
        project / "AGENTS.md",
        project / "CLAUDE.md",
        project / ".codex" / "AGENTS.md",
        project / ".claude" / "CLAUDE.md",
        project / "skills" / "betavibe-insight" / "SKILL.md",
        project / ".claude" / "skills" / "betavibe-insight" / "SKILL.md",
        project / ".betavibe" / "hooks" / "pre_spec.sh",
        project / ".betavibe" / "hooks" / "pre_implement.sh",
        project / ".betavibe" / "hooks" / "should_capture.sh",
    ]
    for path in required:
        ok = path.exists()
        checks.append(ok)
        print(("OK" if ok else "MISSING") + f" {path}")

    # Behavioral smoke checks for capture gate.
    import subprocess, sys
    scenarios = [
        ([sys.executable, "-m", "betavibe", "should-capture", "--debug-minutes", "45", "--attempts", "2", "--had-error-log", "--final-fix-verified", "--context", "webhook token refresh callbacks stopped"], "CAPTURE_RECOMMENDED"),
        ([sys.executable, "-m", "betavibe", "should-capture", "--debug-minutes", "2", "--attempts", "0", "--context", "README typo"], "DO_NOT_CAPTURE_YET"),
        ([sys.executable, "-m", "betavibe", "should-capture", "--debug-minutes", "40", "--attempts", "2", "--had-error-log", "--context", "database migration schema error"], "CAPTURE_AFTER_VERIFICATION"),
    ]
    for cmd, expected in scenarios:
        proc = subprocess.run(cmd, cwd=Path(__file__).resolve().parents[1], text=True, capture_output=True)
        ok = proc.returncode == 0 and expected in proc.stdout
        checks.append(ok)
        print(("OK" if ok else "FAIL") + f" behavior {expected}")
        if not ok:
            print(proc.stdout)
            print(proc.stderr)

    if all(checks):
        print("Betavibe install self-test passed.")
        return 0
    print("Betavibe install self-test failed.")
    return 1

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="betavibe", description="Betalpha Vibe Coding Partner CLI")
    parser.add_argument("--registry", help="Registry path; defaults to BETAVIBE_REGISTRY or ./registry")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("advise")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_advise)

    p = sub.add_parser("capture")
    p.add_argument("--type", required=True, choices=["pitfall", "decision", "pattern", "tool_choice", "spec_guardrail"])
    p.add_argument("--title", required=True)
    p.add_argument("--summary")
    p.add_argument("--tags", required=True)
    p.add_argument("--tech", default="")
    p.add_argument("--symptom")
    p.add_argument("--root-cause")
    p.add_argument("--wrong-paths")
    p.add_argument("--fix")
    p.add_argument("--decision")
    p.add_argument("--tradeoffs")
    p.add_argument("--pattern")
    p.add_argument("--tool-guidance")
    p.add_argument("--evidence")
    p.add_argument("--prevention-signal", required=True)
    p.add_argument("--verify-trigger", required=True)
    p.add_argument("--sync-gbrain", action="store_true", help="Also write this reviewed insight to GBrain when available")
    p.set_defaults(func=cmd_capture)

    p = sub.add_parser("scan-git")
    p.add_argument("repo")
    p.add_argument("--since", default=None)
    p.add_argument("--max-commits", type=int, default=300)
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--with-github", action="store_true", help="reserved; local git mining works without GitHub API")
    p.set_defaults(func=cmd_scan_git)

    p = sub.add_parser("dogfood")
    p.add_argument("repo", help="Git repository to mine and probe")
    p.add_argument("--since", default=None)
    p.add_argument("--max-commits", type=int, default=300)
    p.add_argument("--limit", type=int, default=20, help="Maximum pending candidates to write from this run")
    p.add_argument("--resolve-limit", type=int, default=5, help="Maximum reviewed insights per resolver probe")
    p.add_argument("--with-github", action="store_true", help="Also mine GitHub PR metadata when gh auth is available")
    p.add_argument("--out", help="Markdown report path; defaults to <repo>/.betavibe/reports/dogfood-<UTC timestamp>.md")
    p.add_argument("--pre-spec-context", help="Override generated pre_spec resolver probe context")
    p.add_argument("--pre-implement-context", help="Override generated pre_implement resolver probe context")
    p.set_defaults(func=cmd_dogfood)

    p = sub.add_parser("excavate")
    p.add_argument("repo", help="Git repository to forensically mine for fix/regression clusters")
    p.add_argument("--max-commits", type=int, default=300)
    p.add_argument("--cluster-window", type=int, default=4, help="Number of adjacent commits to include as context for each fix")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--out", help="Markdown report path; defaults to <repo>/.betavibe/reports/excavation-<UTC timestamp>.md")
    p.add_argument("--no-patch", action="store_true", help="Skip patch excerpts in evidence for faster/lighter output")
    p.set_defaults(func=cmd_excavate)

    p = sub.add_parser("doctor")
    p.add_argument("--require-gbrain", action="store_true", help="Exit non-zero if GBrain is missing/unhealthy")
    p.set_defaults(func=cmd_doctor)

    p = sub.add_parser("sync")
    p.add_argument("--repo", required=True, help="Git repo that contains the registry")
    p.add_argument("--message", default="chore(betavibe): sync reviewed insights", help="Commit message")
    p.add_argument("--push", action="store_true", help="Push after committing")
    p.set_defaults(func=cmd_sync)

    p = sub.add_parser("enforce")
    p.add_argument("--max-age-minutes", type=int, default=240)
    p.add_argument("--require-failed", type=int, default=0, help="Compatibility flag: require at least one failed command in recent runtime evidence")
    p.add_argument("--mode", choices=["pass", "strict", "auto"], default=None, help="pass=require passing verification only; strict=failed+passed; auto=strict only for bugfix/high-risk commit messages")
    p.add_argument("--commit-message", default=None, help="Commit message text for --mode auto")
    p.add_argument("--commit-message-file", default=None, help="Commit message file path for git commit-msg hook")
    p.set_defaults(func=cmd_enforce)

    p = sub.add_parser("recall")
    p.add_argument("context", help="Task/context to recall prior project lessons for")
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--gbrain-limit", type=int, default=3)
    p.add_argument("--no-gbrain", action="store_true")
    p.set_defaults(func=cmd_recall)

    p = sub.add_parser("verify")
    p.add_argument("--task", required=True, help="Task this verification belongs to; repeated calls with the same task append to one run")
    p.add_argument("--harness", default=None, help="openclaw, claude-code, codex, cursor, etc.")
    p.add_argument("--repo", help="Git repo being edited; defaults to cwd if cwd is a git repo")
    p.add_argument("--cwd", help="Working directory; defaults to current directory")
    p.add_argument("--run-id", default=None, help="Append to an explicit runtime run")
    p.add_argument("--no-fail", action="store_true", help="Return 0 even if the captured command failed")
    p.add_argument("command", nargs="+", help="Command to execute and capture; put after -- when command has flags")
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("learn")
    p.add_argument("--run-id", default=None, help="Runtime run to turn into a pending lesson; defaults to latest run")
    p.add_argument("--allow-noop", action="store_true", help="Return success even when the latest run is not strong enough to learn from")
    p.set_defaults(func=cmd_learn)

    p = sub.add_parser("run-start")
    p.add_argument("--task", required=True)
    p.add_argument("--harness", default=None, help="openclaw, claude-code, codex, cursor, etc.")
    p.add_argument("--repo", help="Git repo being edited")
    p.set_defaults(func=cmd_run_start)

    p = sub.add_parser("run-exec")
    p.add_argument("run_id")
    p.add_argument("--cwd", help="Working directory; defaults to current directory")
    p.add_argument("--no-fail", action="store_true", help="Return 0 even if the captured command failed")
    p.add_argument("command", nargs="+", help="Command to execute and capture; put after -- when command has flags")
    p.set_defaults(func=cmd_run_exec)

    p = sub.add_parser("run-finish")
    p.add_argument("run_id")
    p.add_argument("--repo", help="Git repo being edited")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_run_finish)

    p = sub.add_parser("pending")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_pending)

    p = sub.add_parser("promote")
    p.add_argument("id")
    p.add_argument("--type", choices=["pitfall", "decision", "pattern", "tool_choice", "spec_guardrail"])
    p.add_argument("--title")
    p.add_argument("--summary")
    p.add_argument("--tags")
    p.add_argument("--tech")
    p.add_argument("--symptom")
    p.add_argument("--root-cause")
    p.add_argument("--wrong-paths")
    p.add_argument("--fix")
    p.add_argument("--prevention-signal")
    p.add_argument("--verify-trigger")
    p.set_defaults(func=cmd_promote)

    p = sub.add_parser("resolve")
    p.add_argument("phase", choices=["pre_spec", "pre_implement", "post_debug", "post_session"])
    p.add_argument("--context", required=True)
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--gbrain-limit", type=int, default=3)
    p.add_argument("--no-gbrain", action="store_true")
    p.set_defaults(func=cmd_resolve)

    p = sub.add_parser("should-capture")
    p.add_argument("--debug-minutes", type=int, default=0)
    p.add_argument("--attempts", type=int, default=0)
    p.add_argument("--had-error-log", action="store_true")
    p.add_argument("--final-fix-verified", action="store_true")
    p.add_argument("--affects-spec-or-tool-choice", action="store_true")
    p.add_argument("--context", required=True)
    p.set_defaults(func=cmd_should_capture)

    p = sub.add_parser("install-agent-contract")
    p.add_argument("--project", required=True, help="Project root that should get AGENTS/CLAUDE/Codex resolver instructions")
    p.add_argument("--pack-path", default="Betalpha-vibe-coding-partner", help="Path from project root to this Betavibe pack")
    p.set_defaults(func=cmd_install_agent_contract)

    p = sub.add_parser("install")
    p.add_argument("--project", required=True, help="Project root to install root contract, skills, hooks, and registry into")
    p.add_argument("--pack-path", default="Betalpha-vibe-coding-partner", help="Path from project root to this Betavibe pack")
    p.add_argument("--self-test", action="store_true", help="Run install self-test after installation")
    p.add_argument("--enforce-runtime", action="store_true", help="Install git hooks: pre-commit requires recent passing verification; commit-msg requires failed evidence only for bugfix/high-risk messages")
    p.add_argument("--strict-runtime", action="store_true", help="With --enforce-runtime, require failed+passing evidence for every commit. Usually too heavy; use only for focused debugging drills.")
    p.set_defaults(func=cmd_install)

    p = sub.add_parser("self-test")
    p.add_argument("--project", help="Project root to verify; defaults to current directory")
    p.set_defaults(func=cmd_self_test)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
