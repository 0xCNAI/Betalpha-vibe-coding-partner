---
{
  "title": "fix(instagram-image-maker): 底圖優先搜尋真實圖片 + 孤字防護擴大範圍",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `f86a9c3f619f`: fix(instagram-image-maker): 底圖優先搜尋真實圖片 + 孤字防護擴大範圍",
  "prevention_signal": "Before modifying `jonathan/skills/daily-review/data/learning_report_2026-03-24.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"f86a9c3f619f38e799229f11d19dc5d8cfeb8b37\",\n  \"files\": [\n    \"jonathan/skills/daily-review/data/learning_report_2026-03-24.md\",\n    \"jonathan/skills/daily-review/data/proposals_2026-03-24.json\",\n    \"jonathan/skills/daily-review/data/proposals_2026-03-24.md\",\n    \"jonathan/skills/daily-review/data/sessions_2026-03-24.json\",\n    \"jonathan/skills/instagram-image-maker/SKILL.md\",\n    \"\\\"jonathan/skills/instagram-image-maker/\\\\345\\\\272\\\\225\\\\345\\\\234\\\\226\\\\350\\\\250\\\\255\\\\350\\\\250\\\\210_checklist.md\\\"\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/skills/daily-review/data/learning_report_2026-03-24.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "f86a9c3f619f38e799229f11d19dc5d8cfeb8b37",
    "date": "2026-03-24T23:03:45+08:00",
    "files": [
      "jonathan/skills/daily-review/data/learning_report_2026-03-24.md",
      "jonathan/skills/daily-review/data/proposals_2026-03-24.json",
      "jonathan/skills/daily-review/data/proposals_2026-03-24.md",
      "jonathan/skills/daily-review/data/sessions_2026-03-24.json",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "\"jonathan/skills/instagram-image-maker/\\345\\272\\225\\345\\234\\226\\350\\250\\255\\350\\250\\210_checklist.md\""
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix(instagram-image-maker): 底圖優先搜尋真實圖片 + 孤字防護擴大範圍

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch f86a9c3f619f38e799229f11d19dc5d8cfeb8b37

## Evidence

{
  "commit": "f86a9c3f619f38e799229f11d19dc5d8cfeb8b37",
  "files": [
    "jonathan/skills/daily-review/data/learning_report_2026-03-24.md",
    "jonathan/skills/daily-review/data/proposals_2026-03-24.json",
    "jonathan/skills/daily-review/data/proposals_2026-03-24.md",
    "jonathan/skills/daily-review/data/sessions_2026-03-24.json",
    "jonathan/skills/instagram-image-maker/SKILL.md",
    "\"jonathan/skills/instagram-image-maker/\\345\\272\\225\\345\\234\\226\\350\\250\\255\\350\\250\\210_checklist.md\""
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
