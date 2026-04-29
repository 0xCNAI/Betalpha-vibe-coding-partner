from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from .gitmine import mine_git
from .models import Insight
from .registry import init_registry, list_insights, list_pending, resolve_registry, write_insight, write_pending
from .search import search_insights


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
    return 0


def cmd_scan_git(args) -> int:
    registry = resolve_registry(args.registry)
    init_registry(registry)
    repo = Path(args.repo).expanduser().resolve()
    candidates = mine_git(repo, since=args.since, max_commits=args.max_commits)
    for c in candidates[: args.limit]:
        write_pending(c, registry)
    print(f"scanned {repo}")
    print(f"wrote {min(len(candidates), args.limit)} pending candidates to {registry / 'pending'}")
    if candidates:
        print("\nTop candidates:")
        for c in candidates[: min(5, args.limit)]:
            print(f"- {c['id']} [{c['score']}] {c['title']} — {', '.join(c['reasons'])}")
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
    p.set_defaults(func=cmd_capture)

    p = sub.add_parser("scan-git")
    p.add_argument("repo")
    p.add_argument("--since", default=None)
    p.add_argument("--max-commits", type=int, default=300)
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--with-github", action="store_true", help="reserved; local git mining works without GitHub API")
    p.set_defaults(func=cmd_scan_git)

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
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
