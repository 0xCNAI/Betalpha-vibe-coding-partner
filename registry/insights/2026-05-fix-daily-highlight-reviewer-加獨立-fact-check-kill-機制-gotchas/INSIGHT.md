---
{
  "title": "fix: daily-highlight reviewer 加獨立 fact-check + Kill 機制 + gotchas",
  "type": "pitfall",
  "tags": [
    "cron"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `18a8a1c0938a`: fix: daily-highlight reviewer 加獨立 fact-check + Kill 機制 + gotchas",
  "prevention_signal": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"18a8a1c0938a53c513568bdc037f7dc92b44f207\",\n  \"files\": [\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"\\\"betalpha-social/post_history/2026-03-20_instagram_NVIDIA_CEO\\\\350\\\\252\\\\215\\\\345\\\\217\\\\257Bittensor.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-20_threads_Gemini\\\\350\\\\210\\\\207Crypto_com\\\\350\\\\243\\\\201\\\\345\\\\223\\\\241\\\\350\\\\242\\\\253\\\\345\\\\270\\\\202\\\\345\\\\240\\\\264\\\\350\\\\246\\\\226\\\\347\\\\202\\\\272\\\\345\\\\210\\\\251\\\\345\\\\245\\\\275.md\\\"\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"publish/AGENTS.md\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/training/inputs/flash_2026-03-21_09.json\",\n    \"research/data/training/inputs/flash_2026-03-21_10.json\",\n    \"research/data/training/inputs/flash_2026-03-21_11.json\",\n    \"research/data/training/inputs/flash_2026-03-21_12.json\",\n    \"research/data/training/inputs/portfolio_2026-03-21_08.json\",\n    \"research/data/training/inputs/portfolio_2026-03-21_09.json\",\n    \"research/data/training/inputs/portfolio_2026-03-21_10.json\",\n    \"research/data/training/inputs/portfolio_2026-03-21_11.json\",\n    \"research/feedback/flash_coverage_feedback.jsonl\",\n    \"research/feedback/flash_coverage_stats.jsonl\",\n    \"research/skills/news-filter/score_history.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, \\\"betalpha-social/post_history/2026-03-20_instagram_NVIDIA_CEO\\\\350\\\\252\\\\215\\\\345\\\\217\\\\257Bittensor.md\\\", \\\"betalpha-social/post_history/2026-03-20_threads_Gemini\\\\350\\\\210\\\\207Crypto_com\\\\350\\\\243\\\\201\\\\345\\\\223\\\\241\\\\350\\\\242\\\\253\\\\345\\\\270\\\\202\\\\345\\\\240\\\\264\\\\350\\\\246\\\\226\\\\347\\\\202\\\\272\\\\345\\\\210\\\\251\\\\345\\\\245\\\\275.md\\\", research/feedback/flash_coverage_feedback.jsonl\",\n    \"large change set: 31 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron"
    ],
    "tech_stack": [],
    "source_kind": "git_commit"
  },
  "tech_versions_last_seen": {},
  "created_at": "2026-05-04",
  "last_verified_at": "2026-05-04",
  "source": {
    "kind": "git_commit",
    "repo": "/Users/betalpha/clawd",
    "sha": "18a8a1c0938a53c513568bdc037f7dc92b44f207",
    "date": "2026-03-21T12:36:40+08:00",
    "files": [
      "betalpha-social/learning/jc_activity_tracking.md",
      "\"betalpha-social/post_history/2026-03-20_instagram_NVIDIA_CEO\\350\\252\\215\\345\\217\\257Bittensor.md\"",
      "\"betalpha-social/post_history/2026-03-20_threads_Gemini\\350\\210\\207Crypto_com\\350\\243\\201\\345\\223\\241\\350\\242\\253\\345\\270\\202\\345\\240\\264\\350\\246\\226\\347\\202\\272\\345\\210\\251\\345\\245\\275.md\"",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "research/data/pipeline_events.jsonl",
      "research/data/training/inputs/flash_2026-03-21_09.json",
      "research/data/training/inputs/flash_2026-03-21_10.json",
      "research/data/training/inputs/flash_2026-03-21_11.json",
      "research/data/training/inputs/flash_2026-03-21_12.json",
      "research/data/training/inputs/portfolio_2026-03-21_08.json",
      "research/data/training/inputs/portfolio_2026-03-21_09.json",
      "research/data/training/inputs/portfolio_2026-03-21_10.json",
      "research/data/training/inputs/portfolio_2026-03-21_11.json",
      "research/feedback/flash_coverage_feedback.jsonl",
      "research/feedback/flash_coverage_stats.jsonl",
      "research/skills/news-filter/score_history.json",
      "research/skills/news-filter/selector_history.json",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl",
      "research/skills/portfolio-alpha/data/good_examples.jsonl",
      "\"research/vault/inputs/podcasts/2026-03-18_gooaye_\\350\\202\\241\\347\\231\\214_ep645.md\"",
      "\"research/vault/inputs/podcasts/2026-03-18_\\345\\221\\242\\345\\226\\203\\350\\262\\223_ep292_\\345\\276\\256\\347\\255\\226\\347\\225\\245\\351\\207\\215\\345\\225\\237_btc_\\347\\204\\241\\351\\231\\220\\345\\212\\240\\347\\242\\274\\345\\274\\225\\346\\223\\216\\344\\275\\206\\351\\200\\231\\346\\254\\241\\347\\234\\237\\347\\232\\204\\344\\270\\215\\344\\270\\200\\346\\250\\243\\345\\227\\216.md\"",
      "research/vault/meta/cron_schedule.md",
      "research/vault/meta/data/tweet_performance.jsonl",
      "research/vault/meta/data/tweet_tracker.json",
      "research/vault/news/2026-03-21.md",
      "social-agent/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: daily-highlight reviewer 加獨立 fact-check + Kill 機制 + gotchas

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 18a8a1c0938a53c513568bdc037f7dc92b44f207

## Evidence

{
  "commit": "18a8a1c0938a53c513568bdc037f7dc92b44f207",
  "files": [
    "betalpha-social/learning/jc_activity_tracking.md",
    "\"betalpha-social/post_history/2026-03-20_instagram_NVIDIA_CEO\\350\\252\\215\\345\\217\\257Bittensor.md\"",
    "\"betalpha-social/post_history/2026-03-20_threads_Gemini\\350\\210\\207Crypto_com\\350\\243\\201\\345\\223\\241\\350\\242\\253\\345\\270\\202\\345\\240\\264\\350\\246\\226\\347\\202\\272\\345\\210\\251\\345\\245\\275.md\"",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "publish/AGENTS.md",
    "research/data/pipeline_events.jsonl",
    "research/data/training/inputs/flash_2026-03-21_09.json",
    "research/data/training/inputs/flash_2026-03-21_10.json",
    "research/data/training/inputs/flash_2026-03-21_11.json",
    "research/data/training/inputs/flash_2026-03-21_12.json",
    "research/data/training/inputs/portfolio_2026-03-21_08.json",
    "research/data/training/inputs/portfolio_2026-03-21_09.json",
    "research/data/training/inputs/portfolio_2026-03-21_10.json",
    "research/data/training/inputs/portfolio_2026-03-21_11.json",
    "research/feedback/flash_coverage_feedback.jsonl",
    "research/feedback/flash_coverage_stats.jsonl",
    "research/skills/news-filter/score_history.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, \"betalpha-social/post_history/2026-03-20_instagram_NVIDIA_CEO\\350\\252\\215\\345\\217\\257Bittensor.md\", \"betalpha-social/post_history/2026-03-20_threads_Gemini\\350\\210\\207Crypto_com\\350\\243\\201\\345\\223\\241\\350\\242\\253\\345\\270\\202\\345\\240\\264\\350\\246\\226\\347\\202\\272\\345\\210\\251\\345\\245\\275.md\", research/feedback/flash_coverage_feedback.jsonl",
    "large change set: 31 files"
  ]
}
