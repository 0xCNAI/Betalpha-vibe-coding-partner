---
{
  "title": "fix: 新聞日期檢查+cron timeout延長至10分鐘+KOL摘要過期fallback",
  "type": "pitfall",
  "tags": [
    "cron"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `937a39180bcd`: fix: 新聞日期檢查+cron timeout延長至10分鐘+KOL摘要過期fallback",
  "prevention_signal": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"937a39180bcd41f2afd0db52fd378cfda15cad5f\",\n  \"files\": [\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"\\\"betalpha-social/post_history/2026-03-17_threads_TRowe_Price\\\\346\\\\217\\\\220\\\\344\\\\272\\\\244DOGE_SHIB_ETF.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-17_threads_\\\\346\\\\234\\\\200\\\\350\\\\262\\\\264\\\\351\\\\233\\\\242\\\\345\\\\251\\\\232\\\\346\\\\241\\\\210\\\\345\\\\201\\\\267\\\\350\\\\265\\\\2602323\\\\346\\\\236\\\\232BTC.md\\\"\",\n    \"betalpha-social/threads/20260318_piverse_thread.md\",\n    \"jonathan/skills/betalpha-content/SKILL.md\",\n    \"jonathan/skills/threads-ideation/SKILL.md\",\n    \"jonathan/skills/threads-scout/SKILL.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/daily_feedback_log.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/rule_verdicts.jsonl\",\n    \"research/memory/corrections.md\",\n    \"research/skills/flash-news/publish_log.json\",\n    \"research/skills/news-filter/score_history.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/learning/jc_activity_tracking.md, \\\"betalpha-social/post_history/2026-03-17_threads_TRowe_Price\\\\346\\\\217\\\\220\\\\344\\\\272\\\\244DOGE_SHIB_ETF.md\\\", \\\"betalpha-social/post_history/2026-03-17_threads_\\\\346\\\\234\\\\200\\\\350\\\\262\\\\264\\\\351\\\\233\\\\242\\\\345\\\\251\\\\232\\\\346\\\\241\\\\210\\\\345\\\\201\\\\267\\\\350\\\\265\\\\2602323\\\\346\\\\236\\\\232BTC.md\\\"\",\n    \"large change set: 29 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/LESSONS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "937a39180bcd41f2afd0db52fd378cfda15cad5f",
    "date": "2026-03-18T11:23:09+08:00",
    "files": [
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/learning/jc_activity_tracking.md",
      "\"betalpha-social/post_history/2026-03-17_threads_TRowe_Price\\346\\217\\220\\344\\272\\244DOGE_SHIB_ETF.md\"",
      "\"betalpha-social/post_history/2026-03-17_threads_\\346\\234\\200\\350\\262\\264\\351\\233\\242\\345\\251\\232\\346\\241\\210\\345\\201\\267\\350\\265\\2602323\\346\\236\\232BTC.md\"",
      "betalpha-social/threads/20260318_piverse_thread.md",
      "jonathan/skills/betalpha-content/SKILL.md",
      "jonathan/skills/threads-ideation/SKILL.md",
      "jonathan/skills/threads-scout/SKILL.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "research-agent/AGENTS.md",
      "research-agent/reviewer-learnings.md",
      "research/data/corrections_tracker_state.json",
      "research/data/daily_feedback_log.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/rule_verdicts.jsonl",
      "research/memory/corrections.md",
      "research/skills/flash-news/publish_log.json",
      "research/skills/news-filter/score_history.json",
      "research/skills/news-filter/selector_history.json",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl",
      "research/skills/portfolio-alpha/data/good_examples.jsonl",
      "\"research/vault/inputs/podcasts/2026-03-14_\\350\\202\\241\\347\\231\\214_ep644.md\"",
      "research/vault/meta/data/tweet_performance.jsonl",
      "research/vault/meta/data/tweet_tracker.json",
      "research/vault/meta/flash_selection_principles.md",
      "research/vault/news/2026-03-18.md",
      "verify/triggers/daily_digest"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: 新聞日期檢查+cron timeout延長至10分鐘+KOL摘要過期fallback

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 937a39180bcd41f2afd0db52fd378cfda15cad5f

## Evidence

{
  "commit": "937a39180bcd41f2afd0db52fd378cfda15cad5f",
  "files": [
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/learning/jc_activity_tracking.md",
    "\"betalpha-social/post_history/2026-03-17_threads_TRowe_Price\\346\\217\\220\\344\\272\\244DOGE_SHIB_ETF.md\"",
    "\"betalpha-social/post_history/2026-03-17_threads_\\346\\234\\200\\350\\262\\264\\351\\233\\242\\345\\251\\232\\346\\241\\210\\345\\201\\267\\350\\265\\2602323\\346\\236\\232BTC.md\"",
    "betalpha-social/threads/20260318_piverse_thread.md",
    "jonathan/skills/betalpha-content/SKILL.md",
    "jonathan/skills/threads-ideation/SKILL.md",
    "jonathan/skills/threads-scout/SKILL.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "research-agent/AGENTS.md",
    "research-agent/reviewer-learnings.md",
    "research/data/corrections_tracker_state.json",
    "research/data/daily_feedback_log.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/data/rule_verdicts.jsonl",
    "research/memory/corrections.md",
    "research/skills/flash-news/publish_log.json",
    "research/skills/news-filter/score_history.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/learning/LESSONS.md, betalpha-social/learning/jc_activity_tracking.md, \"betalpha-social/post_history/2026-03-17_threads_TRowe_Price\\346\\217\\220\\344\\272\\244DOGE_SHIB_ETF.md\", \"betalpha-social/post_history/2026-03-17_threads_\\346\\234\\200\\350\\262\\264\\351\\233\\242\\345\\251\\232\\346\\241\\210\\345\\201\\267\\350\\265\\2602323\\346\\236\\232BTC.md\"",
    "large change set: 29 files"
  ]
}
