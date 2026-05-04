---
{
  "title": "thread pipeline: cross-pipeline thread ideas pool + scout/writer/reviewer thread support +",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `18d2d7345c34`: thread pipeline: cross-pipeline thread ideas pool + scout/writer/reviewer thread support + x_post_api thread command",
  "prevention_signal": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"18d2d7345c34004c31e3bf055802306fc026fc5c\",\n  \"files\": [\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-17.md\",\n    \"\\\"betalpha-social/post_history/2026-03-16_instagram_Venus_Protocol\\\\344\\\\276\\\\233\\\\346\\\\207\\\\211\\\\344\\\\270\\\\212\\\\351\\\\231\\\\220\\\\346\\\\223\\\\215\\\\347\\\\270\\\\261\\\\346\\\\224\\\\273\\\\346\\\\223\\\\212.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-16_threads_\\\\346\\\\210\\\\260\\\\347\\\\210\\\\255\\\\350\\\\241\\\\235\\\\346\\\\223\\\\212\\\\344\\\\270\\\\213Crypto\\\\351\\\\200\\\\206\\\\345\\\\213\\\\242\\\\350\\\\265\\\\260\\\\345\\\\274\\\\267.md\\\"\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"publish/AGENTS.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/daily_feedback_log.jsonl\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/learning/patterns.md\",\n    \"research/memory/MEMORY.md\",\n    \"research/memory/corrections.md\",\n    \"research/scripts/thread_ideas_pool.py\",\n    \"research/scripts/x_post_api.py\",\n    \"research/skills/flash-news/publish_log.json\",\n    \"research/skills/news-filter/score_history.json\",\n    \"research/skills/news-filter/selector_history.json\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-17.md, \\\"betalpha-social/post_history/2026-03-16_instagram_Venus_Protocol\\\\344\\\\276\\\\233\\\\346\\\\207\\\\211\\\\344\\\\270\\\\212\\\\351\\\\231\\\\220\\\\346\\\\223\\\\215\\\\347\\\\270\\\\261\\\\346\\\\224\\\\273\\\\346\\\\223\\\\212.md\\\", \\\"betalpha-social/post_history/2026-03-16_threads_\\\\346\\\\210\\\\260\\\\347\\\\210\\\\255\\\\350\\\\241\\\\235\\\\346\\\\223\\\\212\\\\344\\\\270\\\\213Crypto\\\\351\\\\200\\\\206\\\\345\\\\213\\\\242\\\\350\\\\265\\\\260\\\\345\\\\274\\\\267.md\\\"\",\n    \"large change set: 30 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/learning/jc_activity_tracking.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "git-history"
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
    "sha": "18d2d7345c34004c31e3bf055802306fc026fc5c",
    "date": "2026-03-17T11:40:42+08:00",
    "files": [
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-17.md",
      "\"betalpha-social/post_history/2026-03-16_instagram_Venus_Protocol\\344\\276\\233\\346\\207\\211\\344\\270\\212\\351\\231\\220\\346\\223\\215\\347\\270\\261\\346\\224\\273\\346\\223\\212.md\"",
      "\"betalpha-social/post_history/2026-03-16_threads_\\346\\210\\260\\347\\210\\255\\350\\241\\235\\346\\223\\212\\344\\270\\213Crypto\\351\\200\\206\\345\\213\\242\\350\\265\\260\\345\\274\\267.md\"",
      "jonathan/data/daily_kol_digest.md",
      "publish/AGENTS.md",
      "research-agent/AGENTS.md",
      "research-agent/reviewer-learnings.md",
      "research/data/corrections_tracker_state.json",
      "research/data/daily_feedback_log.jsonl",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/learning/patterns.md",
      "research/memory/MEMORY.md",
      "research/memory/corrections.md",
      "research/scripts/thread_ideas_pool.py",
      "research/scripts/x_post_api.py",
      "research/skills/flash-news/publish_log.json",
      "research/skills/news-filter/score_history.json",
      "research/skills/news-filter/selector_history.json",
      "research/skills/portfolio-alpha/data/auto_evolve_log.jsonl",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl",
      "research/skills/portfolio-alpha/references/scout-rules.md",
      "research/skills/portfolio-alpha/references/tino-reviewer-rules.md",
      "research/skills/portfolio-alpha/references/writer-rules.md",
      "research/skills/portfolio-alpha/scripts/prescan.py",
      "research/vault/meta/data/tweet_performance.jsonl",
      "research/vault/meta/data/tweet_tracker.json",
      "research/vault/news/2026-03-17.md",
      "verify/triggers/daily_digest"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: thread pipeline: cross-pipeline thread ideas pool + scout/writer/reviewer thread support + x_post_api thread command

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 18d2d7345c34004c31e3bf055802306fc026fc5c

## Evidence

{
  "commit": "18d2d7345c34004c31e3bf055802306fc026fc5c",
  "files": [
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-17.md",
    "\"betalpha-social/post_history/2026-03-16_instagram_Venus_Protocol\\344\\276\\233\\346\\207\\211\\344\\270\\212\\351\\231\\220\\346\\223\\215\\347\\270\\261\\346\\224\\273\\346\\223\\212.md\"",
    "\"betalpha-social/post_history/2026-03-16_threads_\\346\\210\\260\\347\\210\\255\\350\\241\\235\\346\\223\\212\\344\\270\\213Crypto\\351\\200\\206\\345\\213\\242\\350\\265\\260\\345\\274\\267.md\"",
    "jonathan/data/daily_kol_digest.md",
    "publish/AGENTS.md",
    "research-agent/AGENTS.md",
    "research-agent/reviewer-learnings.md",
    "research/data/corrections_tracker_state.json",
    "research/data/daily_feedback_log.jsonl",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/learning/patterns.md",
    "research/memory/MEMORY.md",
    "research/memory/corrections.md",
    "research/scripts/thread_ideas_pool.py",
    "research/scripts/x_post_api.py",
    "research/skills/flash-news/publish_log.json",
    "research/skills/news-filter/score_history.json",
    "research/skills/news-filter/selector_history.json"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/learning/jc_activity_tracking.md, betalpha-social/memory/2026-03-17.md, \"betalpha-social/post_history/2026-03-16_instagram_Venus_Protocol\\344\\276\\233\\346\\207\\211\\344\\270\\212\\351\\231\\220\\346\\223\\215\\347\\270\\261\\346\\224\\273\\346\\223\\212.md\", \"betalpha-social/post_history/2026-03-16_threads_\\346\\210\\260\\347\\210\\255\\350\\241\\235\\346\\223\\212\\344\\270\\213Crypto\\351\\200\\206\\345\\213\\242\\350\\265\\260\\345\\274\\267.md\"",
    "large change set: 30 files"
  ]
}
