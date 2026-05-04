---
{
  "title": "memory cronjob consolidation: Phase 1-3",
  "type": "spec_guardrail",
  "tags": [
    "cron",
    "migration",
    "test"
  ],
  "tech_stack": [
    "node",
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `aafc7a0bb144`: memory cronjob consolidation: Phase 1-3",
  "prevention_signal": "Before modifying `betalpha-social/.clawhub/lock.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"aafc7a0bb14487767f7a1695ad3227d5d69a91ee\",\n  \"files\": [\n    \"betalpha-social/.clawhub/lock.json\",\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/MEMORY.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-24.md\",\n    \"betalpha-social/memory/2026-03-25.md\",\n    \"\\\"betalpha-social/memory/\\\\350\\\\236\\\\242\\\\345\\\\271\\\\225\\\\351\\\\214\\\\204\\\\345\\\\275\\\\261\\\\346\\\\226\\\\271\\\\346\\\\263\\\\225.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-24_instagram_Prediction_Market\\\\344\\\\272\\\\244\\\\346\\\\230\\\\223\\\\346\\\\211\\\\200\\\\346\\\\231\\\\202\\\\345\\\\210\\\\273.md\\\"\",\n    \"\\\"betalpha-social/post_history/2026-03-24_threads_BP\\\\347\\\\251\\\\272\\\\346\\\\212\\\\225_Mad_Lads.md\\\"\",\n    \"betalpha-social/recurring/weekly-watchlist/IMAGE_TEMPLATE.md\",\n    \"betalpha-social/recurring/weekly-watchlist/PLAN.md\",\n    \"betalpha-social/recurring/weekly-watchlist/QUICKSTART.md\",\n    \"betalpha-social/recurring/weekly-watchlist/week-00-TRIAL.md\",\n    \"betalpha-social/recurring/weekly-watchlist/week-01-DRAFT.md\",\n    \"betalpha-social/skills/pdf-to-structured/.clawhub/origin.json\",\n    \"betalpha-social/skills/pdf-to-structured/SKILL.md\",\n    \"betalpha-social/skills/pdf-to-structured/_meta.json\",\n    \"betalpha-social/skills/pdf-to-structured/claw.json\",\n    \"betalpha-social/skills/pdf-to-structured/instructions.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/.clawhub/lock.json, betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/learning/LESSONS.md\",\n    \"large change set: 1128 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/.clawhub/lock.json` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "cron",
      "migration",
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
    "sha": "aafc7a0bb14487767f7a1695ad3227d5d69a91ee",
    "date": "2026-03-25T22:25:05+08:00",
    "files": [
      "betalpha-social/.clawhub/lock.json",
      "betalpha-social/AGENTS.md",
      "betalpha-social/MEMORY.md",
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-24.md",
      "betalpha-social/memory/2026-03-25.md",
      "\"betalpha-social/memory/\\350\\236\\242\\345\\271\\225\\351\\214\\204\\345\\275\\261\\346\\226\\271\\346\\263\\225.md\"",
      "\"betalpha-social/post_history/2026-03-24_instagram_Prediction_Market\\344\\272\\244\\346\\230\\223\\346\\211\\200\\346\\231\\202\\345\\210\\273.md\"",
      "\"betalpha-social/post_history/2026-03-24_threads_BP\\347\\251\\272\\346\\212\\225_Mad_Lads.md\"",
      "betalpha-social/recurring/weekly-watchlist/IMAGE_TEMPLATE.md",
      "betalpha-social/recurring/weekly-watchlist/PLAN.md",
      "betalpha-social/recurring/weekly-watchlist/QUICKSTART.md",
      "betalpha-social/recurring/weekly-watchlist/week-00-TRIAL.md",
      "betalpha-social/recurring/weekly-watchlist/week-01-DRAFT.md",
      "betalpha-social/skills/pdf-to-structured/.clawhub/origin.json",
      "betalpha-social/skills/pdf-to-structured/SKILL.md",
      "betalpha-social/skills/pdf-to-structured/_meta.json",
      "betalpha-social/skills/pdf-to-structured/claw.json",
      "betalpha-social/skills/pdf-to-structured/instructions.md",
      "betalpha-social/threads/20260325_mining_capitulation_analysis.md",
      "betalpha-social/tools/pdf-to-excel-converter/DEMO.md",
      "betalpha-social/tools/pdf-to-excel-converter/DEMO_RECORDING.md",
      "betalpha-social/tools/pdf-to-excel-converter/README.md",
      "betalpha-social/tools/pdf-to-excel-converter/api/README.md",
      "betalpha-social/tools/pdf-to-excel-converter/api/SKILL_VET.md",
      "betalpha-social/tools/pdf-to-excel-converter/api/app.py",
      "betalpha-social/tools/pdf-to-excel-converter/api/app_fixed.py",
      "betalpha-social/tools/pdf-to-excel-converter/api/start_api.sh",
      "betalpha-social/tools/pdf-to-excel-converter/api/test_api.py"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: memory cronjob consolidation: Phase 1-3

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch aafc7a0bb14487767f7a1695ad3227d5d69a91ee

## Evidence

{
  "commit": "aafc7a0bb14487767f7a1695ad3227d5d69a91ee",
  "files": [
    "betalpha-social/.clawhub/lock.json",
    "betalpha-social/AGENTS.md",
    "betalpha-social/MEMORY.md",
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-24.md",
    "betalpha-social/memory/2026-03-25.md",
    "\"betalpha-social/memory/\\350\\236\\242\\345\\271\\225\\351\\214\\204\\345\\275\\261\\346\\226\\271\\346\\263\\225.md\"",
    "\"betalpha-social/post_history/2026-03-24_instagram_Prediction_Market\\344\\272\\244\\346\\230\\223\\346\\211\\200\\346\\231\\202\\345\\210\\273.md\"",
    "\"betalpha-social/post_history/2026-03-24_threads_BP\\347\\251\\272\\346\\212\\225_Mad_Lads.md\"",
    "betalpha-social/recurring/weekly-watchlist/IMAGE_TEMPLATE.md",
    "betalpha-social/recurring/weekly-watchlist/PLAN.md",
    "betalpha-social/recurring/weekly-watchlist/QUICKSTART.md",
    "betalpha-social/recurring/weekly-watchlist/week-00-TRIAL.md",
    "betalpha-social/recurring/weekly-watchlist/week-01-DRAFT.md",
    "betalpha-social/skills/pdf-to-structured/.clawhub/origin.json",
    "betalpha-social/skills/pdf-to-structured/SKILL.md",
    "betalpha-social/skills/pdf-to-structured/_meta.json",
    "betalpha-social/skills/pdf-to-structured/claw.json",
    "betalpha-social/skills/pdf-to-structured/instructions.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/.clawhub/lock.json, betalpha-social/AGENTS.md, betalpha-social/MEMORY.md, betalpha-social/learning/LESSONS.md",
    "large change set: 1128 files"
  ]
}
