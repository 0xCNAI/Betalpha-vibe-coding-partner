---
{
  "title": "daily backup 2026-03-22",
  "type": "spec_guardrail",
  "tags": [
    "cron"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `ca6d11ff05f2`: daily backup 2026-03-22",
  "prevention_signal": "Before modifying `betalpha-social/memory/2026-03-21.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"ca6d11ff05f2f75e4951982e5fa301bcf489041f\",\n  \"files\": [\n    \"betalpha-social/memory/2026-03-21.md\",\n    \"\\\"betalpha-social/threads/260321_Aave_Morpho_\\\\346\\\\262\\\\273\\\\347\\\\220\\\\206\\\\345\\\\233\\\\260\\\\345\\\\242\\\\203_thread.md\\\"\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"research/data/pattern_placement.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/podcast_pipeline_state.json\",\n    \"research/data/training/inputs/flash_2026-03-21_13.json\",\n    \"research/data/training/inputs/flash_2026-03-21_14.json\",\n    \"research/data/training/inputs/flash_2026-03-21_15.json\",\n    \"research/data/training/inputs/flash_2026-03-21_16.json\",\n    \"research/data/training/inputs/flash_2026-03-21_17.json\",\n    \"research/data/training/inputs/flash_2026-03-21_18.json\",\n    \"research/data/training/inputs/flash_2026-03-21_19.json\",\n    \"research/data/training/inputs/flash_2026-03-21_20.json\",\n    \"research/data/training/inputs/flash_2026-03-21_21.json\",\n    \"research/data/training/inputs/flash_2026-03-21_22.json\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/memory/2026-03-21.md, \\\"betalpha-social/threads/260321_Aave_Morpho_\\\\346\\\\262\\\\273\\\\347\\\\220\\\\206\\\\345\\\\233\\\\260\\\\345\\\\242\\\\203_thread.md\\\", research/feedback/flash_coverage_feedback.jsonl, research/feedback/flash_coverage_stats.jsonl\",\n    \"large change set: 45 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/memory/2026-03-21.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron"
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
    "sha": "ca6d11ff05f2f75e4951982e5fa301bcf489041f",
    "date": "2026-03-22T03:00:10+08:00",
    "files": [
      "betalpha-social/memory/2026-03-21.md",
      "\"betalpha-social/threads/260321_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203_thread.md\"",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "research/data/pattern_placement.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/podcast_pipeline_state.json",
      "research/data/training/inputs/flash_2026-03-21_13.json",
      "research/data/training/inputs/flash_2026-03-21_14.json",
      "research/data/training/inputs/flash_2026-03-21_15.json",
      "research/data/training/inputs/flash_2026-03-21_16.json",
      "research/data/training/inputs/flash_2026-03-21_17.json",
      "research/data/training/inputs/flash_2026-03-21_18.json",
      "research/data/training/inputs/flash_2026-03-21_19.json",
      "research/data/training/inputs/flash_2026-03-21_20.json",
      "research/data/training/inputs/flash_2026-03-21_21.json",
      "research/data/training/inputs/flash_2026-03-21_22.json",
      "research/data/training/inputs/flash_2026-03-21_23.json",
      "research/data/training/inputs/portfolio_2026-03-21_12.json",
      "research/data/training/inputs/portfolio_2026-03-21_13.json",
      "research/data/training/inputs/portfolio_2026-03-21_14.json",
      "research/data/training/inputs/portfolio_2026-03-21_15.json",
      "research/data/training/inputs/portfolio_2026-03-21_16.json",
      "research/data/training/inputs/portfolio_2026-03-21_17.json",
      "research/data/training/inputs/portfolio_2026-03-21_18.json",
      "research/data/training/inputs/portfolio_2026-03-21_19.json",
      "research/data/training/inputs/portfolio_2026-03-21_20.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: daily backup 2026-03-22

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch ca6d11ff05f2f75e4951982e5fa301bcf489041f

## Evidence

{
  "commit": "ca6d11ff05f2f75e4951982e5fa301bcf489041f",
  "files": [
    "betalpha-social/memory/2026-03-21.md",
    "\"betalpha-social/threads/260321_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203_thread.md\"",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "research/data/pattern_placement.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/data/podcast_pipeline_state.json",
    "research/data/training/inputs/flash_2026-03-21_13.json",
    "research/data/training/inputs/flash_2026-03-21_14.json",
    "research/data/training/inputs/flash_2026-03-21_15.json",
    "research/data/training/inputs/flash_2026-03-21_16.json",
    "research/data/training/inputs/flash_2026-03-21_17.json",
    "research/data/training/inputs/flash_2026-03-21_18.json",
    "research/data/training/inputs/flash_2026-03-21_19.json",
    "research/data/training/inputs/flash_2026-03-21_20.json",
    "research/data/training/inputs/flash_2026-03-21_21.json",
    "research/data/training/inputs/flash_2026-03-21_22.json"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/memory/2026-03-21.md, \"betalpha-social/threads/260321_Aave_Morpho_\\346\\262\\273\\347\\220\\206\\345\\233\\260\\345\\242\\203_thread.md\", research/feedback/flash_coverage_feedback.jsonl, research/feedback/flash_coverage_stats.jsonl",
    "large change set: 45 files"
  ]
}
