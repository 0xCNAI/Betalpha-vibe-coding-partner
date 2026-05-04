---
{
  "title": "fix: correct channel mapping + scout time accuracy gotcha",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `e897e485cd47`: fix: correct channel mapping + scout time accuracy gotcha",
  "prevention_signal": "Before modifying `jonathan/skills/threads-scout/data/keywords.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"e897e485cd4752e5bc9912819b714348a5038a34\",\n  \"files\": [\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"news/memory/2026-03-22.md\",\n    \"publish/handoffs/resolv_usr_update_qt.json\",\n    \"publish/skills/manual-relay/SKILL.md\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/training/flash-news.jsonl\",\n    \"research/data/training/inputs/flash_2026-03-22_16.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_16.json\",\n    \"research/memory/MEMORY.md\",\n    \"research/skills/flash-news/publish_log.json\",\n    \"research/vault/meta/data/tweet_tracker.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"large change set: 11 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/skills/threads-scout/data/keywords.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "git-history"
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
    "sha": "e897e485cd4752e5bc9912819b714348a5038a34",
    "date": "2026-03-22T16:59:30+08:00",
    "files": [
      "jonathan/skills/threads-scout/data/keywords.md",
      "news/memory/2026-03-22.md",
      "publish/handoffs/resolv_usr_update_qt.json",
      "publish/skills/manual-relay/SKILL.md",
      "research/data/pipeline_events.jsonl",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-03-22_16.json",
      "research/data/training/inputs/portfolio_2026-03-22_16.json",
      "research/memory/MEMORY.md",
      "research/skills/flash-news/publish_log.json",
      "research/vault/meta/data/tweet_tracker.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: correct channel mapping + scout time accuracy gotcha

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch e897e485cd4752e5bc9912819b714348a5038a34

## Evidence

{
  "commit": "e897e485cd4752e5bc9912819b714348a5038a34",
  "files": [
    "jonathan/skills/threads-scout/data/keywords.md",
    "news/memory/2026-03-22.md",
    "publish/handoffs/resolv_usr_update_qt.json",
    "publish/skills/manual-relay/SKILL.md",
    "research/data/pipeline_events.jsonl",
    "research/data/training/flash-news.jsonl",
    "research/data/training/inputs/flash_2026-03-22_16.json",
    "research/data/training/inputs/portfolio_2026-03-22_16.json",
    "research/memory/MEMORY.md",
    "research/skills/flash-news/publish_log.json",
    "research/vault/meta/data/tweet_tracker.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "large change set: 11 files"
  ]
}
