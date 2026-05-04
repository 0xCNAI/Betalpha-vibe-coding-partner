---
{
  "title": "fix: gitignore 補 .env.* + preflight secret 檢測加強",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `435641baaa4d`: fix: gitignore 補 .env.* + preflight secret 檢測加強",
  "prevention_signal": "Before modifying `.gitignore` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"435641baaa4d3a0f154d9c86641c552d08d106a9\",\n  \"files\": [\n    \".gitignore\",\n    \"research/skills/system-update/scripts/preflight.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `.gitignore` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "435641baaa4d3a0f154d9c86641c552d08d106a9",
    "date": "2026-03-14T23:29:04+08:00",
    "files": [
      ".gitignore",
      "research/skills/system-update/scripts/preflight.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: gitignore 補 .env.* + preflight secret 檢測加強

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 435641baaa4d3a0f154d9c86641c552d08d106a9

## Evidence

{
  "commit": "435641baaa4d3a0f154d9c86641c552d08d106a9",
  "files": [
    ".gitignore",
    "research/skills/system-update/scripts/preflight.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
