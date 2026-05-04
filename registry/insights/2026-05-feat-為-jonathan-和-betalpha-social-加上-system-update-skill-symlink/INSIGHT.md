---
{
  "title": "feat: 為 jonathan 和 betalpha-social 加上 system-update skill (symlink)",
  "type": "spec_guardrail",
  "tags": [
    "schema"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `dba784c2496e`: feat: 為 jonathan 和 betalpha-social 加上 system-update skill (symlink)",
  "prevention_signal": "Before modifying `betalpha-social/skills/system-update` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"dba784c2496e4c53a9ac95c6dc656af2d1464f4f\",\n  \"files\": [\n    \"betalpha-social/skills/system-update\",\n    \"jonathan/skills/system-update\",\n    \"research/memory/MEMORY.md\",\n    \"research/vault/_meta/link_suggestions.md\",\n    \"research/vault/_meta/orphans.md\",\n    \"research/vault/_meta/skill_versions.md\",\n    \"research/vault/meta/agent-channel-permissions-v1.md\",\n    \"research/vault/meta/agent-communication-mvp-v1.md\",\n    \"research/vault/meta/agent-organization-v1.md\",\n    \"research/vault/meta/auto-research-thread-2026-03-12.md\",\n    \"research/vault/meta/meeting-protocol-v1.md\",\n    \"research/vault/meta/meeting-room-spec-v1.md\",\n    \"research/vault/meta/multiagent-compare-spec-v1.md\",\n    \"research/vault/meta/scout-pipeline-ready-status.md\",\n    \"research/vault/meta/shadow_handoff_schema.md\",\n    \"research/vault/news/2026-03-13.md\",\n    \"research/vault/news/2026-03-14.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/skills/system-update, research/vault/meta/shadow_handoff_schema.md\",\n    \"large change set: 17 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/skills/system-update` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "dba784c2496e4c53a9ac95c6dc656af2d1464f4f",
    "date": "2026-03-14T23:35:48+08:00",
    "files": [
      "betalpha-social/skills/system-update",
      "jonathan/skills/system-update",
      "research/memory/MEMORY.md",
      "research/vault/_meta/link_suggestions.md",
      "research/vault/_meta/orphans.md",
      "research/vault/_meta/skill_versions.md",
      "research/vault/meta/agent-channel-permissions-v1.md",
      "research/vault/meta/agent-communication-mvp-v1.md",
      "research/vault/meta/agent-organization-v1.md",
      "research/vault/meta/auto-research-thread-2026-03-12.md",
      "research/vault/meta/meeting-protocol-v1.md",
      "research/vault/meta/meeting-room-spec-v1.md",
      "research/vault/meta/multiagent-compare-spec-v1.md",
      "research/vault/meta/scout-pipeline-ready-status.md",
      "research/vault/meta/shadow_handoff_schema.md",
      "research/vault/news/2026-03-13.md",
      "research/vault/news/2026-03-14.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: feat: 為 jonathan 和 betalpha-social 加上 system-update skill (symlink)

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch dba784c2496e4c53a9ac95c6dc656af2d1464f4f

## Evidence

{
  "commit": "dba784c2496e4c53a9ac95c6dc656af2d1464f4f",
  "files": [
    "betalpha-social/skills/system-update",
    "jonathan/skills/system-update",
    "research/memory/MEMORY.md",
    "research/vault/_meta/link_suggestions.md",
    "research/vault/_meta/orphans.md",
    "research/vault/_meta/skill_versions.md",
    "research/vault/meta/agent-channel-permissions-v1.md",
    "research/vault/meta/agent-communication-mvp-v1.md",
    "research/vault/meta/agent-organization-v1.md",
    "research/vault/meta/auto-research-thread-2026-03-12.md",
    "research/vault/meta/meeting-protocol-v1.md",
    "research/vault/meta/meeting-room-spec-v1.md",
    "research/vault/meta/multiagent-compare-spec-v1.md",
    "research/vault/meta/scout-pipeline-ready-status.md",
    "research/vault/meta/shadow_handoff_schema.md",
    "research/vault/news/2026-03-13.md",
    "research/vault/news/2026-03-14.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/skills/system-update, research/vault/meta/shadow_handoff_schema.md",
    "large change set: 17 files"
  ]
}
