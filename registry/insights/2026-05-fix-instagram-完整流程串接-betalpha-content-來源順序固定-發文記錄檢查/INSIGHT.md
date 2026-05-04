---
{
  "title": "fix: /instagram 完整流程串接 + betalpha-content 來源順序固定 + 發文記錄檢查",
  "type": "pitfall",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `ebea6f58d82b`: fix: /instagram 完整流程串接 + betalpha-content 來源順序固定 + 發文記錄檢查",
  "prevention_signal": "Before modifying `research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"ebea6f58d82bd3660a86c258fecaa86d76e717ad\",\n  \"files\": [\n    \"jonathan/AGENTS.md\",\n    \"jonathan/skills/betalpha-content/SKILL.md\",\n    \"research/data/runtime/autopilot/active_work.json\",\n    \"research/data/runtime/autopilot/build_manifest.json\",\n    \"research/data/runtime/autopilot/context_budget_view.json\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T151741+0800.json\",\n    \"research/data/runtime/autopilot/heartbeat/20260330T151741+0800.md\",\n    \"research/data/runtime/autopilot/heartbeat/latest.json\",\n    \"research/data/runtime/autopilot/heartbeat/latest.md\",\n    \"research/data/runtime/autopilot/pipeline_state_view.json\",\n    \"research/data/runtime/autopilot/source_health.json\",\n    \"research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.json\",\n    \"research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.md\",\n    \"research/data/runtime/autopilot/trial_scoreboard/latest.json\",\n    \"research/data/runtime/autopilot/trial_scoreboard/latest.md\",\n    \"research/data/runtime/pipelines/alpha-distil/pool/pool_events.jsonl\",\n    \"research/data/runtime/pipelines/alpha-distil/pool/pool_snapshot.json\",\n    \"research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json\",\n    \"research/data/runtime/pipelines/alpha-distil/review/review_decision_latest.json\",\n    \"research/data/runtime/qmd_maintenance/lock\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json, research/data/runtime/pipelines/alpha-distil/review/review_decision_latest.json\",\n    \"large change set: 23 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "test"
    ],
    "tech_stack": [
      "python"
    ],
    "source_kind": "git_commit"
  },
  "tech_versions_last_seen": {},
  "created_at": "2026-05-04",
  "last_verified_at": "2026-05-04",
  "source": {
    "kind": "git_commit",
    "repo": "/Users/betalpha/clawd",
    "sha": "ebea6f58d82bd3660a86c258fecaa86d76e717ad",
    "date": "2026-03-30T15:19:17+08:00",
    "files": [
      "jonathan/AGENTS.md",
      "jonathan/skills/betalpha-content/SKILL.md",
      "research/data/runtime/autopilot/active_work.json",
      "research/data/runtime/autopilot/build_manifest.json",
      "research/data/runtime/autopilot/context_budget_view.json",
      "research/data/runtime/autopilot/heartbeat/20260330T151741+0800.json",
      "research/data/runtime/autopilot/heartbeat/20260330T151741+0800.md",
      "research/data/runtime/autopilot/heartbeat/latest.json",
      "research/data/runtime/autopilot/heartbeat/latest.md",
      "research/data/runtime/autopilot/pipeline_state_view.json",
      "research/data/runtime/autopilot/source_health.json",
      "research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.json",
      "research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.md",
      "research/data/runtime/autopilot/trial_scoreboard/latest.json",
      "research/data/runtime/autopilot/trial_scoreboard/latest.md",
      "research/data/runtime/pipelines/alpha-distil/pool/pool_events.jsonl",
      "research/data/runtime/pipelines/alpha-distil/pool/pool_snapshot.json",
      "research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json",
      "research/data/runtime/pipelines/alpha-distil/review/review_decision_latest.json",
      "research/data/runtime/qmd_maintenance/lock",
      "research/data/scorecards/alpha-distil.json",
      "research/tests/test_insight_stable_source.py",
      "research/vault/meta/data/tweet_tracker.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: /instagram 完整流程串接 + betalpha-content 來源順序固定 + 發文記錄檢查

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch ebea6f58d82bd3660a86c258fecaa86d76e717ad

## Evidence

{
  "commit": "ebea6f58d82bd3660a86c258fecaa86d76e717ad",
  "files": [
    "jonathan/AGENTS.md",
    "jonathan/skills/betalpha-content/SKILL.md",
    "research/data/runtime/autopilot/active_work.json",
    "research/data/runtime/autopilot/build_manifest.json",
    "research/data/runtime/autopilot/context_budget_view.json",
    "research/data/runtime/autopilot/heartbeat/20260330T151741+0800.json",
    "research/data/runtime/autopilot/heartbeat/20260330T151741+0800.md",
    "research/data/runtime/autopilot/heartbeat/latest.json",
    "research/data/runtime/autopilot/heartbeat/latest.md",
    "research/data/runtime/autopilot/pipeline_state_view.json",
    "research/data/runtime/autopilot/source_health.json",
    "research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.json",
    "research/data/runtime/autopilot/trial_scoreboard/20260330T151741+0800.md",
    "research/data/runtime/autopilot/trial_scoreboard/latest.json",
    "research/data/runtime/autopilot/trial_scoreboard/latest.md",
    "research/data/runtime/pipelines/alpha-distil/pool/pool_events.jsonl",
    "research/data/runtime/pipelines/alpha-distil/pool/pool_snapshot.json",
    "research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json",
    "research/data/runtime/pipelines/alpha-distil/review/review_decision_latest.json",
    "research/data/runtime/qmd_maintenance/lock"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: research/data/runtime/pipelines/alpha-distil/publish/feedback_record_latest.json, research/data/runtime/pipelines/alpha-distil/review/review_decision_latest.json",
    "large change set: 23 files"
  ]
}
