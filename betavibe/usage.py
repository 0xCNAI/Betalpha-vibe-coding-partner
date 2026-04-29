from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
from .registry import personal_registry


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def usage_root(registry: Path) -> Path:
    # Usage is local observability, not source-of-truth memory. Keep it as a
    # sibling of the committed registry so `.betavibe/registry` can be synced
    # without timestamp-heavy usage logs and cross-machine merge conflicts.
    return registry.parent / "usage"


def resolver_log_path(registry: Path) -> Path:
    return usage_root(registry) / "resolver_events.jsonl"


def journal_log_path(registry: Path) -> Path:
    return usage_root(registry) / "journal.jsonl"


def append_jsonl(path: Path, event: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": now(), **event}, ensure_ascii=False) + "\n")


def log_resolver_event(registry: Path, *, phase: str, context: str, local_hits: list[dict], gbrain_hits: list[dict], harness: str | None = None) -> None:
    append_jsonl(resolver_log_path(registry), {
        "kind": "resolver",
        "phase": phase,
        "context": context,
        "harness": harness,
        "local_hits": len(local_hits),
        "gbrain_hits": len(gbrain_hits),
        "top_local": local_hits[:5],
        "top_gbrain": gbrain_hits[:5],
    })


def log_journal_event(registry: Path, *, miss: str | None = None, wrong_path: str | None = None, useful_hit: str | None = None, task: str | None = None, note: str | None = None) -> None:
    append_jsonl(journal_log_path(registry), {
        "kind": "journal",
        "task": task,
        "miss": miss,
        "wrong_path": wrong_path,
        "useful_hit": useful_hit,
        "note": note,
    })


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def summarize_usage(registry: Path) -> dict:
    resolver = read_jsonl(resolver_log_path(registry))
    journal = read_jsonl(journal_log_path(registry))
    runs = registry / "runs"
    run_summaries = []
    if runs.exists():
        for path in runs.iterdir():
            summary = path / "summary.json"
            if summary.exists():
                try:
                    run_summaries.append(json.loads(summary.read_text(encoding="utf-8")))
                except Exception:
                    pass
    pending = list((registry / "pending").glob("*.json")) if (registry / "pending").exists() else []
    insights = list((registry / "insights").rglob("INSIGHT.md")) if (registry / "insights").exists() else []
    personal_insights = list((personal_registry() / "insights").rglob("INSIGHT.md")) if (personal_registry() / "insights").exists() else []
    phases = Counter(e.get("phase", "unknown") for e in resolver)
    local_hit_events = sum(1 for e in resolver if int(e.get("local_hits") or 0) > 0)
    personal_hit_events = sum(1 for e in resolver if any(h.get("scope") == "personal" for h in e.get("top_local", [])))
    repo_hit_events = sum(1 for e in resolver if any(h.get("scope") == "repo" for h in e.get("top_local", [])))
    gbrain_hit_events = sum(1 for e in resolver if int(e.get("gbrain_hits") or 0) > 0)
    retrieval_counter: Counter[str] = Counter()
    for e in resolver:
        for h in e.get("top_local", []):
            key = h.get("slug")
            if not key:
                path = h.get("path") or ""
                parts = Path(path).parts if path else ()
                key = parts[-2] if len(parts) >= 2 and parts[-1] == "INSIGHT.md" else (h.get("title") or path)
            if key:
                retrieval_counter[str(key)] += 1
    high_conf = 0
    pass_only = 0
    failed_and_passed = 0
    for s in run_summaries:
        draft = s.get("draft", {})
        commands = draft.get("evidence", {}).get("commands", [])
        has_failed = any(not c.get("ok") for c in commands)
        has_passed = any(c.get("ok") for c in commands)
        if draft.get("confidence") == "high":
            high_conf += 1
        if has_passed and not has_failed:
            pass_only += 1
        if has_failed and has_passed:
            failed_and_passed += 1
    return {
        "resolver_calls": len(resolver),
        "resolver_phases": dict(phases),
        "resolver_local_hit_events": local_hit_events,
        "resolver_repo_hit_events": repo_hit_events,
        "resolver_personal_hit_events": personal_hit_events,
        "resolver_gbrain_hit_events": gbrain_hit_events,
        "per_insight_retrieval": retrieval_counter.most_common(10),
        "insights_recalled_more_than_once": sum(1 for _, count in retrieval_counter.items() if count > 1),
        "journal_entries": len(journal),
        "journal_misses": sum(1 for e in journal if e.get("miss")),
        "journal_wrong_paths": sum(1 for e in journal if e.get("wrong_path")),
        "journal_useful_hits": sum(1 for e in journal if e.get("useful_hit")),
        "runtime_runs": len(run_summaries),
        "runtime_high_confidence_runs": high_conf,
        "runtime_pass_only_runs": pass_only,
        "runtime_failed_and_passed_runs": failed_and_passed,
        "pending_candidates": len(pending),
        "reviewed_insights": len(insights),
        "personal_portable_insights": len(personal_insights),
    }


def format_metrics(summary: dict) -> str:
    lines = [
        "# Betavibe Metrics",
        "",
        f"- reviewed_insights: {summary['reviewed_insights']}",
        f"- pending_candidates: {summary['pending_candidates']}",
        f"- personal_portable_insights: {summary['personal_portable_insights']}",
        f"- resolver_calls: {summary['resolver_calls']}",
        f"- resolver_local_hit_events: {summary['resolver_local_hit_events']}",
        f"- resolver_repo_hit_events: {summary['resolver_repo_hit_events']}",
        f"- resolver_personal_hit_events: {summary['resolver_personal_hit_events']}",
        f"- resolver_gbrain_hit_events: {summary['resolver_gbrain_hit_events']}",
        f"- insights_recalled_more_than_once: {summary['insights_recalled_more_than_once']}",
        f"- journal_entries: {summary['journal_entries']}",
        f"- journal_misses: {summary['journal_misses']}",
        f"- journal_wrong_paths: {summary['journal_wrong_paths']}",
        f"- journal_useful_hits: {summary['journal_useful_hits']}",
        f"- runtime_runs: {summary['runtime_runs']}",
        f"- runtime_high_confidence_runs: {summary['runtime_high_confidence_runs']}",
        f"- runtime_pass_only_runs: {summary['runtime_pass_only_runs']}",
        f"- runtime_failed_and_passed_runs: {summary['runtime_failed_and_passed_runs']}",
        "",
        "## Resolver phases",
    ]
    for phase, count in sorted(summary.get("resolver_phases", {}).items()):
        lines.append(f"- {phase}: {count}")
    lines.extend(["", "## Top recalled insights"])
    for slug, count in summary.get("per_insight_retrieval", [])[:10]:
        lines.append(f"- {slug}: {count}")
    if not summary.get("per_insight_retrieval"):
        lines.append("- none yet")
    if summary["reviewed_insights"] < 20:
        lines.extend(["", "## Cold-start note", "- Registry has fewer than 20 reviewed insights; hit-rate metrics are noisy. Focus on journal_misses / wrong_paths to build the insight backlog.", "- During cold start, rely on GBrain plus ~/.betavibe/personal portable insights; consider `betavibe seed --from-personal --tags <stack>` to bootstrap repo-local memory."])
    return "\n".join(lines)
