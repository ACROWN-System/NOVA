# ISO 704:2022 Preliminary Semantic Review — Batch 021 (Action Policy, Alerts, Watchlist and Regression Tests)

**Review ID:** NOVA-ISO704-SEM-B021  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/STATUS REVIEW COMPLETE FOR FIVE FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main; exact blob SHAs below  
**Boundary:** Terminology/status and adjacent control review; no alerts were sent, no payments were created, and no tests were run.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B021-01 | NOVA/action_policy.json | f479bb29bb8ef5658eb8c98e9e214d41d06a3972 | REVIEWED — autonomy levels and irreversible gates explicit; payment-intent term needs operational definition |
| B021-02 | NOVA/alerts.py | 184eef693f4bf4ea1d1848f79d3bf6347024e2b7 | REVIEWED — current active/inactive labels may collapse any non-active state into DOWN; alert delivery claims and voice payload need separate evidence/security review |
| B021-03 | NOVA/tests/test_economics.py | 6f8101318b269a44d01974d7a93b156faf1a4768 | REVIEWED — test covers explicit free-resource accounting but not unknown/malformed provider price |
| B021-04 | NOVA/tests/test_reasoning.py | 97d2ab717d6085133d261dd30a95527e8ad0d016 | REVIEWED — only minimal valid-payload and empty-schema cases; no adversarial JSON type or policy consistency coverage |
| B021-05 | NOVA/watchlist.json | 84154eb180e92a300b4f7056d866dcead17c0d64 | REVIEWED — source list empty; external monitoring is not configured by this file |

## 2. Findings

### B021-F01 — Alert text maps every non-active provider status to DOWN

The comparative alert generator uses the label `live` if a provider's status equals `active`; every other status is labeled `DOWN`. This means `down`, `deferred`, `candidate`, `blocked`, `unconfigured`, or an unknown status would all receive the same output if they occur in the input roster. The present roster normally separates candidate records from active providers, but the alert function does not enforce a two-state schema or distinguish known inactive states.

**Required action:** map only an explicit `down` state to DOWN; render other known states distinctly and unknown states as UNKNOWN/UNRECOGNIZED. Validate allowed roster status values at the schema boundary, and add regression cases for each state. An alert message is operational evidence used by people; it must not overstate what a status means.

### B021-F02 — Payment intent is labelled autonomous without a local definition of its effects

The action policy requires a human gate for submitting crypto payments, irreversible transfers and changing public prices, but declares `create_payment_intent` autonomous. This may be a legitimate low-impact, non-settling preparation step, but the term “payment intent” is not defined in this file as strictly non-binding, non-settling, and unable to move funds or incur fees by itself.

**Required action:** define the exact allowed behavior and external side effects of payment-intent creation, including whether it reserves funds, triggers a charge, incurs a provider/network fee, or is merely a local draft. If any irreversible or fee-incurring effect can occur, require the policy gate appropriate to that effect. Do not infer safety solely from the operation's name.

### B021-F03 — Existing tests do not cover the potential unknown-cost and malformed-payload paths

The economics test confirms that an explicitly free resource does not change the public tariff, and tests a continuity status with supplied numeric amounts. It does not test absent/invalid tariff rates, unknown unit, malformed decimal, or negative cost inputs, so it does not guard against the B020-F02 zero-default ambiguity. The reasoning tests exercise one valid contract and an empty object; they do not cover JSON scalars/null/lists with invalid types, booleans as confidence, unhashable enum values, or a contradictory CRITICAL / L5 / `requires_human_gate` combination.

**Required action:** add focused negative tests as part of the separately reviewed implementation change. The present coverage cannot be cited as evidence that these cases are handled safely.

### B021-F04 — Empty watchlist means this configuration does not show active external sources

The watchlist document is valid JSON but its `sources` list is empty. The reasoning code returns `NO_PENDING_EVENTS` if there is no pending event; without configured sources, this file itself does not establish that external monitoring/annotation intake is active.

**Required action:** maintain the empty source list as an explicit NOT_CONFIGURED state unless there is a separate authoritative source list elsewhere. Do not claim the observer monitors external feeds merely because a reasoning stage and scheduler exist. If sources are added later, require source URL/identity, intended scope, observation interval, content/privacy boundary and versioned approval.

### B021-F05 — Alert-channel delivery comments are intent, not delivery evidence; voice output needs format-safe handling

The source comments describe GitHub alerts as free and say collaborators get email automatically, but the code alone only attempts to create an issue and returns True/False. It does not prove notification delivery to a particular recipient or that repository settings/preferences yield email. Separately, voice output embeds a generated first line directly into TwiML text without visible XML escaping. Since upstream analysis content can be influenced by external observations, this deserves a separate security review and escaping/negative tests.

**Required action:** distinguish `ISSUE_CREATED` from notification-delivered/received states, avoid describing email delivery as guaranteed without evidence, and route the voice-text formatting issue to a dedicated security remediation. This review did not send an alert or demonstrate an exploit; it records a source-level risk for independent verification.

## 3. Positive controls and limitations

- The action policy makes production/security/payment actions subject to explicit authorization categories and says backend provider changes do not change user pricing.
- The watchlist is a small, explicit configuration rather than an implicit hidden feed list; at present it is empty.
- Tests are source evidence only; none was executed during this review.
- No payment intent, transaction, SMS, voice call, GitHub issue or external provider action was executed.
- No ISO 704 clause result is assigned because the full controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed action policy, alert dispatcher, economics tests, reasoning validation tests, and external source watchlist; identified state-collapsing and insufficient regression coverage.
