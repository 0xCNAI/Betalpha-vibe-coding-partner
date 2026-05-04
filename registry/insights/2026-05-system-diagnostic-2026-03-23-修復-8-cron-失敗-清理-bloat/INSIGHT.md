---
{
  "title": "system-diagnostic: 2026-03-23 - 修復 8 cron 失敗 + 清理 bloat",
  "type": "spec_guardrail",
  "tags": [
    "cron",
    "schema"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `413b1725424a`: system-diagnostic: 2026-03-23 - 修復 8 cron 失敗 + 清理 bloat",
  "prevention_signal": "Before modifying `MD_SCHEMA.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"413b1725424aa4c6540e0c0adb73459ebdbe0c82\",\n  \"files\": [\n    \"MD_SCHEMA.md\",\n    \"betalpha-social/Automation_case\",\n    \"\\\"betalpha-social/threads/260323_Morpho\\\\345\\\\243\\\\236\\\\345\\\\270\\\\263_thread.md\\\"\",\n    \"\\\"betalpha-social/threads/260323_\\\\345\\\\205\\\\250\\\\347\\\\220\\\\203\\\\350\\\\263\\\\207\\\\347\\\\224\\\\242\\\\346\\\\232\\\\264\\\\350\\\\267\\\\214_thread.md\\\"\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"publish/TOOLS.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/HEARTBEAT.md\",\n    \"research-agent/data/reviewer-learnings.md\",\n    \"research/.clawhub/lock.json\",\n    \"research/AGENTS.md\",\n    \"research/SOUL.md\",\n    \"research/USER.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_placement.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pending_rule_proposals.jsonl\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: MD_SCHEMA.md, betalpha-social/Automation_case, \\\"betalpha-social/threads/260323_Morpho\\\\345\\\\243\\\\236\\\\345\\\\270\\\\263_thread.md\\\", \\\"betalpha-social/threads/260323_\\\\345\\\\205\\\\250\\\\347\\\\220\\\\203\\\\350\\\\263\\\\207\\\\347\\\\224\\\\242\\\\346\\\\232\\\\264\\\\350\\\\267\\\\214_thread.md\\\"\",\n    \"large change set: 84 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `MD_SCHEMA.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron",
      "schema"
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
    "sha": "413b1725424aa4c6540e0c0adb73459ebdbe0c82",
    "date": "2026-03-23T22:08:10+08:00",
    "files": [
      "MD_SCHEMA.md",
      "betalpha-social/Automation_case",
      "\"betalpha-social/threads/260323_Morpho\\345\\243\\236\\345\\270\\263_thread.md\"",
      "\"betalpha-social/threads/260323_\\345\\205\\250\\347\\220\\203\\350\\263\\207\\347\\224\\242\\346\\232\\264\\350\\267\\214_thread.md\"",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "publish/TOOLS.md",
      "research-agent/AGENTS.md",
      "research-agent/HEARTBEAT.md",
      "research-agent/data/reviewer-learnings.md",
      "research/.clawhub/lock.json",
      "research/AGENTS.md",
      "research/SOUL.md",
      "research/USER.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_placement.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pending_rule_proposals.jsonl",
      "research/data/pipeline_events.jsonl",
      "research/data/rule_verdicts.jsonl",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-03-23_10.json",
      "research/data/training/inputs/flash_2026-03-23_11.json",
      "research/data/training/inputs/flash_2026-03-23_12.json",
      "research/data/training/inputs/flash_2026-03-23_13.json",
      "research/data/training/inputs/flash_2026-03-23_14.json",
      "research/data/training/inputs/flash_2026-03-23_15.json",
      "research/data/training/inputs/flash_2026-03-23_16.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: system-diagnostic: 2026-03-23 - 修復 8 cron 失敗 + 清理 bloat

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 413b1725424aa4c6540e0c0adb73459ebdbe0c82

## Evidence

{
  "commit": "413b1725424aa4c6540e0c0adb73459ebdbe0c82",
  "files": [
    "MD_SCHEMA.md",
    "betalpha-social/Automation_case",
    "\"betalpha-social/threads/260323_Morpho\\345\\243\\236\\345\\270\\263_thread.md\"",
    "\"betalpha-social/threads/260323_\\345\\205\\250\\347\\220\\203\\350\\263\\207\\347\\224\\242\\346\\232\\264\\350\\267\\214_thread.md\"",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "publish/TOOLS.md",
    "research-agent/AGENTS.md",
    "research-agent/HEARTBEAT.md",
    "research-agent/data/reviewer-learnings.md",
    "research/.clawhub/lock.json",
    "research/AGENTS.md",
    "research/SOUL.md",
    "research/USER.md",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_placement.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pending_rule_proposals.jsonl"
  ],
  "reasons": [
    "touches risky subsystem: MD_SCHEMA.md, betalpha-social/Automation_case, \"betalpha-social/threads/260323_Morpho\\345\\243\\236\\345\\270\\263_thread.md\", \"betalpha-social/threads/260323_\\345\\205\\250\\347\\220\\203\\350\\263\\207\\347\\224\\242\\346\\232\\264\\350\\267\\214_thread.md\"",
    "large change set: 84 files"
  ]
}
