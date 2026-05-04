---
{
  "title": "Upgrade Threads current recommendation schema",
  "type": "pitfall",
  "tags": [
    "schema"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `1ce5aecd043d`: Upgrade Threads current recommendation schema",
  "prevention_signal": "Before modifying `jonathan/skills/threads-scout/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"1ce5aecd043de44b15d0465fad562572d4bf9689\",\n  \"files\": [\n    \"jonathan/skills/threads-scout/SKILL.md\",\n    \"jonathan/skills/threads-scout/data/current_recommendations.md\",\n    \"jonathan/skills/threads-scout/references/v2-prompt.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/skills/threads-scout/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "schema"
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
    "sha": "1ce5aecd043de44b15d0465fad562572d4bf9689",
    "date": "2026-04-24T15:12:20+08:00",
    "files": [
      "jonathan/skills/threads-scout/SKILL.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/references/v2-prompt.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: Upgrade Threads current recommendation schema

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 1ce5aecd043de44b15d0465fad562572d4bf9689

## Evidence

{
  "commit": "1ce5aecd043de44b15d0465fad562572d4bf9689",
  "files": [
    "jonathan/skills/threads-scout/SKILL.md",
    "jonathan/skills/threads-scout/data/current_recommendations.md",
    "jonathan/skills/threads-scout/references/v2-prompt.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
