---
{
  "title": "fix: Scout manual task rule → explicit skill pointer instead of inline flow",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `8ce0478bacfb`: fix: Scout manual task rule → explicit skill pointer instead of inline flow",
  "prevention_signal": "Before modifying `publish/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"8ce0478bacfb3cb113d207656bcb2eac393f77fa\",\n  \"files\": [\n    \"publish/AGENTS.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `publish/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "8ce0478bacfb3cb113d207656bcb2eac393f77fa",
    "date": "2026-03-22T16:36:00+08:00",
    "files": [
      "publish/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: Scout manual task rule → explicit skill pointer instead of inline flow

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 8ce0478bacfb3cb113d207656bcb2eac393f77fa

## Evidence

{
  "commit": "8ce0478bacfb3cb113d207656bcb2eac393f77fa",
  "files": [
    "publish/AGENTS.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
