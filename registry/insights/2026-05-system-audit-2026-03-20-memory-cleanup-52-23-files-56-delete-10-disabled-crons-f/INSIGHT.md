---
{
  "title": "system audit 2026-03-20: memory cleanup (52→23 files, -56%), delete 10 disabled crons, fix",
  "type": "pitfall",
  "tags": [
    "cron"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `2c74c2077eee`: system audit 2026-03-20: memory cleanup (52→23 files, -56%), delete 10 disabled crons, fix timeouts, update MEMORY.md cron table, delete deprecated self-optimize skill, merge Jonathan duplicate crons, downgrade flash-coverage-review to gpt-5.4",
  "prevention_signal": "Before modifying `research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"2c74c2077eee3c6b29e270f7d17dc2697ac0b9f9\",\n  \"files\": [\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"publish/HEARTBEAT.md\",\n    \"publish/drafts/hegic-treasury-governance.md\",\n    \"publish/handoffs/hegic-treasury-governance.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_placement.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/rule_verdicts.jsonl\",\n    \"research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json\",\n    \"research/feedback/autoresearch_log/flash-writer_2026-03-20_2511.json\",\n    \"research/feedback/autoresearch_log/flash-writer_2026-03-20_2512.json\",\n    \"research/feedback/flash_coverage_feedback.jsonl\",\n    \"research/feedback/flash_coverage_stats.jsonl\",\n    \"research/feedback/heartbeat_inbox.jsonl\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json, research/feedback/autoresearch_log/flash-writer_2026-03-20_2511.json, research/feedback/autoresearch_log/flash-writer_2026-03-20_2512.json, research/feedback/flash_coverage_feedback.jsonl\",\n    \"large change set: 73 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "2c74c2077eee3c6b29e270f7d17dc2697ac0b9f9",
    "date": "2026-03-20T11:57:47+08:00",
    "files": [
      "jonathan/data/daily_kol_digest.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "publish/HEARTBEAT.md",
      "publish/drafts/hegic-treasury-governance.md",
      "publish/handoffs/hegic-treasury-governance.md",
      "research-agent/reviewer-learnings.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_placement.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/rule_verdicts.jsonl",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2511.json",
      "research/feedback/autoresearch_log/flash-writer_2026-03-20_2512.json",
      "research/feedback/flash_coverage_feedback.jsonl",
      "research/feedback/flash_coverage_stats.jsonl",
      "research/feedback/heartbeat_inbox.jsonl",
      "research/memory/2025-05-07.md",
      "research/memory/2026-01-28.md",
      "research/memory/2026-01-29.md",
      "research/memory/2026-01-30.md",
      "research/memory/2026-02-01.md",
      "research/memory/2026-02-03.md",
      "research/memory/2026-02-04.md",
      "research/memory/2026-02-05.md",
      "research/memory/2026-02-07.md",
      "research/memory/2026-02-09.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: system audit 2026-03-20: memory cleanup (52→23 files, -56%), delete 10 disabled crons, fix timeouts, update MEMORY.md cron table, delete deprecated self-optimize skill, merge Jonathan duplicate crons, downgrade flash-coverage-review to gpt-5.4

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 2c74c2077eee3c6b29e270f7d17dc2697ac0b9f9

## Evidence

{
  "commit": "2c74c2077eee3c6b29e270f7d17dc2697ac0b9f9",
  "files": [
    "jonathan/data/daily_kol_digest.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "publish/HEARTBEAT.md",
    "publish/drafts/hegic-treasury-governance.md",
    "publish/handoffs/hegic-treasury-governance.md",
    "research-agent/reviewer-learnings.md",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_placement.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/data/rule_verdicts.jsonl",
    "research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json",
    "research/feedback/autoresearch_log/flash-writer_2026-03-20_2511.json",
    "research/feedback/autoresearch_log/flash-writer_2026-03-20_2512.json",
    "research/feedback/flash_coverage_feedback.jsonl",
    "research/feedback/flash_coverage_stats.jsonl",
    "research/feedback/heartbeat_inbox.jsonl"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: research/feedback/autoresearch_log/flash-writer_2026-03-20_2510.json, research/feedback/autoresearch_log/flash-writer_2026-03-20_2511.json, research/feedback/autoresearch_log/flash-writer_2026-03-20_2512.json, research/feedback/flash_coverage_feedback.jsonl",
    "large change set: 73 files"
  ]
}
