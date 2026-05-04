---
{
  "title": "snapshot: working tree before governance setup",
  "type": "spec_guardrail",
  "tags": [
    "auth",
    "token",
    "cron",
    "ci",
    "github",
    "migration",
    "schema",
    "deploy",
    "test"
  ],
  "tech_stack": [
    "github-actions",
    "node",
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `6b1daf97eb9d`: snapshot: working tree before governance setup",
  "prevention_signal": "Before modifying `analyst/_archive/learning/config_changes.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"6b1daf97eb9dc49c58c65e4109aba6fde622a8be\",\n  \"files\": [\n    \"AGENTS.md\",\n    \"CLAUDE.md\",\n    \"SOUL.md\",\n    \"analyst/AGENTS.md\",\n    \"analyst/CLAUDE.md\",\n    \"analyst/DREAMS.md\",\n    \"analyst/HEARTBEAT.md\",\n    \"analyst/IDENTITY.md\",\n    \"analyst/MEMORY.md\",\n    \"analyst/SOUL.md\",\n    \"analyst/TOOLS.md\",\n    \"analyst/USER.md\",\n    \"analyst/_archive/AGENTS.md.backup-20260220\",\n    \"analyst/_archive/AGENTS.md.bak\",\n    \"analyst/_archive/HEARTBEAT.md.bak\",\n    \"analyst/_archive/IDENTITY.md.bak\",\n    \"analyst/_archive/MEMORY.md.bak\",\n    \"analyst/_archive/SOUL.md.bak\",\n    \"analyst/_archive/TOOLS.md.bak\",\n    \"analyst/_archive/USER.md.bak\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: analyst/_archive/learning/config_changes.md, analyst/vault/context/local/workflows/benchmark-todayindefi.md, analyst/vault/context/local/workflows/content-gap-analysis.md, analyst/vault/context/local/workflows/strategy-review.md\",\n    \"large change set: 28056 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `analyst/_archive/learning/config_changes.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "auth",
      "token",
      "cron",
      "ci",
      "github",
      "migration",
      "schema",
      "deploy",
      "test"
    ],
    "tech_stack": [
      "github-actions",
      "node",
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
    "sha": "6b1daf97eb9dc49c58c65e4109aba6fde622a8be",
    "date": "2026-04-17T15:43:19+08:00",
    "files": [
      "AGENTS.md",
      "CLAUDE.md",
      "SOUL.md",
      "analyst/AGENTS.md",
      "analyst/CLAUDE.md",
      "analyst/DREAMS.md",
      "analyst/HEARTBEAT.md",
      "analyst/IDENTITY.md",
      "analyst/MEMORY.md",
      "analyst/SOUL.md",
      "analyst/TOOLS.md",
      "analyst/USER.md",
      "analyst/_archive/AGENTS.md.backup-20260220",
      "analyst/_archive/AGENTS.md.bak",
      "analyst/_archive/HEARTBEAT.md.bak",
      "analyst/_archive/IDENTITY.md.bak",
      "analyst/_archive/MEMORY.md.bak",
      "analyst/_archive/SOUL.md.bak",
      "analyst/_archive/TOOLS.md.bak",
      "analyst/_archive/USER.md.bak",
      "analyst/_archive/_ARCHIVE_README.md",
      "analyst/_archive/data/reviewer-learnings.md",
      "analyst/_archive/learning/config_changes.md",
      "analyst/_archive/memory/2026-02-20.md",
      "analyst/_archive/memory/2026-03-16-baseline.md",
      "analyst/_archive/memory/2026-03-26.md",
      "analyst/_archive/memory/2026-03-27.md",
      "analyst/_archive/memory/2026-03-30-baseline.md",
      "analyst/_archive/memory/2026-03-30.md",
      "analyst/_archive/memory/2026-03-31.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: snapshot: working tree before governance setup

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 6b1daf97eb9dc49c58c65e4109aba6fde622a8be

## Evidence

{
  "commit": "6b1daf97eb9dc49c58c65e4109aba6fde622a8be",
  "files": [
    "AGENTS.md",
    "CLAUDE.md",
    "SOUL.md",
    "analyst/AGENTS.md",
    "analyst/CLAUDE.md",
    "analyst/DREAMS.md",
    "analyst/HEARTBEAT.md",
    "analyst/IDENTITY.md",
    "analyst/MEMORY.md",
    "analyst/SOUL.md",
    "analyst/TOOLS.md",
    "analyst/USER.md",
    "analyst/_archive/AGENTS.md.backup-20260220",
    "analyst/_archive/AGENTS.md.bak",
    "analyst/_archive/HEARTBEAT.md.bak",
    "analyst/_archive/IDENTITY.md.bak",
    "analyst/_archive/MEMORY.md.bak",
    "analyst/_archive/SOUL.md.bak",
    "analyst/_archive/TOOLS.md.bak",
    "analyst/_archive/USER.md.bak"
  ],
  "reasons": [
    "touches risky subsystem: analyst/_archive/learning/config_changes.md, analyst/vault/context/local/workflows/benchmark-todayindefi.md, analyst/vault/context/local/workflows/content-gap-analysis.md, analyst/vault/context/local/workflows/strategy-review.md",
    "large change set: 28056 files"
  ]
}
