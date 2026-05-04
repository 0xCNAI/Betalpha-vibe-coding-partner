---
{
  "title": "fix: IG輪播內頁規則大修 - 尺寸/漸層/標題/排版統一",
  "type": "pitfall",
  "tags": [
    "schema"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `210fa255222c`: fix: IG輪播內頁規則大修 - 尺寸/漸層/標題/排版統一",
  "prevention_signal": "Before modifying `betalpha-social/MEMORY.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"210fa255222c24bc621bdae4247251435f6a2e58\",\n  \"files\": [\n    \"betalpha-social/MEMORY.md\",\n    \"betalpha-social/SKILLS_INDEX.md\",\n    \"betalpha-social/TOOLS.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"jonathan/content/publish_llm_hack.sh\",\n    \"jonathan/post_history/threads_20260317_134600_dogecoin_etf.md\",\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"publish/TOOLS.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/TOOLS.md\",\n    \"research/config/podcasts.json\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pattern_tracker.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/podcast_processed.json\",\n    \"research/learning/patterns.md\",\n    \"research/memory/2026-03-17.md\",\n    \"research/memory/MEMORY.md\",\n    \"research/memory/corrections.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: betalpha-social/MEMORY.md, betalpha-social/SKILLS_INDEX.md, betalpha-social/TOOLS.md, betalpha-social/learning/LESSONS.md\",\n    \"large change set: 45 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/MEMORY.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
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
    "sha": "210fa255222c24bc621bdae4247251435f6a2e58",
    "date": "2026-03-17T15:19:23+08:00",
    "files": [
      "betalpha-social/MEMORY.md",
      "betalpha-social/SKILLS_INDEX.md",
      "betalpha-social/TOOLS.md",
      "betalpha-social/learning/LESSONS.md",
      "jonathan/content/publish_llm_hack.sh",
      "jonathan/post_history/threads_20260317_134600_dogecoin_etf.md",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "publish/TOOLS.md",
      "research-agent/AGENTS.md",
      "research-agent/reviewer-learnings.md",
      "research/TOOLS.md",
      "research/config/podcasts.json",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/data/podcast_processed.json",
      "research/learning/patterns.md",
      "research/memory/2026-03-17.md",
      "research/memory/MEMORY.md",
      "research/memory/corrections.md",
      "research/scripts/auto_evolve.py",
      "research/scripts/feedback_inject.py",
      "research/scripts/podcast_digest.py",
      "research/scripts/podcast_fetch.py",
      "research/scripts/podcast_transcribe.py",
      "research/scripts/thread_ideas_pool.py",
      "research/scripts/x_post_api.py",
      "research/skills/flash-news/publish_log.json",
      "research/skills/portfolio-alpha/SKILL.md",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: IG輪播內頁規則大修 - 尺寸/漸層/標題/排版統一

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 210fa255222c24bc621bdae4247251435f6a2e58

## Evidence

{
  "commit": "210fa255222c24bc621bdae4247251435f6a2e58",
  "files": [
    "betalpha-social/MEMORY.md",
    "betalpha-social/SKILLS_INDEX.md",
    "betalpha-social/TOOLS.md",
    "betalpha-social/learning/LESSONS.md",
    "jonathan/content/publish_llm_hack.sh",
    "jonathan/post_history/threads_20260317_134600_dogecoin_etf.md",
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "publish/TOOLS.md",
    "research-agent/AGENTS.md",
    "research-agent/reviewer-learnings.md",
    "research/TOOLS.md",
    "research/config/podcasts.json",
    "research/data/corrections_tracker_state.json",
    "research/data/pattern_tracker.json",
    "research/data/pipeline_events.jsonl",
    "research/data/podcast_processed.json",
    "research/learning/patterns.md",
    "research/memory/2026-03-17.md",
    "research/memory/MEMORY.md",
    "research/memory/corrections.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: betalpha-social/MEMORY.md, betalpha-social/SKILLS_INDEX.md, betalpha-social/TOOLS.md, betalpha-social/learning/LESSONS.md",
    "large change set: 45 files"
  ]
}
