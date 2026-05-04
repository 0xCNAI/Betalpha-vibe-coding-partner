---
{
  "title": "diversified curation: cron prompts + tasks completion",
  "type": "spec_guardrail",
  "tags": [
    "cron",
    "migration",
    "schema",
    "test"
  ],
  "tech_stack": [
    "node",
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `fb7db32d4a26`: diversified curation: cron prompts + tasks completion",
  "prevention_signal": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"fb7db32d4a26978c99a39edecc38f749e54cb9bb\",\n  \"files\": [\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/HEARTBEAT.md\",\n    \"betalpha-social/MEMORY.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-26.md\",\n    \"betalpha-social/memory/corrections.md\",\n    \"\\\"betalpha-social/post_history/2026-03-25_instagram_Circle_\\\\350\\\\202\\\\241\\\\345\\\\203\\\\271\\\\346\\\\232\\\\264\\\\350\\\\267\\\\214_\\\\347\\\\251\\\\251\\\\345\\\\256\\\\232\\\\345\\\\271\\\\243\\\\346\\\\262\\\\222\\\\346\\\\255\\\\273.md\\\"\",\n    \"betalpha-social/post_history/2026-03-25_threads_Circle_Clarity_Act.md\",\n    \"\\\"betalpha-social/post_history/2026-03-25_threads_Resolv_\\\\345\\\\243\\\\236\\\\345\\\\270\\\\263\\\\345\\\\204\\\\237\\\\351\\\\202\\\\204\\\\351\\\\200\\\\262\\\\345\\\\272\\\\246.md\\\"\",\n    \"betalpha-social/skills/session-hygiene/SKILL.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/MEMORY.md\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/data/daily_review_proposals/2026-03-26.md\",\n    \"jonathan/skills/betalpha-writer/writing_style.md\",\n    \"jonathan/skills/daily-review/SKILL.md\",\n    \"jonathan/skills/daily-review/data/learning_report_2026-03-26.md\",\n    \"jonathan/skills/daily-review/data/recommendations_2026-03-26.json\",\n    \"jonathan/skills/daily-review/data/recommendations_2026-03-26.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/HEARTBEAT.md, betalpha-social/MEMORY.md, betalpha-social/learning/LESSONS.md\",\n    \"large change set: 1288 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/AGENTS.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron",
      "migration",
      "schema",
      "test"
    ],
    "tech_stack": [
      "node",
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
    "sha": "fb7db32d4a26978c99a39edecc38f749e54cb9bb",
    "date": "2026-03-26T18:03:44+08:00",
    "files": [
      "betalpha-social/AGENTS.md",
      "betalpha-social/HEARTBEAT.md",
      "betalpha-social/MEMORY.md",
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-26.md",
      "betalpha-social/memory/corrections.md",
      "\"betalpha-social/post_history/2026-03-25_instagram_Circle_\\350\\202\\241\\345\\203\\271\\346\\232\\264\\350\\267\\214_\\347\\251\\251\\345\\256\\232\\345\\271\\243\\346\\262\\222\\346\\255\\273.md\"",
      "betalpha-social/post_history/2026-03-25_threads_Circle_Clarity_Act.md",
      "\"betalpha-social/post_history/2026-03-25_threads_Resolv_\\345\\243\\236\\345\\270\\263\\345\\204\\237\\351\\202\\204\\351\\200\\262\\345\\272\\246.md\"",
      "betalpha-social/skills/session-hygiene/SKILL.md",
      "jonathan/AGENTS.md",
      "jonathan/MEMORY.md",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/data/daily_review_proposals/2026-03-26.md",
      "jonathan/skills/betalpha-writer/writing_style.md",
      "jonathan/skills/daily-review/SKILL.md",
      "jonathan/skills/daily-review/data/learning_report_2026-03-26.md",
      "jonathan/skills/daily-review/data/recommendations_2026-03-26.json",
      "jonathan/skills/daily-review/data/recommendations_2026-03-26.md",
      "jonathan/skills/daily-review/data/sessions_2026-03-26.json",
      "jonathan/skills/daily-review/scripts/classify_sessions.py",
      "jonathan/skills/daily-review/scripts/extract_learnings.py",
      "jonathan/skills/instagram-image-maker/SKILL.md",
      "jonathan/skills/instagram-writer/SKILL.md",
      "jonathan/skills/threads-scout/data/current_recommendations.md",
      "jonathan/skills/threads-scout/data/keywords.md",
      "jonathan/skills/threads-scout/data/recommended_history.md",
      "publish/AGENTS.md",
      "publish/memory/2026-03-26.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: diversified curation: cron prompts + tasks completion

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch fb7db32d4a26978c99a39edecc38f749e54cb9bb

## Evidence

{
  "commit": "fb7db32d4a26978c99a39edecc38f749e54cb9bb",
  "files": [
    "betalpha-social/AGENTS.md",
    "betalpha-social/HEARTBEAT.md",
    "betalpha-social/MEMORY.md",
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-26.md",
    "betalpha-social/memory/corrections.md",
    "\"betalpha-social/post_history/2026-03-25_instagram_Circle_\\350\\202\\241\\345\\203\\271\\346\\232\\264\\350\\267\\214_\\347\\251\\251\\345\\256\\232\\345\\271\\243\\346\\262\\222\\346\\255\\273.md\"",
    "betalpha-social/post_history/2026-03-25_threads_Circle_Clarity_Act.md",
    "\"betalpha-social/post_history/2026-03-25_threads_Resolv_\\345\\243\\236\\345\\270\\263\\345\\204\\237\\351\\202\\204\\351\\200\\262\\345\\272\\246.md\"",
    "betalpha-social/skills/session-hygiene/SKILL.md",
    "jonathan/AGENTS.md",
    "jonathan/MEMORY.md",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/data/daily_review_proposals/2026-03-26.md",
    "jonathan/skills/betalpha-writer/writing_style.md",
    "jonathan/skills/daily-review/SKILL.md",
    "jonathan/skills/daily-review/data/learning_report_2026-03-26.md",
    "jonathan/skills/daily-review/data/recommendations_2026-03-26.json",
    "jonathan/skills/daily-review/data/recommendations_2026-03-26.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/AGENTS.md, betalpha-social/HEARTBEAT.md, betalpha-social/MEMORY.md, betalpha-social/learning/LESSONS.md",
    "large change set: 1288 files"
  ]
}
