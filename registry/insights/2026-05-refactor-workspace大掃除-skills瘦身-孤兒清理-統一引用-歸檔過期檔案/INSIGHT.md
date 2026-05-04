---
{
  "title": "refactor: workspace大掃除 - skills瘦身/孤兒清理/統一引用/歸檔過期檔案",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `ab1788a35d85`: refactor: workspace大掃除 - skills瘦身/孤兒清理/統一引用/歸檔過期檔案",
  "prevention_signal": "Before modifying `research/scripts/feedback_inject.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"ab1788a35d853a1ac053c3559b775f48e5ec9a8d\",\n  \"files\": [\n    \"jonathan/IDENTITY.md\",\n    \"jonathan/archive/.analysis_2026-03-09.md\",\n    \"jonathan/archive/THREADS_REPLY_FIX.md\",\n    \"jonathan/archive/auto_learning_log.md\",\n    \"jonathan/archive/memory-old/2026-03-11.md\",\n    \"jonathan/archive/memory-old/2026-03-13.md\",\n    \"jonathan/archive/memory-old/2026-03-16.md\",\n    \"jonathan/archive/style_memory.md\",\n    \"jonathan/archive/threads-scout-old/CRITICAL_BUG.md\",\n    \"jonathan/archive/threads-scout-old/FORMAT_CHECKLIST.md\",\n    \"jonathan/archive/threads-scout-old/INTEGRATION_UPDATE.md\",\n    \"jonathan/archive/threads-scout-old/reply_tracker.md\",\n    \"jonathan/memory/2026-03-11.md\",\n    \"jonathan/skills/betalpha-content/SKILL.md\",\n    \"jonathan/skills/betalpha-content/references/content_clusters.md\",\n    \"jonathan/skills/betalpha-images/SKILL.md\",\n    \"jonathan/skills/brand-guidelines/SKILL.md\",\n    \"jonathan/skills/threads-ideation/SKILL.md\",\n    \"jonathan/skills/threads-ideation/references/algorithm_guide.md\",\n    \"jonathan/skills/threads-scout/SKILL.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: research/scripts/feedback_inject.py, research/scripts/feedback_record.py, research/skills/portfolio-alpha/data/feedback_log.jsonl\",\n    \"large change set: 45 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/scripts/feedback_inject.py` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "ab1788a35d853a1ac053c3559b775f48e5ec9a8d",
    "date": "2026-03-17T16:27:51+08:00",
    "files": [
      "jonathan/IDENTITY.md",
      "jonathan/archive/.analysis_2026-03-09.md",
      "jonathan/archive/THREADS_REPLY_FIX.md",
      "jonathan/archive/auto_learning_log.md",
      "jonathan/archive/memory-old/2026-03-11.md",
      "jonathan/archive/memory-old/2026-03-13.md",
      "jonathan/archive/memory-old/2026-03-16.md",
      "jonathan/archive/style_memory.md",
      "jonathan/archive/threads-scout-old/CRITICAL_BUG.md",
      "jonathan/archive/threads-scout-old/FORMAT_CHECKLIST.md",
      "jonathan/archive/threads-scout-old/INTEGRATION_UPDATE.md",
      "jonathan/archive/threads-scout-old/reply_tracker.md",
      "jonathan/memory/2026-03-11.md",
      "jonathan/skills/betalpha-content/SKILL.md",
      "jonathan/skills/betalpha-content/references/content_clusters.md",
      "jonathan/skills/betalpha-images/SKILL.md",
      "jonathan/skills/brand-guidelines/SKILL.md",
      "jonathan/skills/threads-ideation/SKILL.md",
      "jonathan/skills/threads-ideation/references/algorithm_guide.md",
      "jonathan/skills/threads-scout/SKILL.md",
      "jonathan/skills/threads-scout/auto_learning_log.md",
      "jonathan/skills/threads-scout/data/recommended_posts.md",
      "jonathan/skills/threads-scout/keywords.md",
      "jonathan/skills/threads-scout/recommended_posts.md",
      "jonathan/skills/threads-scout/temp_analysis.md",
      "research-agent/reviewer-learnings.md",
      "research/data/corrections_tracker_state.json",
      "research/data/pattern_tracker.json",
      "research/data/pipeline_events.jsonl",
      "research/memory/2026-03-17.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: refactor: workspace大掃除 - skills瘦身/孤兒清理/統一引用/歸檔過期檔案

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch ab1788a35d853a1ac053c3559b775f48e5ec9a8d

## Evidence

{
  "commit": "ab1788a35d853a1ac053c3559b775f48e5ec9a8d",
  "files": [
    "jonathan/IDENTITY.md",
    "jonathan/archive/.analysis_2026-03-09.md",
    "jonathan/archive/THREADS_REPLY_FIX.md",
    "jonathan/archive/auto_learning_log.md",
    "jonathan/archive/memory-old/2026-03-11.md",
    "jonathan/archive/memory-old/2026-03-13.md",
    "jonathan/archive/memory-old/2026-03-16.md",
    "jonathan/archive/style_memory.md",
    "jonathan/archive/threads-scout-old/CRITICAL_BUG.md",
    "jonathan/archive/threads-scout-old/FORMAT_CHECKLIST.md",
    "jonathan/archive/threads-scout-old/INTEGRATION_UPDATE.md",
    "jonathan/archive/threads-scout-old/reply_tracker.md",
    "jonathan/memory/2026-03-11.md",
    "jonathan/skills/betalpha-content/SKILL.md",
    "jonathan/skills/betalpha-content/references/content_clusters.md",
    "jonathan/skills/betalpha-images/SKILL.md",
    "jonathan/skills/brand-guidelines/SKILL.md",
    "jonathan/skills/threads-ideation/SKILL.md",
    "jonathan/skills/threads-ideation/references/algorithm_guide.md",
    "jonathan/skills/threads-scout/SKILL.md"
  ],
  "reasons": [
    "touches risky subsystem: research/scripts/feedback_inject.py, research/scripts/feedback_record.py, research/skills/portfolio-alpha/data/feedback_log.jsonl",
    "large change set: 45 files"
  ]
}
