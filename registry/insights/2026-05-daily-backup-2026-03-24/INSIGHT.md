---
{
  "title": "daily backup 2026-03-24",
  "type": "spec_guardrail",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `bf7375981ee9`: daily backup 2026-03-24",
  "prevention_signal": "Before modifying `betalpha-social/TOOLS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"bf7375981ee9630385028103a9a0ac6e694acc76\",\n  \"files\": [\n    \"betalpha-social/TOOLS.md\",\n    \"betalpha-social/skills/threads-post-publish/SKILL.md\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/scripts/threads_performance_daily.py\",\n    \"jonathan/skills/betalpha-analytics/performance_data.md\",\n    \"jonathan/skills/betalpha-analytics/performance_data.md.bak-2026-03-24-0058\",\n    \"jonathan/skills/betalpha-screenshot/SKILL.md\",\n    \"jonathan/skills/threads-scout/SKILL.md\",\n    \"publish/TOOLS.md\",\n    \"research-agent/TOOLS.md\",\n    \"research/AGENTS.md\",\n    \"research/TOOLS.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pending_rule_proposals.jsonl\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/podcast_pipeline_state.json\",\n    \"research/data/podcast_processed.json\",\n    \"research/data/rule_verdicts.jsonl\",\n    \"research/data/training/flash-news.jsonl\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/TOOLS.md, betalpha-social/skills/threads-post-publish/SKILL.md, research/skills/portfolio-alpha/data/feedback_log.jsonl, research/vault/inputs/podcasts/2026-03-19_unchained_dex_in_the_city_why_the_binance_case_against_the_wsj_is_prob.md\",\n    \"large change set: 52 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/TOOLS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "bf7375981ee9630385028103a9a0ac6e694acc76",
    "date": "2026-03-24T03:00:50+08:00",
    "files": [
      "betalpha-social/TOOLS.md",
      "betalpha-social/skills/threads-post-publish/SKILL.md",
      "jonathan/TOOLS.md",
      "jonathan/scripts/threads_performance_daily.py",
      "jonathan/skills/betalpha-analytics/performance_data.md",
      "jonathan/skills/betalpha-analytics/performance_data.md.bak-2026-03-24-0058",
      "jonathan/skills/betalpha-screenshot/SKILL.md",
      "jonathan/skills/threads-scout/SKILL.md",
      "publish/TOOLS.md",
      "research-agent/TOOLS.md",
      "research/AGENTS.md",
      "research/TOOLS.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_tracker.json",
      "research/data/pending_rule_proposals.jsonl",
      "research/data/pipeline_events.jsonl",
      "research/data/podcast_pipeline_state.json",
      "research/data/podcast_processed.json",
      "research/data/rule_verdicts.jsonl",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-03-23_22.json",
      "research/data/training/inputs/flash_2026-03-23_23.json",
      "research/data/training/inputs/portfolio_2026-03-23_22.json",
      "research/memory/2026-03-23.md",
      "research/memory/2026-03-24.md",
      "research/memory/corrections.md",
      "research/scripts/podcast_nightly.py",
      "research/scripts/tweet_performance.py",
      "research/skills/flash-news/publish_log.json",
      "research/skills/portfolio-alpha/data/auto_evolve_log.jsonl"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: daily backup 2026-03-24

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch bf7375981ee9630385028103a9a0ac6e694acc76

## Evidence

{
  "commit": "bf7375981ee9630385028103a9a0ac6e694acc76",
  "files": [
    "betalpha-social/TOOLS.md",
    "betalpha-social/skills/threads-post-publish/SKILL.md",
    "jonathan/TOOLS.md",
    "jonathan/scripts/threads_performance_daily.py",
    "jonathan/skills/betalpha-analytics/performance_data.md",
    "jonathan/skills/betalpha-analytics/performance_data.md.bak-2026-03-24-0058",
    "jonathan/skills/betalpha-screenshot/SKILL.md",
    "jonathan/skills/threads-scout/SKILL.md",
    "publish/TOOLS.md",
    "research-agent/TOOLS.md",
    "research/AGENTS.md",
    "research/TOOLS.md",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_tracker.json",
    "research/data/pending_rule_proposals.jsonl",
    "research/data/pipeline_events.jsonl",
    "research/data/podcast_pipeline_state.json",
    "research/data/podcast_processed.json",
    "research/data/rule_verdicts.jsonl",
    "research/data/training/flash-news.jsonl"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/TOOLS.md, betalpha-social/skills/threads-post-publish/SKILL.md, research/skills/portfolio-alpha/data/feedback_log.jsonl, research/vault/inputs/podcasts/2026-03-19_unchained_dex_in_the_city_why_the_binance_case_against_the_wsj_is_prob.md",
    "large change set: 52 files"
  ]
}
