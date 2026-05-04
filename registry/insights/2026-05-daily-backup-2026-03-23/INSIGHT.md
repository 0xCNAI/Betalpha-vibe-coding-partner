---
{
  "title": "daily backup 2026-03-23",
  "type": "spec_guardrail",
  "tags": [
    "git-history"
  ],
  "tech_stack": [
    "python"
  ],
  "summary": "Git history candidate from `clawd` commit `ca7f9ccd6e11`: daily backup 2026-03-23",
  "prevention_signal": "Before modifying `research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
  "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
  "concrete_evidence": "{\n  \"commit\": \"ca7f9ccd6e11de0386965023ce2ef48bdc27379a\",\n  \"files\": [\n    \"jonathan/AGENTS.md\",\n    \"publish/AGENTS.md\",\n    \"research/data/pattern_placement.jsonl\",\n    \"research/data/pipeline_events.jsonl\",\n    \"research/data/podcast_pipeline_state.json\",\n    \"research/data/podcast_processed.json\",\n    \"research/data/training/inputs/flash_2026-03-22_22.json\",\n    \"research/data/training/inputs/flash_2026-03-22_23.json\",\n    \"research/data/training/inputs/portfolio_2026-03-22_22.json\",\n    \"research/scripts/podcast_nightly.py\",\n    \"research/skills/flash-news/references/exploit_response_playbook.md\",\n    \"research/skills/portfolio-alpha/data/positive_examples.jsonl\",\n    \"research/vault/_meta/link_suggestions.md\",\n    \"research/vault/_meta/orphans.md\",\n    \"research/vault/_meta/skill_versions.md\",\n    \"research/vault/_weekly_review.md\",\n    \"research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md\",\n    \"research/vault/inputs/podcasts/2026-03-20_bell_curve_tempo_goes_live_can_stripes_blockchain_own_the_payment_rails.md\",\n    \"\\\"research/vault/inputs/podcasts/2026-03-21_gooaye_\\\\350\\\\202\\\\241\\\\347\\\\231\\\\214_ep646.md\\\"\",\n    \"research/vault/inputs/podcasts/2026-03-22_unchained_bits_bips_what_iran_oil_shocks_and_no_rate_cuts_mean_for_cry.md\"\n  ],\n  \"reasons\": [\n    \"touches risky subsystem: research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md, research/vault/inputs/podcasts/2026-03-20_bell_curve_tempo_goes_live_can_stripes_blockchain_own_the_payment_rails.md, social-agent/AGENTS.md\",\n    \"large change set: 23 files\"\n  ]\n}",
  "transferable_pattern": "Before modifying `research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md` or adjacent subsystem, search this registry and inspect the original fixing commit.",
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
    "sha": "ca7f9ccd6e11de0386965023ce2ef48bdc27379a",
    "date": "2026-03-23T03:01:04+08:00",
    "files": [
      "jonathan/AGENTS.md",
      "publish/AGENTS.md",
      "research/data/pattern_placement.jsonl",
      "research/data/pipeline_events.jsonl",
      "research/data/podcast_pipeline_state.json",
      "research/data/podcast_processed.json",
      "research/data/training/inputs/flash_2026-03-22_22.json",
      "research/data/training/inputs/flash_2026-03-22_23.json",
      "research/data/training/inputs/portfolio_2026-03-22_22.json",
      "research/scripts/podcast_nightly.py",
      "research/skills/flash-news/references/exploit_response_playbook.md",
      "research/skills/portfolio-alpha/data/positive_examples.jsonl",
      "research/vault/_meta/link_suggestions.md",
      "research/vault/_meta/orphans.md",
      "research/vault/_meta/skill_versions.md",
      "research/vault/_weekly_review.md",
      "research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md",
      "research/vault/inputs/podcasts/2026-03-20_bell_curve_tempo_goes_live_can_stripes_blockchain_own_the_payment_rails.md",
      "\"research/vault/inputs/podcasts/2026-03-21_gooaye_\\350\\202\\241\\347\\231\\214_ep646.md\"",
      "research/vault/inputs/podcasts/2026-03-22_unchained_bits_bips_what_iran_oil_shocks_and_no_rate_cuts_mean_for_cry.md",
      "research/vault/meta/data/tweet_tracker.json",
      "research/vault/news/2026-03-22.md",
      "social-agent/AGENTS.md"
    ]
  }
}
---

## Symptom

Commit message suggests a potential lesson: daily backup 2026-03-23

## Root Cause

Review the commit diff / PR discussion before promotion.

## Wrong Paths

Unknown from git log alone.

## Fix

Inspect with: git show --stat --patch ca7f9ccd6e11de0386965023ce2ef48bdc27379a

## Evidence

{
  "commit": "ca7f9ccd6e11de0386965023ce2ef48bdc27379a",
  "files": [
    "jonathan/AGENTS.md",
    "publish/AGENTS.md",
    "research/data/pattern_placement.jsonl",
    "research/data/pipeline_events.jsonl",
    "research/data/podcast_pipeline_state.json",
    "research/data/podcast_processed.json",
    "research/data/training/inputs/flash_2026-03-22_22.json",
    "research/data/training/inputs/flash_2026-03-22_23.json",
    "research/data/training/inputs/portfolio_2026-03-22_22.json",
    "research/scripts/podcast_nightly.py",
    "research/skills/flash-news/references/exploit_response_playbook.md",
    "research/skills/portfolio-alpha/data/positive_examples.jsonl",
    "research/vault/_meta/link_suggestions.md",
    "research/vault/_meta/orphans.md",
    "research/vault/_meta/skill_versions.md",
    "research/vault/_weekly_review.md",
    "research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md",
    "research/vault/inputs/podcasts/2026-03-20_bell_curve_tempo_goes_live_can_stripes_blockchain_own_the_payment_rails.md",
    "\"research/vault/inputs/podcasts/2026-03-21_gooaye_\\350\\202\\241\\347\\231\\214_ep646.md\"",
    "research/vault/inputs/podcasts/2026-03-22_unchained_bits_bips_what_iran_oil_shocks_and_no_rate_cuts_mean_for_cry.md"
  ],
  "reasons": [
    "touches risky subsystem: research/vault/inputs/podcasts/2026-03-20_bell_curve_oneshot_tempo_mainnet_agentic_payments_and_sec_crypto_rulema.md, research/vault/inputs/podcasts/2026-03-20_bell_curve_tempo_goes_live_can_stripes_blockchain_own_the_payment_rails.md, social-agent/AGENTS.md",
    "large change set: 23 files"
  ]
}
