---
{
  "title": "Upgrade daily raw to canonical source-context schema",
  "type": "pitfall",
  "tags": [
    "schema"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `105ca77f1668`: Upgrade daily raw to canonical source-context schema",
  "prevention_signal": "Before modifying `jonathan/memory/2026-04-14.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"105ca77f1668084549ef110467d57001aaf99edf\",\n  \"files\": [\n    \"jonathan/memory/2026-04-14.md\",\n    \"jonathan/scripts/daily_raw_update.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/memory/2026-04-14.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "105ca77f1668084549ef110467d57001aaf99edf",
    "date": "2026-04-14T12:44:22+08:00",
    "files": [
      "jonathan/memory/2026-04-14.md",
      "jonathan/scripts/daily_raw_update.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: Upgrade daily raw to canonical source-context schema

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 105ca77f1668084549ef110467d57001aaf99edf

## Evidence

{
  "commit": "105ca77f1668084549ef110467d57001aaf99edf",
  "files": [
    "jonathan/memory/2026-04-14.md",
    "jonathan/scripts/daily_raw_update.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
