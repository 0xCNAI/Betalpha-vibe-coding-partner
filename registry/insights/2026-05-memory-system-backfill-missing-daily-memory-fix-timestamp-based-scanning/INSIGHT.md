---
{
  "title": "memory system: backfill missing daily memory + fix timestamp-based scanning",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `564638790560`: memory system: backfill missing daily memory + fix timestamp-based scanning",
  "prevention_signal": "Before modifying `research/scripts/memory_backfill.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"564638790560d3b23ea175570415ad1c351984e1\",\n  \"files\": [\n    \"research/scripts/memory_backfill.py\",\n    \"research/scripts/memory_nightly.py\",\n    \"research/scripts/thread_memory_candidates.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/scripts/memory_backfill.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "564638790560d3b23ea175570415ad1c351984e1",
    "date": "2026-03-26T13:52:47+08:00",
    "files": [
      "research/scripts/memory_backfill.py",
      "research/scripts/memory_nightly.py",
      "research/scripts/thread_memory_candidates.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: memory system: backfill missing daily memory + fix timestamp-based scanning

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 564638790560d3b23ea175570415ad1c351984e1

## Evidence

{
  "commit": "564638790560d3b23ea175570415ad1c351984e1",
  "files": [
    "research/scripts/memory_backfill.py",
    "research/scripts/memory_nightly.py",
    "research/scripts/thread_memory_candidates.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
