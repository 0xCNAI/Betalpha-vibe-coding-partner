---
{
  "title": "fix: manual-relay auto-triggers Writer→Reviewer via cron tool",
  "type": "pitfall",
  "tags": [
    "cron"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `2c9377bf8085`: fix: manual-relay auto-triggers Writer→Reviewer via cron tool",
  "prevention_signal": "Before modifying `publish/skills/manual-relay/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"2c9377bf8085da85e1dfc6fe6e523aca52717128\",\n  \"files\": [\n    \"publish/skills/manual-relay/SKILL.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `publish/skills/manual-relay/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron"
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
    "sha": "2c9377bf8085da85e1dfc6fe6e523aca52717128",
    "date": "2026-03-22T16:54:57+08:00",
    "files": [
      "publish/skills/manual-relay/SKILL.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: manual-relay auto-triggers Writer→Reviewer via cron tool

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 2c9377bf8085da85e1dfc6fe6e523aca52717128

## Evidence

{
  "commit": "2c9377bf8085da85e1dfc6fe6e523aca52717128",
  "files": [
    "publish/skills/manual-relay/SKILL.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
