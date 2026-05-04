---
{
  "title": "init: full clawd monorepo",
  "type": "spec_guardrail",
  "tags": [
    "auth",
    "token",
    "ci",
    "github",
    "schema",
    "deploy",
    "test"
  ],
  "tech_stack": [
    "github-actions",
    "node",
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `02ca85f859c6`: init: full clawd monorepo",
  "prevention_signal": "Before modifying `betalpha-social/.skill_review_2026-03-09.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"02ca85f859c623fbb9acef6abd61e8b8a6bc1b6e\",\n  \"files\": [\n    \".agents/skills/canvas-design/LICENSE.txt\",\n    \".agents/skills/canvas-design/SKILL.md\",\n    \".agents/skills/canvas-design/canvas-fonts/ArsenalSC-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/ArsenalSC-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/BigShoulders-Bold.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/BigShoulders-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/BigShoulders-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/Boldonse-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/Boldonse-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Bold.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Italic.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/CrimsonPro-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/DMMono-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/DMMono-Regular.ttf\",\n    \".agents/skills/canvas-design/canvas-fonts/EricaOne-OFL.txt\",\n    \".agents/skills/canvas-design/canvas-fonts/EricaOne-Regular.ttf\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: betalpha-social/.skill_review_2026-03-09.md, betalpha-social/AGENTS.md, betalpha-social/HEARTBEAT.md, betalpha-social/IDENTITY.md\",\n    \"large change set: 1151 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `betalpha-social/.skill_review_2026-03-09.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "domain_metadata": {
    "tags": [
      "auth",
      "token",
      "ci",
      "github",
      "schema",
      "deploy",
      "test"
    ],
    "tech_stack": [
      "github-actions",
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
    "sha": "02ca85f859c623fbb9acef6abd61e8b8a6bc1b6e",
    "date": "2026-03-14T23:12:39+08:00",
    "files": [
      ".agents/skills/canvas-design/LICENSE.txt",
      ".agents/skills/canvas-design/SKILL.md",
      ".agents/skills/canvas-design/canvas-fonts/ArsenalSC-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/ArsenalSC-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/BigShoulders-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/BigShoulders-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/BigShoulders-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/Boldonse-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/Boldonse-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Italic.ttf",
      ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/DMMono-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/DMMono-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/EricaOne-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/EricaOne-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/GeistMono-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/GeistMono-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/GeistMono-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/Gloock-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/Gloock-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/IBMPlexMono-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/IBMPlexMono-OFL.txt",
      ".agents/skills/canvas-design/canvas-fonts/IBMPlexMono-Regular.ttf",
      ".agents/skills/canvas-design/canvas-fonts/IBMPlexSerif-Bold.ttf",
      ".agents/skills/canvas-design/canvas-fonts/IBMPlexSerif-BoldItalic.ttf"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: init: full clawd monorepo

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch 02ca85f859c623fbb9acef6abd61e8b8a6bc1b6e

## Evidence

{
  "commit": "02ca85f859c623fbb9acef6abd61e8b8a6bc1b6e",
  "files": [
    ".agents/skills/canvas-design/LICENSE.txt",
    ".agents/skills/canvas-design/SKILL.md",
    ".agents/skills/canvas-design/canvas-fonts/ArsenalSC-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/ArsenalSC-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/BigShoulders-Bold.ttf",
    ".agents/skills/canvas-design/canvas-fonts/BigShoulders-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/BigShoulders-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/Boldonse-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/Boldonse-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Bold.ttf",
    ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/BricolageGrotesque-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Bold.ttf",
    ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Italic.ttf",
    ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/CrimsonPro-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/DMMono-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/DMMono-Regular.ttf",
    ".agents/skills/canvas-design/canvas-fonts/EricaOne-OFL.txt",
    ".agents/skills/canvas-design/canvas-fonts/EricaOne-Regular.ttf"
  ],
  "reasons": [
    "touches risky subsystem: betalpha-social/.skill_review_2026-03-09.md, betalpha-social/AGENTS.md, betalpha-social/HEARTBEAT.md, betalpha-social/IDENTITY.md",
    "large change set: 1151 files"
  ]
}
