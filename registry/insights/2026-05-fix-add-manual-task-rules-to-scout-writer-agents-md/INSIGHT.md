---
{
  "title": "fix: add manual task rules to Scout + Writer AGENTS.md",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [],
  "summary": "Git history candidate from `clawd` commit `9dfa9ddbd27c`: fix: add manual task rules to Scout + Writer AGENTS.md",
  "prevention_signal": "Before modifying `social-agent/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"9dfa9ddbd27cb318f9a072e9abd70854f35f9e93\",\n  \"files\": [\n    \"publish/AGENTS.md\",\n    \"social-agent/AGENTS.md\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: social-agent/AGENTS.md\"\n  ]\n}",
  "transferable_pattern": "Before modifying `social-agent/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "9dfa9ddbd27cb318f9a072e9abd70854f35f9e93",
    "date": "2026-03-22T16:20:12+08:00",
    "files": [
      "publish/AGENTS.md",
      "social-agent/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: add manual task rules to Scout + Writer AGENTS.md

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 9dfa9ddbd27cb318f9a072e9abd70854f35f9e93

## Evidence

{
  "commit": "9dfa9ddbd27cb318f9a072e9abd70854f35f9e93",
  "files": [
    "publish/AGENTS.md",
    "social-agent/AGENTS.md"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: social-agent/AGENTS.md"
  ]
}
