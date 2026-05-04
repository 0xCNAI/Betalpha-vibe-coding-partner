---
{
  "title": "Fix Threads Scout engagement parsing",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `53ff34b947df`: Fix Threads Scout engagement parsing",
  "prevention_signal": "Before modifying `jonathan/memory/2026-04-27.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"53ff34b947dfbee2bed27f1b7630fc204c420c45\",\n  \"files\": [\n    \"jonathan/memory/2026-04-27.md\",\n    \"jonathan/scripts/threads_scout_file_relay.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/memory/2026-04-27.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "53ff34b947dfbee2bed27f1b7630fc204c420c45",
    "date": "2026-04-27T12:59:32+08:00",
    "files": [
      "jonathan/memory/2026-04-27.md",
      "jonathan/scripts/threads_scout_file_relay.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: Fix Threads Scout engagement parsing

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 53ff34b947dfbee2bed27f1b7630fc204c420c45

## Evidence

{
  "commit": "53ff34b947dfbee2bed27f1b7630fc204c420c45",
  "files": [
    "jonathan/memory/2026-04-27.md",
    "jonathan/scripts/threads_scout_file_relay.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
