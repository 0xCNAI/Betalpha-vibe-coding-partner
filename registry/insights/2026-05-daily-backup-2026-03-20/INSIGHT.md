---
{
  "title": "daily backup 2026-03-20",
  "type": "spec_guardrail",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `8375892d669f`: daily backup 2026-03-20",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"8375892d669f1b6751d2d284c4e97590b309c5be\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/MEMORY.md\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/memory/2026-03-19.md\",\n    \"jonathan/post_history/threads_20260319_114400_market_vs_infra.md\",\n    \"jonathan/post_history/threads_20260319_150000_trump_btc.md\",\n    \"jonathan/projects/nansen-agent\",\n    \"jonathan/references/nansen_api_capability_map.md\",\n    \"jonathan/references/nansen_competition_analysis.md\",\n    \"jonathan/references/nansen_research.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/data/keywords.md\",\n    \"jonathan/skills/threads-scout/data/recommended_history.md\",\n    \"jonathan/topics/nansen_hackathon.md\",\n    \"publish/AGENTS.md\",\n    \"publish/AGENTS.md.autoresearch_backup\",\n    \"publish/MEMORY.md\",\n    \"publish/drafts/derive-overview.md\",\n    \"publish/drafts/fluid-usd-lite-vault-final.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/AGENTS.md, publish/feedback/positive_examples.jsonl, research/feedback/autoresearch_log/portfolio-writer_2026-03-19_180af1e8.json, research/feedback/autoresearch_log/portfolio-writer_2026-03-19_4a39a10d.json\",\n    \"large change set: 140 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "8375892d669f1b6751d2d284c4e97590b309c5be",
    "date": "2026-03-20T03:00:10+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "jonathan/AGENTS.md",
      "jonathan/MEMORY.md",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/memory/2026-03-19.md",
      "jonathan/post_history/threads_20260319_114400_market_vs_infra.md",
      "jonathan/post_history/threads_20260319_150000_trump_btc.md",
      "jonathan/projects/nansen-agent",
      "jonathan/references/nansen_api_capability_map.md",
      "jonathan/references/nansen_competition_analysis.md",
      "jonathan/references/nansen_research.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "jonathan/topics/nansen_hackathon.md",
      "publish/AGENTS.md",
      "publish/AGENTS.md.autoresearch_backup",
      "publish/MEMORY.md",
      "publish/drafts/derive-overview.md",
      "publish/drafts/fluid-usd-lite-vault-final.md",
      "publish/drafts/tempo-mainnet-mpp-final.md",
      "publish/drafts/tempo-mainnet-mpp.md",
      "publish/feedback/positive_examples.jsonl",
      "publish/handoffs/derive-overview.md",
      "publish/handoffs/fluid-usd-lite-vault.md",
      "publish/handoffs/tempo-mainnet-mpp.md",
      "publish/references/reporter-distillation-v1.md",
      "publish/skills/content-pipeline/SKILL.md",
      "research-agent/HEARTBEAT.md",
      "research-agent/reviewer-learnings.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: daily backup 2026-03-20

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 8375892d669f1b6751d2d284c4e97590b309c5be

## Evidence

{
  "commit": "8375892d669f1b6751d2d284c4e97590b309c5be",
  "files": [
    "betalpha-social/AGENTS.md",
    "jonathan/AGENTS.md",
    "jonathan/MEMORY.md",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/memory/2026-03-19.md",
    "jonathan/post_history/threads_20260319_114400_market_vs_infra.md",
    "jonathan/post_history/threads_20260319_150000_trump_btc.md",
    "jonathan/projects/nansen-agent",
    "jonathan/references/nansen_api_capability_map.md",
    "jonathan/references/nansen_competition_analysis.md",
    "jonathan/references/nansen_research.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/data/keywords.md",
    "jonathan/skills/threads-scout/data/recommended_history.md",
    "jonathan/topics/nansen_hackathon.md",
    "publish/AGENTS.md",
    "publish/AGENTS.md.autoresearch_backup",
    "publish/MEMORY.md",
    "publish/drafts/derive-overview.md",
    "publish/drafts/fluid-usd-lite-vault-final.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/AGENTS.md, publish/feedback/positive_examples.jsonl, research/feedback/autoresearch_log/portfolio-writer_2026-03-19_180af1e8.json, research/feedback/autoresearch_log/portfolio-writer_2026-03-19_4a39a10d.json",
    "large change set: 140 files"
  ]
}
