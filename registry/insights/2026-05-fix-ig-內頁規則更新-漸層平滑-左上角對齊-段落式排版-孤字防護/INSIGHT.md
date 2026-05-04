---
{
  "title": "fix: IG 內頁規則更新 - 漸層平滑/左上角對齊/段落式排版/孤字防護",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `a8a842aa72ab`: fix: IG 內頁規則更新 - 漸層平滑/左上角對齊/段落式排版/孤字防護",
  "prevention_signal": "Before modifying `jonathan/skills/instagram-image-maker/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"a8a842aa72ab44b8ab7131b691ce38583569d3f7\",\n  \"files\": [\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"research/data/corrections_tracker_state.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/memory/corrections.md\",\n    \"research/scripts/corrections_tracker.py\",\n    \"research/scripts/pipeline_observe.py\",\n    \"research/scripts/tweet_performance.py\",\n    \"research/scripts/tweet_tracker.py\",\n    \"research/skills/flash-news/flash_auto_publish.py\",\n    \"research/skills/flash-news/flash_pipeline.py\",\n    \"research/skills/news-filter/prefilter.py\",\n    \"research/skills/news-publish/publish_daily.py\",\n    \"research/skills/portfolio-alpha/data/auto_evolve_log.jsonl\",\n    \"research/skills/portfolio-alpha/scripts/prescan.py\",\n    \"research/vault/ideas/self-improving-skills-research.md\",\n    \"research/vault/meta/data/tweet_tracker.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"large change set: 16 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/skills/instagram-image-maker/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "a8a842aa72ab44b8ab7131b691ce38583569d3f7",
    "date": "2026-03-16T18:12:20+08:00",
    "files": [
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pipeline_events.jsonl",
      "research/memory/corrections.md",
      "research/scripts/corrections_tracker.py",
      "research/scripts/pipeline_observe.py",
      "research/scripts/tweet_performance.py",
      "research/scripts/tweet_tracker.py",
      "research/skills/flash-news/flash_auto_publish.py",
      "research/skills/flash-news/flash_pipeline.py",
      "research/skills/news-filter/prefilter.py",
      "research/skills/news-publish/publish_daily.py",
      "research/skills/portfolio-alpha/data/auto_evolve_log.jsonl",
      "research/skills/portfolio-alpha/scripts/prescan.py",
      "research/vault/ideas/self-improving-skills-research.md",
      "research/vault/meta/data/tweet_tracker.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: IG 內頁規則更新 - 漸層平滑/左上角對齊/段落式排版/孤字防護

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch a8a842aa72ab44b8ab7131b691ce38583569d3f7

## Evidence

{
  "commit": "a8a842aa72ab44b8ab7131b691ce38583569d3f7",
  "files": [
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "research/data/corrections_tracker_state.json",
    "research/data/pipeline_events.jsonl",
    "research/memory/corrections.md",
    "research/scripts/corrections_tracker.py",
    "research/scripts/pipeline_observe.py",
    "research/scripts/tweet_performance.py",
    "research/scripts/tweet_tracker.py",
    "research/skills/flash-news/flash_auto_publish.py",
    "research/skills/flash-news/flash_pipeline.py",
    "research/skills/news-filter/prefilter.py",
    "research/skills/news-publish/publish_daily.py",
    "research/skills/portfolio-alpha/data/auto_evolve_log.jsonl",
    "research/skills/portfolio-alpha/scripts/prescan.py",
    "research/vault/ideas/self-improving-skills-research.md",
    "research/vault/meta/data/tweet_tracker.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "large change set: 16 files"
  ]
}
