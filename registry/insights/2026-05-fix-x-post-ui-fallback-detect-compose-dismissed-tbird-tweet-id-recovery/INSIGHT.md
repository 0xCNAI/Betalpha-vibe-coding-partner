---
{
  "title": "fix: x_post UI fallback — detect compose_dismissed + tbird tweet_id recovery",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `c63bdd3672cd`: fix: x_post UI fallback — detect compose_dismissed + tbird tweet_id recovery",
  "prevention_signal": "Before modifying `research/scripts/x_post_api.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"c63bdd3672cd98c8d1397c82661606fc17db6b03\",\n  \"files\": [\n    \"research/scripts/x_post_api.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/scripts/x_post_api.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "c63bdd3672cd98c8d1397c82661606fc17db6b03",
    "date": "2026-03-28T10:59:20+08:00",
    "files": [
      "research/scripts/x_post_api.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: x_post UI fallback — detect compose_dismissed + tbird tweet_id recovery

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch c63bdd3672cd98c8d1397c82661606fc17db6b03

## Evidence

{
  "commit": "c63bdd3672cd98c8d1397c82661606fc17db6b03",
  "files": [
    "research/scripts/x_post_api.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
