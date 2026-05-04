---
{
  "title": "fix: remove hardcoded channel mention from manual-relay output template",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `9cf33272dc85`: fix: remove hardcoded channel mention from manual-relay output template",
  "prevention_signal": "Before modifying `publish/skills/manual-relay/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"9cf33272dc85aa2af721104681649f4807fcb1aa\",\n  \"files\": [\n    \"publish/skills/manual-relay/SKILL.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `publish/skills/manual-relay/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "9cf33272dc85aa2af721104681649f4807fcb1aa",
    "date": "2026-03-22T17:07:24+08:00",
    "files": [
      "publish/skills/manual-relay/SKILL.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: remove hardcoded channel mention from manual-relay output template

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 9cf33272dc85aa2af721104681649f4807fcb1aa

## Evidence

{
  "commit": "9cf33272dc85aa2af721104681649f4807fcb1aa",
  "files": [
    "publish/skills/manual-relay/SKILL.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
