---
{
  "title": "feat: add Discord thread workflow + daily-review skill, migrate social agent from Telegram",
  "type": "spec_guardrail",
  "tags": [
    "ci"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `031216f54a7f`: feat: add Discord thread workflow + daily-review skill, migrate social agent from Telegram to Discord",
  "prevention_signal": "Before modifying `betalpha-social/.skill_review_2026-03-09.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"031216f54a7f70614d6bf6b0846a61dd271d8bb4\",\n  \"files\": [\n    \"betalpha-social/.skill_review_2026-03-09.md\",\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/MEMORY.md\",\n    \"betalpha-social/SKILLS_INDEX.md\",\n    \"betalpha-social/TOOLS.md\",\n    \"betalpha-social/learning/2026-03-09_thread_production_lessons.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/skills/daily-review/SKILL.md\",\n    \"jonathan/skills/threads-scout/data/recommended_posts.md\",\n    \"research-agent/AGENTS.md\",\n    \"research-agent/memory/2026-03-16-baseline.md\",\n    \"research-agent/reviewer-learnings.md\",\n    \"research/AGENTS.md\",\n    \"research/data/pending_rule_proposals.jsonl\",\n    \"research/data/rule_verdicts.jsonl\",\n    \"research/learning/patterns.md\",\n    \"research/memory/2026-03-16-thread-archive.md\",\n    \"research/scripts/deep_dive_review.py\",\n    \"research/scripts/session_maintenance.py\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/.skill_review_2026-03-09.md, betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/SKILLS_INDEX.md\",\n    \"large change set: 26 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/.skill_review_2026-03-09.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "ci"
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
    "sha": "031216f54a7f70614d6bf6b0846a61dd271d8bb4",
    "date": "2026-03-16T16:31:24+08:00",
    "files": [
      "betalpha-social/.skill_review_2026-03-09.md",
      "betalpha-social/AGENTS.md",
      "betalpha-social/MEMORY.md",
      "betalpha-social/SKILLS_INDEX.md",
      "betalpha-social/TOOLS.md",
      "betalpha-social/learning/2026-03-09_thread_production_lessons.md",
      "betalpha-social/learning/LESSONS.md",
      "jonathan/AGENTS.md",
      "jonathan/skills/daily-review/SKILL.md",
      "jonathan/skills/threads-scout/data/recommended_posts.md",
      "research-agent/AGENTS.md",
      "research-agent/memory/2026-03-16-baseline.md",
      "research-agent/reviewer-learnings.md",
      "research/AGENTS.md",
      "research/data/pending_rule_proposals.jsonl",
      "research/data/rule_verdicts.jsonl",
      "research/learning/patterns.md",
      "research/memory/2026-03-16-thread-archive.md",
      "research/scripts/deep_dive_review.py",
      "research/scripts/session_maintenance.py",
      "research/skills/flash-news/flash_result_formatter.py",
      "research/skills/flash-news/publish_log.json",
      "research/skills/portfolio-alpha/data/auto_evolve_log.jsonl",
      "research/skills/portfolio-alpha/data/feedback_log.jsonl",
      "research/skills/portfolio-alpha/references/writer-rules.md",
      "social-agent/memory/2026-03-16.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: feat: add Discord thread workflow + daily-review skill, migrate social agent from Telegram to Discord

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 031216f54a7f70614d6bf6b0846a61dd271d8bb4

## Evidence

{
  "commit": "031216f54a7f70614d6bf6b0846a61dd271d8bb4",
  "files": [
    "betalpha-social/.skill_review_2026-03-09.md",
    "betalpha-social/AGENTS.md",
    "betalpha-social/MEMORY.md",
    "betalpha-social/SKILLS_INDEX.md",
    "betalpha-social/TOOLS.md",
    "betalpha-social/learning/2026-03-09_thread_production_lessons.md",
    "betalpha-social/learning/LESSONS.md",
    "jonathan/AGENTS.md",
    "jonathan/skills/daily-review/SKILL.md",
    "jonathan/skills/threads-scout/data/recommended_posts.md",
    "research-agent/AGENTS.md",
    "research-agent/memory/2026-03-16-baseline.md",
    "research-agent/reviewer-learnings.md",
    "research/AGENTS.md",
    "research/data/pending_rule_proposals.jsonl",
    "research/data/rule_verdicts.jsonl",
    "research/learning/patterns.md",
    "research/memory/2026-03-16-thread-archive.md",
    "research/scripts/deep_dive_review.py",
    "research/scripts/session_maintenance.py"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/.skill_review_2026-03-09.md, betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/SKILLS_INDEX.md",
    "large change set: 26 files"
  ]
}
