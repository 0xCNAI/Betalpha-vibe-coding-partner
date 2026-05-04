---
{
  "title": "fix: manual-relay skill gotchas — enforce /tmp/ path, no sessions_send",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `947e4286851f`: fix: manual-relay skill gotchas — enforce /tmp/ path, no sessions_send",
  "prevention_signal": "Before modifying `publish/skills/manual-relay/SKILL.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"947e4286851ff4c33d13002bbcfa641d1a48109f\",\n  \"files\": [\n    \"publish/skills/manual-relay/SKILL.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
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
    "sha": "947e4286851ff4c33d13002bbcfa641d1a48109f",
    "date": "2026-03-22T16:52:04+08:00",
    "files": [
      "publish/skills/manual-relay/SKILL.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: manual-relay skill gotchas — enforce /tmp/ path, no sessions_send

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 947e4286851ff4c33d13002bbcfa641d1a48109f

## Evidence

{
  "commit": "947e4286851ff4c33d13002bbcfa641d1a48109f",
  "files": [
    "publish/skills/manual-relay/SKILL.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
