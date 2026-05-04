from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import math
from pathlib import Path
import json
import statistics
import time

from .gitmine import mine_git
from .models import Insight
from .registry import list_scoped_insights
from .search import hybrid_search_insights, search_insights, tokenize


PHASE_TERMS = {
    "pre_spec": "spec guardrail decision pattern tool choice architecture migration integration",
    "pre_implement": "pitfall wrong paths fix implementation test deploy config migration",
}

STOPWORDS = {
    "add", "and", "the", "for", "from", "with", "this", "that", "into", "fix",
    "fixed", "bug", "regression", "failure", "failed", "test", "tests", "update",
    "phase", "codex", "agent", "agents", "skill", "skills", "file", "files",
    "before", "modifying", "adjacent", "subsystem", "search", "registry",
    "inspect", "original", "fixing", "commit", "similar", "work", "related",
}

NULL_CONTROL_TOPICS = [
    "Plan a watercolor workshop signup sheet for a community art class.",
    "Choose a dinner menu for a family picnic with seasonal fruit.",
    "Draft a packing checklist for a weekend mountain photography trip.",
    "Compare ergonomic desk chair colors for a home office refresh.",
    "Create a reading list for historical fiction set near the ocean.",
    "Design a chess study schedule for beginner endgame practice.",
    "Outline a birthday party playlist for acoustic guitar songs.",
    "Prepare a houseplant watering calendar for succulents and ferns.",
]


@dataclass
class BenchResult:
    report: dict
    path: Path


def _topic_tokens(text: str) -> set[str]:
    return {tok for tok in tokenize(text) if len(tok) >= 4 and tok not in STOPWORDS}


def _overlap_score(left: str, right: str) -> dict:
    left_tokens = _topic_tokens(left)
    right_tokens = _topic_tokens(right)
    overlap = sorted(left_tokens.intersection(right_tokens))
    if not left_tokens or not right_tokens:
        return {"score": 0.0, "overlap": overlap, "left_count": len(left_tokens), "right_count": len(right_tokens)}
    # Use the smaller side as denominator so concise prevention signals can
    # match long pitfall descriptions without requiring noisy whole-doc overlap.
    score = len(overlap) / min(len(left_tokens), len(right_tokens))
    return {"score": score, "overlap": overlap, "left_count": len(left_tokens), "right_count": len(right_tokens)}


def _case_from_candidate(candidate: dict) -> dict:
    source = candidate.get("source", {})
    files = list(source.get("files") or [])
    draft = candidate.get("draft", {})
    title = candidate.get("title", "")
    tags = list(candidate.get("tags") or [])
    tech_stack = list(candidate.get("tech_stack") or [])
    task_description = "\n".join([
        f"Fix commit: {title}",
        f"Summary: {candidate.get('summary', '')}",
        f"Touched files: {', '.join(files[:12])}",
        f"Tags: {', '.join(tags)}",
        f"Tech: {', '.join(tech_stack)}",
    ]).strip()
    actual_pitfall = "\n".join([
        title,
        candidate.get("summary", ""),
        draft.get("symptom", ""),
        draft.get("root_cause", ""),
        draft.get("prevention_signal", ""),
        " ".join(tags),
        " ".join(tech_stack),
        " ".join(files[:12]),
    ]).strip()
    return {
        "id": candidate["id"],
        "source": source,
        "task_description": task_description,
        "actual_pitfall": actual_pitfall,
        "tags": tags,
        "tech_stack": tech_stack,
        "title": title,
        "is_null_control": False,
    }


def _null_control_cases(real_count: int) -> list[dict]:
    count = max(1, math.ceil(real_count * 0.10))
    cases = []
    for idx in range(count):
        topic = NULL_CONTROL_TOPICS[idx % len(NULL_CONTROL_TOPICS)]
        cases.append({
            "id": f"null-control-{idx + 1:02d}",
            "source": {"kind": "synthetic_null_control"},
            "task_description": topic,
            "actual_pitfall": topic,
            "tags": ["null-control"],
            "tech_stack": [],
            "title": topic,
            "is_null_control": True,
        })
    return cases


def _hit_text(insight: Insight) -> str:
    return "\n".join([
        insight.title,
        insight.summary,
        insight.prevention_signal,
        " ".join(insight.tags),
        " ".join(insight.tech_stack),
        "\n".join(str(v) for v in insight.body.values()),
    ])


def _classify(case: dict, hits: list[tuple[float, Insight, list[str]]]) -> tuple[str, dict | None]:
    is_null_control = bool(case.get("is_null_control"))
    if not case.get("actual_pitfall"):
        return "null", None
    if not hits:
        return "null" if is_null_control else "miss", None

    best = None
    for score, insight, matched in hits:
        overlap = _overlap_score(insight.prevention_signal, case.get("actual_pitfall", ""))
        relevant = overlap["score"] >= 0.15 and len(overlap["overlap"]) >= 2
        row = {
            "score": score,
            "slug": insight.slug,
            "title": insight.title,
            "matched": matched,
            "prevention_signal": insight.prevention_signal,
            "overlap_score": overlap["score"],
            "overlap_tokens": overlap["overlap"][:12],
            "relevant": relevant,
            "path": str(insight.path) if insight.path else None,
        }
        if best is None:
            best = row
        if relevant:
            return "hit", row
    return "false_positive" if is_null_control else "miss", best


def _rates(outcomes: list[str]) -> dict:
    total = max(len(outcomes), 1)
    counts = {name: outcomes.count(name) for name in ["hit", "miss", "false_positive", "null"]}
    return {
        "total": len(outcomes),
        **{f"{name}_count": count for name, count in counts.items()},
        **{f"{name}_rate": count / total for name, count in counts.items()},
    }


def _latency_summary(values: list[float]) -> dict:
    if not values:
        return {"count": 0, "avg_ms": 0.0, "p50_ms": 0.0, "p95_ms": 0.0, "max_ms": 0.0}
    ordered = sorted(values)
    p95_index = min(len(ordered) - 1, int(round((len(ordered) - 1) * 0.95)))
    return {
        "count": len(values),
        "avg_ms": statistics.fmean(values),
        "p50_ms": statistics.median(values),
        "p95_ms": ordered[p95_index],
        "max_ms": max(values),
    }


def run_bench(
    repo: Path,
    registry: Path,
    since: str,
    out: Path,
    max_commits: int = 500,
    min_cases: int = 30,
    limit: int = 5,
    include_personal: bool = True,
    search_mode: str = "lexical",
) -> BenchResult:
    repo = repo.expanduser().resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"not a git repository: {repo}")

    candidates = mine_git(repo, since=since, max_commits=max_commits, with_github=False)
    real_cases = [_case_from_candidate(c) for c in candidates]
    if len(real_cases) < min_cases:
        raise SystemExit(f"bench requires at least {min_cases} mined fix cases; found {len(real_cases)} from {repo} since {since!r}")
    cases = real_cases + _null_control_cases(len(real_cases))

    insights = list_scoped_insights(registry, include_personal=include_personal)
    phase_rows: dict[str, list[dict]] = {phase: [] for phase in PHASE_TERMS}
    phase_outcomes: dict[str, list[str]] = {phase: [] for phase in PHASE_TERMS}
    phase_latencies: dict[str, list[float]] = {phase: [] for phase in PHASE_TERMS}

    for case in cases:
        for phase, terms in PHASE_TERMS.items():
            query = f"{case['task_description']}\n{terms}"
            started = time.perf_counter()
            if search_mode == "hybrid":
                hits = hybrid_search_insights(registry, insights, query, limit=limit)
            else:
                hits = search_insights(insights, query, limit=limit)
            latency_ms = (time.perf_counter() - started) * 1000
            outcome, top_hit = _classify(case, hits)
            phase_outcomes[phase].append(outcome)
            phase_latencies[phase].append(latency_ms)
            phase_rows[phase].append({
                "case_id": case["id"],
                "source": case["source"],
                "task_description": case["task_description"],
                "actual_pitfall": case["actual_pitfall"],
                "outcome": outcome,
                "latency_ms": latency_ms,
                "top_hit": top_hit,
            })

    all_outcomes = [outcome for outcomes in phase_outcomes.values() for outcome in outcomes]
    all_latencies = [latency for latencies in phase_latencies.values() for latency in latencies]
    real_outcomes = []
    null_control_outcomes = []
    for rows in phase_rows.values():
        for row in rows:
            if row["source"].get("kind") == "synthetic_null_control":
                null_control_outcomes.append(row["outcome"])
            else:
                real_outcomes.append(row["outcome"])
    metrics = {
        "overall": {**_rates(all_outcomes), "latency": _latency_summary(all_latencies)},
        "real_cases": _rates(real_outcomes),
        "null_controls": _rates(null_control_outcomes),
        "phases": {
            phase: {**_rates(phase_outcomes[phase]), "latency": _latency_summary(phase_latencies[phase])}
            for phase in PHASE_TERMS
        },
    }
    report = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repo": str(repo),
        "registry": str(registry),
        "since": since,
        "max_commits": max_commits,
        "min_cases": min_cases,
        "case_count": len(real_cases),
        "null_control_count": len(cases) - len(real_cases),
        "reviewed_insight_count": len(insights),
        "search_mode": search_mode,
        "metrics": metrics,
        "cases": cases,
        "phase_results": phase_rows,
    }

    out = out.expanduser()
    if not out.is_absolute():
        out = (Path.cwd() / out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return BenchResult(report=report, path=out)
