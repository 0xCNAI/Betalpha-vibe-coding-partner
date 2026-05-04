---
{
  "title": "daily backup 2026-03-25",
  "type": "spec_guardrail",
  "tags": [
    "cron",
    "migration",
    "schema",
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `481a3b54943a`: daily backup 2026-03-25",
  "prevention_signal": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"481a3b54943a0cb6f40032bb343f0e9cc95df82c\",\n  \"files\": [\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/memory/corrections.md\",\n    \"betalpha-social/memory/errors.md\",\n    \"betalpha-social/memory/features.md\",\n    \"jonathan/MEMORY.md\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/archive/style_memory_full_20260324.md\",\n    \"jonathan/memory/corrections.md\",\n    \"jonathan/memory/features.md\",\n    \"jonathan/skills/betalpha-analytics/performance_data.md\",\n    \"jonathan/skills/daily-review/data/recommendations_2026-03-24.json\",\n    \"jonathan/skills/daily-review/data/recommendations_2026-03-24.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"research/AGENTS.md\",\n    \"research/config/qmd_memory_registry.json\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/feedback_compiler.json\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/memory/corrections.md, betalpha-social/memory/errors.md, betalpha-social/memory/features.md\",\n    \"large change set: 347 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron",
      "migration",
      "schema",
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
    "sha": "481a3b54943a0cb6f40032bb343f0e9cc95df82c",
    "date": "2026-03-25T03:00:45+08:00",
    "files": [
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/memory/corrections.md",
      "betalpha-social/memory/errors.md",
      "betalpha-social/memory/features.md",
      "jonathan/MEMORY.md",
      "jonathan/TOOLS.md",
      "jonathan/archive/style_memory_full_20260324.md",
      "jonathan/memory/corrections.md",
      "jonathan/memory/features.md",
      "jonathan/skills/betalpha-analytics/performance_data.md",
      "jonathan/skills/daily-review/data/recommendations_2026-03-24.json",
      "jonathan/skills/daily-review/data/recommendations_2026-03-24.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "research/AGENTS.md",
      "research/config/qmd_memory_registry.json",
      "research/data/corrections_tracker_state.json",
      "research/data/feedback_compiler.json",
      "research/data/feedback_compiler.md",
      "research/data/memory_curator_last.json",
      "research/data/pattern_placement.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/podcast_pipeline_state.json",
      "research/data/podcast_processed.json",
      "research/data/runtime/gateway_restart/launches/launch-20260324-210739-fb5ceb.json",
      "research/data/runtime/gateway_restart/launches/launch-20260324-211318-cf3992.json",
      "research/data/runtime/gateway_restart/launches/launch-20260324-213311-e39d96.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: daily backup 2026-03-25

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 481a3b54943a0cb6f40032bb343f0e9cc95df82c

## Evidence

{
  "commit": "481a3b54943a0cb6f40032bb343f0e9cc95df82c",
  "files": [
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/memory/corrections.md",
    "betalpha-social/memory/errors.md",
    "betalpha-social/memory/features.md",
    "jonathan/MEMORY.md",
    "jonathan/TOOLS.md",
    "jonathan/archive/style_memory_full_20260324.md",
    "jonathan/memory/corrections.md",
    "jonathan/memory/features.md",
    "jonathan/skills/betalpha-analytics/performance_data.md",
    "jonathan/skills/daily-review/data/recommendations_2026-03-24.json",
    "jonathan/skills/daily-review/data/recommendations_2026-03-24.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "research/AGENTS.md",
    "research/config/qmd_memory_registry.json",
    "research/data/corrections_tracker_state.json",
    "research/data/feedback_compiler.json"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/memory/corrections.md, betalpha-social/memory/errors.md, betalpha-social/memory/features.md",
    "large change set: 347 files"
  ]
}
