# How to Test Whether Betavibe Is Actually Useful

Do not judge this by whether the CLI runs. Judge it by whether it changes developer behavior and reduces repeated mistakes.

## Test 1 — Retrospective replay A/B

Pick 5 old painful bugs from real client/project history.

For each bug, create a short task prompt that describes the original starting point but not the final solution.

Run two agents or two attempts:

- Control: no Betavibe resolver.
- Treatment: must run `resolve pre_spec` and `resolve pre_implement` first.

Measure:

- Did treatment identify the likely pitfall earlier?
- Did treatment avoid wrong paths from the original debug?
- Did the spec include better verification gates?
- Time to correct diagnosis.
- Number of tool calls / failed attempts.

Pass condition: treatment avoids at least 50% of repeated wrong paths across 5 cases.

## Test 2 — Spec quality gate

Take 3 upcoming features or fake client tasks.

Ask an agent to write specs with and without resolver output.

Score each spec 1-5 on:

- Known pitfalls included as guardrails.
- Verification plan quality.
- Tool choice correctness.
- Rollback / migration safety.
- Client delivery stability.

Pass condition: resolver-assisted specs improve average score by >= 1 point.

## Test 3 — Capture precision

During one week of development, let agents run `should-capture` after debug sessions.

Track:

- capture recommended count
- approved count
- rejected count
- later-useful count

Pass condition:

- approval rate >= 50%
- rejected items are mostly “not verified / too generic,” not random bad triggers
- at least one captured insight is surfaced later in a relevant task

## Test 4 — Retrieval quality

Seed 20 reviewed insights.

Create 20 search prompts with different wording from the original insight.

Run:

```bash
python3 -m betavibe resolve pre_spec --context "<prompt>"
```

Score:

- top-1 relevant?
- top-3 relevant?
- stale/conflicting surfaced clearly?

Pass condition:

- top-3 relevance >= 80%
- no dangerous false positive in top-1

## Test 5 — Client-delivery simulation

For one small internal project, require this flow:

1. scan existing repo history
2. promote 3-5 real insights
3. write a new spec with resolver
4. implement with resolver
5. capture any hard-won debug lesson

Pass condition:

- at least one spec decision changes because of prior insight
- at least one verification gate is added
- no unverified/generic insight enters reviewed registry

## Decision rule

Betavibe is worth keeping only if it creates one of these outcomes:

- avoids a repeated bug
- improves spec guardrails
- shortens diagnosis time
- picks a better tool earlier
- forces verification that would otherwise be skipped

If it only creates nicer notes, it failed.
