---
{
  "title": "codex batch 2-3: shared lib, constants, test fixes, 237 tests all green",
  "type": "pitfall",
  "tags": [
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `796e35f57c4b`: codex batch 2-3: shared lib, constants, test fixes, 237 tests all green",
  "prevention_signal": "Before modifying `research/config/__init__.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"796e35f57c4b0f9dce91291401a6318baed7ebf6\",\n  \"files\": [\n    \"research/config/__init__.py\",\n    \"research/config/constants.py\",\n    \"research/config/podcasts.json\",\n    \"research/scripts/lib/__init__.py\",\n    \"research/scripts/lib/io.py\",\n    \"research/scripts/lib/tbird_cli.py\",\n    \"research/scripts/lib/timeutil.py\",\n    \"research/scripts/portfolio_report.py\",\n    \"research/tests/test_auto_evolve.py\",\n    \"research/tests/test_constants.py\",\n    \"research/tests/test_lib.py\"\n  ],\n  \"reasons\": [\n    \"commit message contains failure/fix signal\",\n    \"touches risky subsystem: research/config/__init__.py, research/config/constants.py, research/config/podcasts.json\",\n    \"large change set: 11 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/config/__init__.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "test"
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
    "sha": "796e35f57c4b0f9dce91291401a6318baed7ebf6",
    "date": "2026-03-20T17:12:47+08:00",
    "files": [
      "research/config/__init__.py",
      "research/config/constants.py",
      "research/config/podcasts.json",
      "research/scripts/lib/__init__.py",
      "research/scripts/lib/io.py",
      "research/scripts/lib/tbird_cli.py",
      "research/scripts/lib/timeutil.py",
      "research/scripts/portfolio_report.py",
      "research/tests/test_auto_evolve.py",
      "research/tests/test_constants.py",
      "research/tests/test_lib.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: codex batch 2-3: shared lib, constants, test fixes, 237 tests all green

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 796e35f57c4b0f9dce91291401a6318baed7ebf6

## Evidence

{
  "commit": "796e35f57c4b0f9dce91291401a6318baed7ebf6",
  "files": [
    "research/config/__init__.py",
    "research/config/constants.py",
    "research/config/podcasts.json",
    "research/scripts/lib/__init__.py",
    "research/scripts/lib/io.py",
    "research/scripts/lib/tbird_cli.py",
    "research/scripts/lib/timeutil.py",
    "research/scripts/portfolio_report.py",
    "research/tests/test_auto_evolve.py",
    "research/tests/test_constants.py",
    "research/tests/test_lib.py"
  ],
  "reasons": [
    "commit message contains failure/fix signal",
    "touches risky subsystem: research/config/__init__.py, research/config/constants.py, research/config/podcasts.json",
    "large change set: 11 files"
  ]
}
