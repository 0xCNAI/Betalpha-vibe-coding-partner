---
{
  "title": "system-diagnostic: 2026-03-22 - 修復 2 個 cron timeout (300s→600s)",
  "type": "pitfall",
  "tags": [
    "cron"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `47407a010544`: system-diagnostic: 2026-03-22 - 修復 2 個 cron timeout (300s→600s)",
  "prevention_signal": "Before modifying `research/feedback/flash_coverage_feedback.jsonl` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"47407a0105441e3a4710b28decdf45f409fdf338\",\n  \"files\": [\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/rule_change_log.jsonl\",\n    \"research/data/training/flash-news.jsonl\",\n    \"research/data/training/inputs/flash_2026-03-22_17.json\",\n    \"research/data/training/inputs/flash_2026-03-22_18.json\",\n    \"research/data/training/inputs/flash_2026-03-22_19.json\",\n    \"research/data/training/inputs/flash_2026-03-22_20.json\",\n    \"research/data/training/inputs/flash_2026-03-22_21.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_17.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_18.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_19.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_20.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_21.json\",\n    \"research/feedback/flash_coverage_feedback.jsonl\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: research/feedback/flash_coverage_feedback.jsonl, research/feedback/flash_coverage_stats.jsonl, research/scripts/feedback_weekly_digest.py, research/skills/portfolio-alpha/data/feedback_log.jsonl\",\n    \"large change set: 30 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/feedback/flash_coverage_feedback.jsonl` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "47407a0105441e3a4710b28decdf45f409fdf338",
    "date": "2026-03-22T22:05:56+08:00",
    "files": [
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/rule_change_log.jsonl",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-03-22_17.json",
      "research/data/training/inputs/flash_2026-03-22_18.json",
      "research/data/training/inputs/flash_2026-03-22_19.json",
      "research/data/training/inputs/flash_2026-03-22_20.json",
      "research/data/training/inputs/flash_2026-03-22_21.json",
      "research/data/training/inputs/portfolio_2026-03-22_17.json",
      "research/data/training/inputs/portfolio_2026-03-22_18.json",
      "research/data/training/inputs/portfolio_2026-03-22_19.json",
      "research/data/training/inputs/portfolio_2026-03-22_20.json",
      "research/data/training/inputs/portfolio_2026-03-22_21.json",
      "research/feedback/flash_coverage_feedback.jsonl",
      "research/feedback/flash_coverage_stats.jsonl",
      "research/memory/corrections.md",
      "research/scripts/feedback_weekly_digest.py",
      "research/scripts/weekly_scorecard.py",
      "research/skills/discord-channels/SKILL.md",
      "research/skills/flash-news/publish_log.json",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl",
      "research/skills/portfolio-alpha/data/resolved_urls.jsonl",
      "research/vault/meta/data/tweet_tracker.json",
      "social-agent/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: system-diagnostic: 2026-03-22 - 修復 2 個 cron timeout (300s→600s)

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 47407a0105441e3a4710b28decdf45f409fdf338

## Evidence

{
  "commit": "47407a0105441e3a4710b28decdf45f409fdf338",
  "files": [
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/data/rule_change_log.jsonl",
    "research/data/training/flash-news.jsonl",
    "research/data/training/inputs/flash_2026-03-22_17.json",
    "research/data/training/inputs/flash_2026-03-22_18.json",
    "research/data/training/inputs/flash_2026-03-22_19.json",
    "research/data/training/inputs/flash_2026-03-22_20.json",
    "research/data/training/inputs/flash_2026-03-22_21.json",
    "research/data/training/inputs/portfolio_2026-03-22_17.json",
    "research/data/training/inputs/portfolio_2026-03-22_18.json",
    "research/data/training/inputs/portfolio_2026-03-22_19.json",
    "research/data/training/inputs/portfolio_2026-03-22_20.json",
    "research/data/training/inputs/portfolio_2026-03-22_21.json",
    "research/feedback/flash_coverage_feedback.jsonl"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: research/feedback/flash_coverage_feedback.jsonl, research/feedback/flash_coverage_stats.jsonl, research/scripts/feedback_weekly_digest.py, research/skills/portfolio-alpha/data/feedback_log.jsonl",
    "large change set: 30 files"
  ]
}
