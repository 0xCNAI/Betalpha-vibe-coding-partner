"""Resolver quality regression tests after phase_terms removal + min-score gate."""
from __future__ import annotations

import os
import subprocess
from datetime import date
from pathlib import Path

from betavibe.models import Insight
from betavibe.registry import init_registry, write_insight

REPO = Path(__file__).resolve().parent.parent


def run_resolve(phase: str, context: str, registry: Path, extra: list[str] | None = None) -> str:
    personal = registry.parent / "personal"
    personal.mkdir(parents=True, exist_ok=True)
    cmd = [
        "python3",
        "-m",
        "betavibe",
        "--registry",
        str(registry),
        "resolve",
        phase,
        "--context",
        context,
        "--no-gbrain",
        "--limit",
        "5",
    ] + (extra or [])
    env = {**os.environ, "BETAVIBE_PERSONAL_REGISTRY": str(personal)}
    r = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True, text=True, check=True)
    return r.stdout


def test_empty_context_returns_no_hits(tmp_path):
    """Empty context should not synthesize bogus hits from phase_terms."""
    registry = _seed_minimal_registry(tmp_path)
    out = run_resolve("pre_implement", "", registry)
    assert "No matching local reviewed insights" in out or "No reviewed local guardrail" in out


def test_unrelated_query_filtered_by_min_score(tmp_path):
    """A clearly unrelated query should be filtered by the min-score gate."""
    registry = _seed_minimal_registry(tmp_path)
    out = run_resolve("pre_implement", "Stripe payment webhook signature verification", registry)
    assert "No reviewed local guardrail" in out or "Relevant local reviewed insights: 0" in out


def test_relevant_query_finds_hit(tmp_path):
    """A paraphrased on-topic query should still find its insight."""
    registry = _seed_minimal_registry(tmp_path)
    out = run_resolve("pre_implement", "LINE bot stops replying in group chats", registry)
    assert "resolveLineAccount" in out or "group-source guard" in out


def test_min_score_zero_disables_gate(tmp_path):
    """--min-score 0 should restore old behavior (no gate)."""
    registry = _seed_minimal_registry(tmp_path)
    out = run_resolve("pre_implement", "Stripe payment webhook", registry, ["--min-score", "0"])
    assert "Relevant local reviewed insights" in out


def _seed_minimal_registry(tmp_path: Path) -> Path:
    """Write 3 minimal insights to a fresh registry for these tests."""
    registry = tmp_path / "registry"
    init_registry(registry)
    today = date.today().isoformat()
    seeds = [
        Insight(
            title="LINE group-source guard preserves resolveLineAccount replies",
            type="pitfall",
            tags=["line", "bot", "group", "reply"],
            tech_stack=["typescript", "openclaw"],
            summary="LINE group chats stopped replying when account resolution skipped the group-source guard and chose the wrong account binding.",
            prevention_signal="Before changing LINE reply routing, verify resolveLineAccount keeps the group-source guard for group chats.",
            verify_trigger="When LINE account routing, group chat source parsing, or reply delivery changes.",
            created_at=today,
            last_verified_at=today,
            body={
                "symptom": "LINE bot stops replying in group chats after routing changes.",
                "root_cause": "The group-source guard was bypassed before resolveLineAccount selected the delivery account.",
                "fix": "Keep the group-source guard and test group chat reply routing end to end.",
                "wrong_paths": "Only testing one-to-one LINE DMs misses group-source routing regressions.",
            },
        ),
        Insight(
            title="Discord thread bindings must persist across restart",
            type="pitfall",
            tags=["discord", "threads", "persistence", "restart"],
            tech_stack=["node", "openclaw"],
            summary="Discord conversations were lost after restart because thread binding state was kept only in process memory.",
            prevention_signal="Before changing Discord conversation routing, persist and reload thread bindings across process restart.",
            verify_trigger="When Discord thread binding, session routing, or restart recovery changes.",
            created_at=today,
            last_verified_at=today,
            body={
                "symptom": "Discord bot lost all conversations after restart.",
                "root_cause": "Thread bindings were not persisted before shutdown and were unavailable on boot.",
                "fix": "Store thread bindings durably and smoke test restart recovery.",
            },
        ),
        Insight(
            title="Cron OAuth jobs need explicit launch environment",
            type="pattern",
            tags=["cron", "oauth", "launchd", "environment"],
            tech_stack=["python", "macos"],
            summary="Cron and launchd jobs failed OAuth-backed commands when PATH and credential environment differed from the interactive shell.",
            prevention_signal="Before adding OAuth cron jobs, set the launch environment explicitly and run a cron-style smoke test.",
            verify_trigger="When cron, launchd, OAuth credentials, or command PATH handling changes.",
            created_at=today,
            last_verified_at=today,
            body={
                "pattern": "Treat cron and launchd as a separate runtime with explicit PATH and credentials.",
                "fix": "Inject the required PATH and OAuth environment, then run an env-clean smoke test.",
            },
        ),
    ]
    for insight in seeds:
        write_insight(insight, registry)
    return registry
