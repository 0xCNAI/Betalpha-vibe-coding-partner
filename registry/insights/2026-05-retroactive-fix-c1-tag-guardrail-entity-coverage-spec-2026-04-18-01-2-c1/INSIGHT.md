---
{
  "title": "(retroactive) fix: C1 tag guardrail entity coverage (SPEC-2026-04-18-01 §2 C1)",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `d2826846341c`: (retroactive) fix: C1 tag guardrail entity coverage (SPEC-2026-04-18-01 §2 C1)",
  "prevention_signal": "Before modifying `tino/skills/news-filter/maps.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"d2826846341c98ce5099434ea4113699297f2376\",\n  \"files\": [\n    \"tino/skills/news-filter/maps.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `tino/skills/news-filter/maps.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "d2826846341c98ce5099434ea4113699297f2376",
    "date": "2026-04-18T16:38:32+08:00",
    "files": [
      "tino/skills/news-filter/maps.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: (retroactive) fix: C1 tag guardrail entity coverage (SPEC-2026-04-18-01 §2 C1)

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch d2826846341c98ce5099434ea4113699297f2376

## Evidence

{
  "commit": "d2826846341c98ce5099434ea4113699297f2376",
  "files": [
    "tino/skills/news-filter/maps.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
