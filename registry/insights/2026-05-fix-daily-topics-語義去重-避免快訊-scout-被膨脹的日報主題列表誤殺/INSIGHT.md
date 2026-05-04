---
{
  "title": "fix: daily_topics 語義去重，避免快訊 Scout 被膨脹的日報主題列表誤殺",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `50ebbf770eba`: fix: daily_topics 語義去重，避免快訊 Scout 被膨脹的日報主題列表誤殺",
  "prevention_signal": "Before modifying `research/skills/flash-news/flash_pipeline.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"50ebbf770eba11ac3d8c7ce3ca80b60ceb28dcc0\",\n  \"files\": [\n    \"research/skills/flash-news/flash_pipeline.py\",\n    \"research/skills/news-filter/merge_clusters.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/skills/flash-news/flash_pipeline.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "50ebbf770eba11ac3d8c7ce3ca80b60ceb28dcc0",
    "date": "2026-03-21T15:07:39+08:00",
    "files": [
      "research/skills/flash-news/flash_pipeline.py",
      "research/skills/news-filter/merge_clusters.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: daily_topics 語義去重，避免快訊 Scout 被膨脹的日報主題列表誤殺

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 50ebbf770eba11ac3d8c7ce3ca80b60ceb28dcc0

## Evidence

{
  "commit": "50ebbf770eba11ac3d8c7ce3ca80b60ceb28dcc0",
  "files": [
    "research/skills/flash-news/flash_pipeline.py",
    "research/skills/news-filter/merge_clusters.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
