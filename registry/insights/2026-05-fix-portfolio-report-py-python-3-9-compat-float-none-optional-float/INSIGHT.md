---
{
  "title": "fix: portfolio_report.py Python 3.9 compat (float|None → Optional[float])",
  "type": "pitfall",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `b0134ddd93e5`: fix: portfolio_report.py Python 3.9 compat (float|None → Optional[float])",
  "prevention_signal": "Before modifying `research/scripts/portfolio_report.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"b0134ddd93e548ed3fa4dd22ca8834ff13933b02\",\n  \"files\": [\n    \"research/scripts/portfolio_report.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/scripts/portfolio_report.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "b0134ddd93e548ed3fa4dd22ca8834ff13933b02",
    "date": "2026-03-20T19:01:30+08:00",
    "files": [
      "research/scripts/portfolio_report.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: fix: portfolio_report.py Python 3.9 compat (float|None → Optional[float])

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch b0134ddd93e548ed3fa4dd22ca8834ff13933b02

## Evidence

{
  "commit": "b0134ddd93e548ed3fa4dd22ca8834ff13933b02",
  "files": [
    "research/scripts/portfolio_report.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal"
  ]
}
