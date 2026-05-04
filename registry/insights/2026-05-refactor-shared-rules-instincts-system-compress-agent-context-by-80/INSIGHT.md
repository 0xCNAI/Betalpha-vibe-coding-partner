---
{
  "title": "refactor: shared rules + instincts system, compress agent context by ~80%",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `80cac6a1316d`: refactor: shared rules + instincts system, compress agent context by ~80%",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"80cac6a1316d62d0f737041f303c47ddb6093b28\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/MEMORY.md\",\n    \"betalpha-social/TOOLS.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/rules-shared\",\n    \"betalpha-social/skills/threads-post-publish/SKILL.md\",\n    \"betalpha-social/skills/threads-verify/SKILL.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/MEMORY.md\",\n    \"jonathan/TOOLS.md\",\n    \"jonathan/rules-shared\",\n    \"jonathan/skills/betalpha-writer/style_memory.md\",\n    \"shared/instincts/active.md\",\n    \"shared/instincts/graduated.md\",\n    \"shared/rules/algorithm-check.md\",\n    \"shared/rules/image-standards.md\",\n    \"shared/rules/publishing-checklist.md\",\n    \"shared/rules/skill-security.md\",\n    \"shared/rules/threads-api.md\",\n    \"shared/rules/writing-style.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/TOOLS.md, betalpha-social/learning/LESSONS.md\",\n    \"large change set: 20 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "80cac6a1316d62d0f737041f303c47ddb6093b28",
    "date": "2026-03-24T17:24:32+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "betalpha-social/MEMORY.md",
      "betalpha-social/TOOLS.md",
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/rules-shared",
      "betalpha-social/skills/threads-post-publish/SKILL.md",
      "betalpha-social/skills/threads-verify/SKILL.md",
      "jonathan/AGENTS.md",
      "jonathan/MEMORY.md",
      "jonathan/TOOLS.md",
      "jonathan/rules-shared",
      "jonathan/skills/betalpha-writer/style_memory.md",
      "shared/instincts/active.md",
      "shared/instincts/graduated.md",
      "shared/rules/algorithm-check.md",
      "shared/rules/image-standards.md",
      "shared/rules/publishing-checklist.md",
      "shared/rules/skill-security.md",
      "shared/rules/threads-api.md",
      "shared/rules/writing-style.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: refactor: shared rules + instincts system, compress agent context by ~80%

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 80cac6a1316d62d0f737041f303c47ddb6093b28

## Evidence

{
  "commit": "80cac6a1316d62d0f737041f303c47ddb6093b28",
  "files": [
    "betalpha-social/AGENTS.md",
    "betalpha-social/MEMORY.md",
    "betalpha-social/TOOLS.md",
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/rules-shared",
    "betalpha-social/skills/threads-post-publish/SKILL.md",
    "betalpha-social/skills/threads-verify/SKILL.md",
    "jonathan/AGENTS.md",
    "jonathan/MEMORY.md",
    "jonathan/TOOLS.md",
    "jonathan/rules-shared",
    "jonathan/skills/betalpha-writer/style_memory.md",
    "shared/instincts/active.md",
    "shared/instincts/graduated.md",
    "shared/rules/algorithm-check.md",
    "shared/rules/image-standards.md",
    "shared/rules/publishing-checklist.md",
    "shared/rules/skill-security.md",
    "shared/rules/threads-api.md",
    "shared/rules/writing-style.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/TOOLS.md, betalpha-social/learning/LESSONS.md",
    "large change set: 20 files"
  ]
}
