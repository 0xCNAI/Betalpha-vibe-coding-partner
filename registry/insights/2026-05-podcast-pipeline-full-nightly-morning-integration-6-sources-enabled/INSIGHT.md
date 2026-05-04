---
{
  "title": "podcast pipeline: full nightly + morning integration + 6 sources enabled",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `c10bd21d68d6`: podcast pipeline: full nightly + morning integration + 6 sources enabled",
  "prevention_signal": "Before modifying `betalpha-social/memory/2026-03-17.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"c10bd21d68d6925e3eb423de6a1d70107950d868\",\n  \"files\": [\n    \"betalpha-social/memory/2026-03-17.md\",\n    \"news/AGENTS.md\",\n    \"news/HEARTBEAT.md\",\n    \"news/IDENTITY.md\",\n    \"news/MEMORY.md\",\n    \"news/SOUL.md\",\n    \"publish/AGENTS.md\",\n    \"publish/HEARTBEAT.md\",\n    \"publish/IDENTITY.md\",\n    \"publish/MEMORY.md\",\n    \"publish/SOUL.md\",\n    \"publish/TEAM-PROTOCOL.md\",\n    \"publish/TOOLS.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/HEARTBEAT.md\",\n    \"research-agent/IDENTITY.md\",\n    \"research-agent/MEETING_RULES.md\",\n    \"research-agent/MEMORY.md\",\n    \"research-agent/SOUL.md\",\n    \"research-agent/TEAM-PROTOCOL.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/memory/2026-03-17.md, research/config/podcasts.json, research/skills/portfolio-alpha/data/feedback_log.jsonl, social-agent/AGENTS.md\",\n    \"large change set: 60 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/memory/2026-03-17.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "c10bd21d68d6925e3eb423de6a1d70107950d868",
    "date": "2026-03-17T22:48:04+08:00",
    "files": [
      "betalpha-social/memory/2026-03-17.md",
      "news/AGENTS.md",
      "news/HEARTBEAT.md",
      "news/IDENTITY.md",
      "news/MEMORY.md",
      "news/SOUL.md",
      "publish/AGENTS.md",
      "publish/HEARTBEAT.md",
      "publish/IDENTITY.md",
      "publish/MEMORY.md",
      "publish/SOUL.md",
      "publish/TEAM-PROTOCOL.md",
      "publish/TOOLS.md",
      "research-agent/AGENTS.md",
      "research-agent/HEARTBEAT.md",
      "research-agent/IDENTITY.md",
      "research-agent/MEETING_RULES.md",
      "research-agent/MEMORY.md",
      "research-agent/SOUL.md",
      "research-agent/TEAM-PROTOCOL.md",
      "research-agent/TOOLS.md",
      "research-agent/references/reviewer-learnings.md",
      "research-agent/references/strategy-review-rules.md",
      "research/AGENTS.md",
      "research/HEARTBEAT.md",
      "research/SOUL.md",
      "research/USER.md",
      "research/config/podcasts.json",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_tracker.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: podcast pipeline: full nightly + morning integration + 6 sources enabled

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch c10bd21d68d6925e3eb423de6a1d70107950d868

## Evidence

{
  "commit": "c10bd21d68d6925e3eb423de6a1d70107950d868",
  "files": [
    "betalpha-social/memory/2026-03-17.md",
    "news/AGENTS.md",
    "news/HEARTBEAT.md",
    "news/IDENTITY.md",
    "news/MEMORY.md",
    "news/SOUL.md",
    "publish/AGENTS.md",
    "publish/HEARTBEAT.md",
    "publish/IDENTITY.md",
    "publish/MEMORY.md",
    "publish/SOUL.md",
    "publish/TEAM-PROTOCOL.md",
    "publish/TOOLS.md",
    "research-agent/AGENTS.md",
    "research-agent/HEARTBEAT.md",
    "research-agent/IDENTITY.md",
    "research-agent/MEETING_RULES.md",
    "research-agent/MEMORY.md",
    "research-agent/SOUL.md",
    "research-agent/TEAM-PROTOCOL.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/memory/2026-03-17.md, research/config/podcasts.json, research/skills/portfolio-alpha/data/feedback_log.jsonl, social-agent/AGENTS.md",
    "large change set: 60 files"
  ]
}
