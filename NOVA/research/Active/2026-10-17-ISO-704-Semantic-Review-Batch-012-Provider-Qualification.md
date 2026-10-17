# ISO 704:2022 Preliminary Semantic Review — Batch 012 (Provider Qualification Diagnostic)

**Review ID:** NOVA-ISO704-SEM-B012  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/STATE-SEMANTICS REVIEW COMPLETE FOR THREE FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** This is not a live provider probe, credential inspection, software security audit, or ISO clause-conformity result.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B012-01 | `NOVA/provider_qualification.py` | `8ebe5b58b74a269ad983d8b61e9c9fd2c740a3b9` | REVIEWED — safe diagnostics and evidence/eligibility boundaries are explicit; Cloudflare qualification state conflicts with a documentation source |
| B012-02 | `NOVA/tests/test_provider_qualification.py` | `ca636fb85dcb30892a37e800f191ecf969460cdc` | REVIEWED — mock tests preserve privacy and state distinctions; not live qualification evidence |
| B012-03 | `.github/workflows/nova-provider-qualification.yml` | `2faf2af2f7e326b62ab95a4165080cc6da337528` | REVIEWED — bounded manually dispatchable and source-triggered workflow with read-only repo permissions; no runtime run performed |

## 2. Findings

### B012-F01 — Cloudflare LLM qualification state conflicts across the diagnostic and KEY-READINESS.md

In the reviewed provider-qualification code, Cloudflare's `@cf/meta/llama-3.1-8b-instruct-fast` row is deliberately not probed by this diagnostic. It is recorded as `SKIPPED_ALREADY_QUALIFIED`, `lifecycle_status: ACTIVE`, and linked to live evidence run 38350563789 for the exact structured-JSON response contract. The diagnostic intentionally does not read the Cloudflare secret values; it sets credential-configured to null and states that “not checked here” is not the same as “missing”.

However, the active `NOVA/KEY-READINESS.md` still describes Cloudflare inference as `BLOCKED_CONTRACT_UNVERIFIED` and says the exact model/API response contract remains to be verified. The two sources therefore conflict about the qualification state of the same Cloudflare inference capability. This may reflect stale documentation or a change in qualification scope, but the reason is not established from these three files alone.

**Required action:** reconcile the current source-of-truth status using the linked run and exact model/endpoint evidence. Record the qualification's scope (model, endpoint/API operation, response contract), observation date, tested result, evidence URL, and any expiry/retest rule. Update KEY-READINESS.md or the diagnostic through a reviewed change so both agree. If the previous result no longer applies, restore BLOCKED with the reason; if it applies only to the response contract, say that explicitly rather than treating it as overall operational readiness. Do not trigger another provider request just to resolve documentation drift unless a human explicitly authorizes it.

### B012-F02 — “Already qualified” is narrower than live availability, quota, zero-cost entitlement, or production readiness

The diagnostic's own text correctly says a pass does not prove remaining quota, $0 eligibility, commercial rights or production capacity. Its Cloudflare row skips a duplicate inference request based on earlier evidence. A skipped probe is not a fresh observation of current provider health, credential configuration, free allocation, account billing, quality, or commercial eligibility.

**Required action:** keep separate fields for response-contract qualification, last live observation, current account/credential check, cost/terms eligibility, quality, rate/quota and lifecycle. Add evidence freshness/expiry where a decision depends on current status. Render `SKIPPED_ALREADY_QUALIFIED` as “no new request this run; prior scoped contract evidence referenced”, not as a fresh provider PASS.

### B012-F03 — Positive control: diagnostic result labels distinguish HTTP, shape, marker and resource states

The code distinguishes response status, JSON/shape validity, presence of the probe marker, latency, sanitized allowlisted rate-limit headers, token-usage counters and lifecycle. The status vocabulary includes distinct outcomes for authentication rejection, payment/credit ambiguity, policy/access denial, endpoint/model-not-found, rate-limit/quota ambiguity, provider server errors, network errors, timeouts, invalid body shape, missing marker and skipped credential.

The mock tests also demonstrate that response text, synthetic secrets and personal identity fields are not persisted; they assert that missing markers are not mislabelled as authentication failure and that a token credential alone does not establish credits. These are useful meaning and evidence boundaries.

**Disposition:** preserve these distinctions. A diagnostic outcome such as `PASS` means the bounded expected probe response/marker was observed; it does not automatically grant a lifecycle promotion or establish an entitlement.

## 3. Evidence and limitations

- The source explicitly excludes Mistral from probes by current decision and skips Cloudflare to avoid duplicating a previous bounded request.
- Tests use synthetic/mock responses and patched network calls. They are offline implementation evidence, not current account observations.
- This review did not execute the workflow or provider code, inspect secret values, or verify the referenced external run artifact/log.
- No code, secret or operational state was changed by this review.
- No ISO 704 clause conformity result is assigned.

## 4. Evidence links

- [Provider qualification implementation](https://github.com/ACROWN-System/NOVA/blob/main/NOVA/provider_qualification.py)
- [Provider qualification tests](https://github.com/ACROWN-System/NOVA/blob/main/NOVA/tests/test_provider_qualification.py)
- [Provider qualification workflow](https://github.com/ACROWN-System/NOVA/blob/main/.github/workflows/nova-provider-qualification.yml)
- [Cloudflare qualification evidence referenced by the diagnostic](https://github.com/ACROWN-System/NOVA/actions/runs/38350563789)
- [KEY-READINESS.md](https://github.com/ACROWN-System/NOVA/blob/main/NOVA/KEY-READINESS.md)

## 5. Revision history

- **2026-10-17 / v0.1.0:** Reviewed the qualification diagnostic, its tests and workflow. Found an unresolved Cloudflare status conflict between implementation and key-readiness documentation.
