---
{
  "title": "fix: 圖片傳送改用 MEDIA: 語法，修正所有 skill 中錯誤的 Read 工具用法",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `97319748293d`: fix: 圖片傳送改用 MEDIA: 語法，修正所有 skill 中錯誤的 Read 工具用法",
  "prevention_signal": "Before modifying `jonathan/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"97319748293dc0f9dbdecea8be785b75def9fbf6\",\n  \"files\": [\n    \"jonathan/AGENTS.md\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/skills/betalpha-images/SKILL.md\",\n    \"jonathan/skills/betalpha-images/image_templates.md\",\n    \"jonathan/skills/betalpha-screenshot/SKILL.md\",\n    \"research/scripts/factcheck_decay.py\",\n    \"research/skills/fact-check/SKILL.md\",\n    \"research/skills/research/SKILL.md\",\n    \"research/skills/research/references/thesis-checkpoint.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `jonathan/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "97319748293dc0f9dbdecea8be785b75def9fbf6",
    "date": "2026-03-16T17:18:35+08:00",
    "files": [
      "jonathan/AGENTS.md",
      "jonathan/TOOLS.md",
      "jonathan/skills/betalpha-images/SKILL.md",
      "jonathan/skills/betalpha-images/image_templates.md",
      "jonathan/skills/betalpha-screenshot/SKILL.md",
      "research/scripts/factcheck_decay.py",
      "research/skills/fact-check/SKILL.md",
      "research/skills/research/SKILL.md",
      "research/skills/research/references/thesis-checkpoint.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: 圖片傳送改用 MEDIA: 語法，修正所有 skill 中錯誤的 Read 工具用法

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 97319748293dc0f9dbdecea8be785b75def9fbf6

## Evidence

{
  "commit": "97319748293dc0f9dbdecea8be785b75def9fbf6",
  "files": [
    "jonathan/AGENTS.md",
    "jonathan/TOOLS.md",
    "jonathan/skills/betalpha-images/SKILL.md",
    "jonathan/skills/betalpha-images/image_templates.md",
    "jonathan/skills/betalpha-screenshot/SKILL.md",
    "research/scripts/factcheck_decay.py",
    "research/skills/fact-check/SKILL.md",
    "research/skills/research/SKILL.md",
    "research/skills/research/references/thesis-checkpoint.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
