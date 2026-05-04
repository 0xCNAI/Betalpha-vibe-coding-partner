---
{
  "title": "refactor: instagram-image-maker 大重構 - 統一 compose.py、重寫 SKILL.md、新增 text-design.md、AGENTS.m",
  "type": "spec_guardrail",
  "tags": [
    "token",
    "cron",
    "ci",
    "migration",
    "schema",
    "test"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `0738f961f061`: refactor: instagram-image-maker 大重構 - 統一 compose.py、重寫 SKILL.md、新增 text-design.md、AGENTS.md 指令觸發",
  "prevention_signal": "Before modifying `betalpha-social/2026-03-30-alchemix-cover.jpg` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"0738f961f06160f14811310120e4980b9687fa3b\",\n  \"files\": [\n    \"betalpha-social/2026-03-30-alchemix-cover.jpg\",\n    \"betalpha-social/2026-03-30-alchemix-cover.png\",\n    \"betalpha-social/AGENTS.md\",\n    \"betalpha-social/learning/LESSONS.md\",\n    \"betalpha-social/learning/jc_activity_tracking.md\",\n    \"betalpha-social/memory/2026-03-27.md\",\n    \"betalpha-social/memory/2026-03-28.md\",\n    \"betalpha-social/memory/2026-03-29.md\",\n    \"betalpha-social/memory/corrections.md\",\n    \"betalpha-social/post_history/2026-03-26_threads_X_Money_Benji_Taylor.md\",\n    \"betalpha-social/post_history/2026-03-27_threads_Clarity_Act_DeFi.md\",\n    \"betalpha-social/reports/daily_plan_2026-03-27.md\",\n    \"betalpha-social/threads/260330_alchemix_thread.md\",\n    \"jonathan/AGENTS.md\",\n    \"jonathan/data/daily_kol_digest.md\",\n    \"jonathan/data/daily_review_proposals/2026-03-26.md\",\n    \"jonathan/data/daily_review_proposals/2026-03-27.md\",\n    \"jonathan/data/daily_review_proposals/2026-03-28.md\",\n    \"jonathan/memory/2026-03-26.md\",\n    \"jonathan/memory/2026-03-27.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/2026-03-30-alchemix-cover.jpg, betalpha-social/2026-03-30-alchemix-cover.png, betalpha-social/AGENTS.md, betalpha-social/learning/LESSONS.md\",\n    \"large change set: 8717 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/2026-03-30-alchemix-cover.jpg` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "token",
      "cron",
      "ci",
      "migration",
      "schema",
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
    "sha": "0738f961f06160f14811310120e4980b9687fa3b",
    "date": "2026-03-30T13:52:42+08:00",
    "files": [
      "betalpha-social/2026-03-30-alchemix-cover.jpg",
      "betalpha-social/2026-03-30-alchemix-cover.png",
      "betalpha-social/AGENTS.md",
      "betalpha-social/learning/LESSONS.md",
      "betalpha-social/learning/jc_activity_tracking.md",
      "betalpha-social/memory/2026-03-27.md",
      "betalpha-social/memory/2026-03-28.md",
      "betalpha-social/memory/2026-03-29.md",
      "betalpha-social/memory/corrections.md",
      "betalpha-social/post_history/2026-03-26_threads_X_Money_Benji_Taylor.md",
      "betalpha-social/post_history/2026-03-27_threads_Clarity_Act_DeFi.md",
      "betalpha-social/reports/daily_plan_2026-03-27.md",
      "betalpha-social/threads/260330_alchemix_thread.md",
      "jonathan/AGENTS.md",
      "jonathan/data/daily_kol_digest.md",
      "jonathan/data/daily_review_proposals/2026-03-26.md",
      "jonathan/data/daily_review_proposals/2026-03-27.md",
      "jonathan/data/daily_review_proposals/2026-03-28.md",
      "jonathan/memory/2026-03-26.md",
      "jonathan/memory/2026-03-27.md",
      "jonathan/memory/2026-03-28.md",
      "jonathan/memory/2026-03-30.md",
      "jonathan/memory/corrections.md",
      "jonathan/post_history/threads_20260326_204000_x_money_benji_taylor.md",
      "jonathan/post_history/threads_20260327_171900_clarity_act_defi.md",
      "jonathan/post_history/threads_20260330_132600_alchemix_v3.md",
      "jonathan/projects/pdf-converter-v2/SPEC.md",
      "jonathan/projects/pdf-converter-v2/sample_output_format.xlsx",
      "jonathan/projects/pdf-converter-v2/sample_pdf_pu.jpg",
      "jonathan/projects/pdf-converter-v2/sample_pdf_sas.jpg"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: refactor: instagram-image-maker 大重構 - 統一 compose.py、重寫 SKILL.md、新增 text-design.md、AGENTS.md 指令觸發

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 0738f961f06160f14811310120e4980b9687fa3b

## Evidence

{
  "commit": "0738f961f06160f14811310120e4980b9687fa3b",
  "files": [
    "betalpha-social/2026-03-30-alchemix-cover.jpg",
    "betalpha-social/2026-03-30-alchemix-cover.png",
    "betalpha-social/AGENTS.md",
    "betalpha-social/learning/LESSONS.md",
    "betalpha-social/learning/jc_activity_tracking.md",
    "betalpha-social/memory/2026-03-27.md",
    "betalpha-social/memory/2026-03-28.md",
    "betalpha-social/memory/2026-03-29.md",
    "betalpha-social/memory/corrections.md",
    "betalpha-social/post_history/2026-03-26_threads_X_Money_Benji_Taylor.md",
    "betalpha-social/post_history/2026-03-27_threads_Clarity_Act_DeFi.md",
    "betalpha-social/reports/daily_plan_2026-03-27.md",
    "betalpha-social/threads/260330_alchemix_thread.md",
    "jonathan/AGENTS.md",
    "jonathan/data/daily_kol_digest.md",
    "jonathan/data/daily_review_proposals/2026-03-26.md",
    "jonathan/data/daily_review_proposals/2026-03-27.md",
    "jonathan/data/daily_review_proposals/2026-03-28.md",
    "jonathan/memory/2026-03-26.md",
    "jonathan/memory/2026-03-27.md"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/2026-03-30-alchemix-cover.jpg, betalpha-social/2026-03-30-alchemix-cover.png, betalpha-social/AGENTS.md, betalpha-social/learning/LESSONS.md",
    "large change set: 8717 files"
  ]
}
