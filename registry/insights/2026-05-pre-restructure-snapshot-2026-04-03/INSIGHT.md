---
{
  "title": "pre-restructure snapshot 2026-04-03",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `d3c43b4ccaa2`: pre-restructure snapshot 2026-04-03",
  "prevention_signal": "Before modifying `betalpha-social/memory/2026-04-01.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"d3c43b4ccaa2c3e4f6a93e2e4bf3376760e8ef8c\",\n  \"files\": [\n    \"betalpha-social/memory/2026-04-01.md\",\n    \"jonathan/memory/2026-04-03.md\",\n    \"jonathan/memory/errors.md\",\n    \"publish/AGENTS.md\",\n    \"publish/memory/2026-04-01.md\",\n    \"research/data/memory_nightly_last.json\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/runtime/event_chains.json\",\n    \"research/data/runtime/qmd_maintenance/history.jsonl\",\n    \"research/data/runtime/qmd_maintenance/lock\",\n    \"research/data/runtime/qmd_maintenance/state.json\",\n    \"research/data/training/flash-news.jsonl\",\n    \"research/data/training/inputs/flash_2026-04-03_12.json\",\n    \"research/memory/2026-04-01.md\",\n    \"research/skills/flash-news/publish_log.json\",\n    \"research/vault/_meta/orphans.md\",\n    \"research/vault/_meta/skill_versions.md\",\n    \"research/vault/inputs/podcasts/2026-03-30_the_rollup_stani_kulechov_on_why_aave_v4_is_the_most_resilient_defi_in_.md\",\n    \"research/vault/meta/data/tweet_tracker.json\",\n    \"research/vault/news/2026-04-01.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/memory/2026-04-01.md, social-agent/memory/2026-04-01.md\",\n    \"large change set: 22 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/memory/2026-04-01.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "d3c43b4ccaa2c3e4f6a93e2e4bf3376760e8ef8c",
    "date": "2026-04-03T13:52:52+08:00",
    "files": [
      "betalpha-social/memory/2026-04-01.md",
      "jonathan/memory/2026-04-03.md",
      "jonathan/memory/errors.md",
      "publish/AGENTS.md",
      "publish/memory/2026-04-01.md",
      "research/data/memory_nightly_last.json",
      "research/data/pipeline_events.jsonl",
      "research/data/runtime/event_chains.json",
      "research/data/runtime/qmd_maintenance/history.jsonl",
      "research/data/runtime/qmd_maintenance/lock",
      "research/data/runtime/qmd_maintenance/state.json",
      "research/data/training/flash-news.jsonl",
      "research/data/training/inputs/flash_2026-04-03_12.json",
      "research/memory/2026-04-01.md",
      "research/skills/flash-news/publish_log.json",
      "research/vault/_meta/orphans.md",
      "research/vault/_meta/skill_versions.md",
      "research/vault/inputs/podcasts/2026-03-30_the_rollup_stani_kulechov_on_why_aave_v4_is_the_most_resilient_defi_in_.md",
      "research/vault/meta/data/tweet_tracker.json",
      "research/vault/news/2026-04-01.md",
      "social-agent/memory/2026-04-01.md",
      "verify/triggers/daily_digest"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: pre-restructure snapshot 2026-04-03

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch d3c43b4ccaa2c3e4f6a93e2e4bf3376760e8ef8c

## Evidence

{
  "commit": "d3c43b4ccaa2c3e4f6a93e2e4bf3376760e8ef8c",
  "files": [
    "betalpha-social/memory/2026-04-01.md",
    "jonathan/memory/2026-04-03.md",
    "jonathan/memory/errors.md",
    "publish/AGENTS.md",
    "publish/memory/2026-04-01.md",
    "research/data/memory_nightly_last.json",
    "research/data/pipeline_events.jsonl",
    "research/data/runtime/event_chains.json",
    "research/data/runtime/qmd_maintenance/history.jsonl",
    "research/data/runtime/qmd_maintenance/lock",
    "research/data/runtime/qmd_maintenance/state.json",
    "research/data/training/flash-news.jsonl",
    "research/data/training/inputs/flash_2026-04-03_12.json",
    "research/memory/2026-04-01.md",
    "research/skills/flash-news/publish_log.json",
    "research/vault/_meta/orphans.md",
    "research/vault/_meta/skill_versions.md",
    "research/vault/inputs/podcasts/2026-03-30_the_rollup_stani_kulechov_on_why_aave_v4_is_the_most_resilient_defi_in_.md",
    "research/vault/meta/data/tweet_tracker.json",
    "research/vault/news/2026-04-01.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/memory/2026-04-01.md, social-agent/memory/2026-04-01.md",
    "large change set: 22 files"
  ]
}
