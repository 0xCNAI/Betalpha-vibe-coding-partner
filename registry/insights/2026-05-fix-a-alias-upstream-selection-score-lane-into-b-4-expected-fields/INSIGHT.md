---
{
  "title": "fix(A): alias upstream selection_score/lane into B-4 expected fields",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `7f9f3f7138fc`: fix(A): alias upstream selection_score/lane into B-4 expected fields",
  "prevention_signal": "Before modifying `jonathan/scripts/daily_raw_update.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"7f9f3f7138fca655c2db992f4766567d47eba9cb\",\n  \"files\": [\n    \"jonathan/scripts/daily_raw_update.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/scripts/daily_raw_update.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "7f9f3f7138fca655c2db992f4766567d47eba9cb",
    "date": "2026-04-17T17:06:57+08:00",
    "files": [
      "jonathan/scripts/daily_raw_update.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix(A): alias upstream selection_score/lane into B-4 expected fields

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 7f9f3f7138fca655c2db992f4766567d47eba9cb

## Evidence

{
  "commit": "7f9f3f7138fca655c2db992f4766567d47eba9cb",
  "files": [
    "jonathan/scripts/daily_raw_update.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
