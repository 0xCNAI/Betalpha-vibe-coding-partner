# Insight Schema

Each reviewed insight is `registry/insights/YYYY-MM-title/INSIGHT.md`.

Frontmatter is JSON between `---` fences for parser stability across agents.

Required fields:

- title
- type: pitfall | decision | pattern | tool_choice | spec_guardrail
- tags
- tech_stack
- summary
- prevention_signal
- verify_trigger
- created_at
- last_verified_at
- source

Useful body sections:

- Symptom
- Root Cause
- Wrong Paths
- Fix
- Decision
- Tradeoffs
- Pattern
- Tool Guidance
- Evidence
