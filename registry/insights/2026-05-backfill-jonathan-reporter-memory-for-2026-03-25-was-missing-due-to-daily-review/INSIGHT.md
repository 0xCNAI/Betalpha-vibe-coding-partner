---
{
  "title": "backfill: jonathan + reporter memory for 2026-03-25 (was missing due to daily-review API f",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `592d43e02d52`: backfill: jonathan + reporter memory for 2026-03-25 (was missing due to daily-review API failure)",
  "prevention_signal": "Before modifying `jonathan/memory/2026-03-25.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"592d43e02d524eaf9e5cc259533953d35b331c83\",\n  \"files\": [\n    \"jonathan/memory/2026-03-25.md\",\n    \"publish/memory/2026-03-25.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/memory/2026-03-25.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "592d43e02d524eaf9e5cc259533953d35b331c83",
    "date": "2026-03-26T13:52:51+08:00",
    "files": [
      "jonathan/memory/2026-03-25.md",
      "publish/memory/2026-03-25.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: backfill: jonathan + reporter memory for 2026-03-25 (was missing due to daily-review API failure)

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 592d43e02d524eaf9e5cc259533953d35b331c83

## Evidence

{
  "commit": "592d43e02d524eaf9e5cc259533953d35b331c83",
  "files": [
    "jonathan/memory/2026-03-25.md",
    "publish/memory/2026-03-25.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
