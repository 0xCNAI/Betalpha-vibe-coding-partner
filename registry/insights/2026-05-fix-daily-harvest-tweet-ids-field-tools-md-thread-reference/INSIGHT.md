---
{
  "title": "fix: daily harvest tweet_ids field + TOOLS.md thread reference",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `e4b09cec53a2`: fix: daily harvest tweet_ids field + TOOLS.md thread reference",
  "prevention_signal": "Before modifying `research/TOOLS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"e4b09cec53a200aa9759b1d9af5aac8ca6387ae2\",\n  \"files\": [\n    \"research/TOOLS.md\",\n    \"research/vault/meta/data/tweet_tracker.json\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/TOOLS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "e4b09cec53a200aa9759b1d9af5aac8ca6387ae2",
    "date": "2026-03-17T11:47:29+08:00",
    "files": [
      "research/TOOLS.md",
      "research/vault/meta/data/tweet_tracker.json"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: daily harvest tweet_ids field + TOOLS.md thread reference

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch e4b09cec53a200aa9759b1d9af5aac8ca6387ae2

## Evidence

{
  "commit": "e4b09cec53a200aa9759b1d9af5aac8ca6387ae2",
  "files": [
    "research/TOOLS.md",
    "research/vault/meta/data/tweet_tracker.json"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
