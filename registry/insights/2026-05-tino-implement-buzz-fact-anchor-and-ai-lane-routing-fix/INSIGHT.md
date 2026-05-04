---
{
  "title": "tino: implement buzz fact-anchor and AI lane routing fix",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `0e9c38050499`: tino: implement buzz fact-anchor and AI lane routing fix",
  "prevention_signal": "Before modifying `tino/scripts/agent_relay_plan.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"0e9c3805049949da1f50b797be780fd393edc23b\",\n  \"files\": [\n    \"tino/scripts/agent_relay_plan.py\",\n    \"tino/scripts/dispatch_content_agents.py\",\n    \"tino/scripts/run_content_pipeline.py\",\n    \"tino/skills/news-filter/daily_finalization.py\",\n    \"tino/skills/news-filter/draft_review.py\",\n    \"tino/skills/news-filter/feature_flags.py\",\n    \"tino/skills/news-filter/maps.py\",\n    \"tino/skills/news-filter/scout_stub.py\",\n    \"tino/skills/news-filter/source_registry.py\",\n    \"tino/skills/news-filter/story_consolidation.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"large change set: 10 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `tino/scripts/agent_relay_plan.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "0e9c3805049949da1f50b797be780fd393edc23b",
    "date": "2026-04-18T15:25:07+08:00",
    "files": [
      "tino/scripts/agent_relay_plan.py",
      "tino/scripts/dispatch_content_agents.py",
      "tino/scripts/run_content_pipeline.py",
      "tino/skills/news-filter/daily_finalization.py",
      "tino/skills/news-filter/draft_review.py",
      "tino/skills/news-filter/feature_flags.py",
      "tino/skills/news-filter/maps.py",
      "tino/skills/news-filter/scout_stub.py",
      "tino/skills/news-filter/source_registry.py",
      "tino/skills/news-filter/story_consolidation.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: tino: implement buzz fact-anchor and AI lane routing fix

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 0e9c3805049949da1f50b797be780fd393edc23b

## Evidence

{
  "commit": "0e9c3805049949da1f50b797be780fd393edc23b",
  "files": [
    "tino/scripts/agent_relay_plan.py",
    "tino/scripts/dispatch_content_agents.py",
    "tino/scripts/run_content_pipeline.py",
    "tino/skills/news-filter/daily_finalization.py",
    "tino/skills/news-filter/draft_review.py",
    "tino/skills/news-filter/feature_flags.py",
    "tino/skills/news-filter/maps.py",
    "tino/skills/news-filter/scout_stub.py",
    "tino/skills/news-filter/source_registry.py",
    "tino/skills/news-filter/story_consolidation.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "large change set: 10 files"
  ]
}
