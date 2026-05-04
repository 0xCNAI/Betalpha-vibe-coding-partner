---
{
  "title": "fix: expand manual relay flow in Scout AGENTS.md with full instructions",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `615cd8ef2eda`: fix: expand manual relay flow in Scout AGENTS.md with full instructions",
  "prevention_signal": "Before modifying `publish/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"615cd8ef2edacaceae54dd2ff9f8ad3afcebaf46\",\n  \"files\": [\n    \"publish/AGENTS.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
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
    "sha": "615cd8ef2edacaceae54dd2ff9f8ad3afcebaf46",
    "date": "2026-03-22T16:30:43+08:00",
    "files": [
      "publish/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: expand manual relay flow in Scout AGENTS.md with full instructions

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 615cd8ef2edacaceae54dd2ff9f8ad3afcebaf46

## Evidence

{
  "commit": "615cd8ef2edacaceae54dd2ff9f8ad3afcebaf46",
  "files": [
    "publish/AGENTS.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
