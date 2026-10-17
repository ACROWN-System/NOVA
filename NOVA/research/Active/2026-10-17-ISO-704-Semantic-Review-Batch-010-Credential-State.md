# ISO 704:2022 Preliminary Semantic Review — Batch 010 (Provider Incident and Credential-State Records)

**Review ID:** NOVA-ISO704-SEM-B010  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR THREE FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** This review assesses terminology and status traceability. It does not independently verify the referenced live runs, provider terms, credentials, runtime behavior, or ISO clause conformity.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary result |
|---|---|---|---|
| B010-01 | `NOVA/research/2026.10.09-Provider-Error-Evidence-and-Credential-Gap-Review.md` | `f36cf163c801cf1648d350134b48ba2309237c2b` | REVIEWED — strong historical uncertainty classification; top-level state stale against later decisions |
| B010-02 | `NOVA/OPERATIONAL-STATE.md` | `897780186d896ba60eefa372dc791c75bcf88f6b` | REVIEWED — clean separation of code branch and telemetry state; administrative prerequisites are not current verification |
| B010-03 | `NOVA/KEY-READINESS.md` | `f47b2bf22dabefc07681a27c10a534a9a1319d01` | REVIEWED — resource lifecycle distinctions are useful; Cloudflare contract block and dated observations require precise interpretation |

## 2. Findings

### B010-F01 — Historical Mistral incident record has stale top-level status

The provider-error review is explicitly dated **2026-10-09** and records a 429 / code 1300 incident, run evidence and then-current diagnostics. Its header still reads **“PR #57 OPEN — current branch-head CI passed all 56 offline tests; live-provider outcomes remain pending.”** The later active resource-readiness record says Mistral was deferred on 2026-10-10 by user decision and excluded from active free-tier capacity/health probes, while other repository history references the diagnostic fix and the later deferral PR. The header can therefore be misread as current workflow/qualification state rather than status at the original observation date.

**Required action:** keep the incident timeline immutable and accurate, but add a conspicuous “status as of observation date” qualifier or a later status/reconciliation note linked to the subsequent decision. Confirm the exact PR disposition from repository metadata before updating the factual statement. Do not erase the historical run state, rewrite the original observations, or treat the code-1300 cause as proven. Mistral remains deferred unless a separately authorized requalification occurs.

### B010-F02 — Positive control: status concepts are explicitly separated

Across these files, NOVA distinguishes:
- secret present vs credential authenticated;
- credential configured vs provider activated;
- API reachability vs valid response contract vs quality;
- account/project/organization limit scope;
- one historical observed failure vs confirmed root cause;
- candidate GPU credential vs an active GPU allocation;
- current code policy on main vs persisted runtime-health markers on the separate operational-state branch.

These distinctions are valuable evidence of controlled language. Preserve them and use the same lifecycle/state semantics in future provider/resource records. A key being present or a heartbeat overall succeeding is not proof that all providers are healthy or eligible.

### B010-F03 — “Cloudflare contract unverified” is endpoint/model-specific, not a universal provider status

The key-readiness record says Cloudflare inference qualification remains blocked without another request until the exact model/API response contract is verified. The Cloudflare image qualification record documents live image-request evidence, including a confirmed image/png header with JPEG payload. These records cover different API paths: an image endpoint success cannot establish LLM/chat endpoint qualification, and a chat smoke-test result cannot establish image-generation qualification.

**Required action:** name the actual Cloudflare capability/model/endpoint in each status and avoid a provider-wide “verified” flag where different adapters remain in different states. Record image-generation, chat inference, and any GPU allocation/API adapter as separate capabilities if they have different contracts and evidence.

### B010-F04 — Several statements are dated observations rather than current entitlements

The provider incident review contains historical account secret-presence observations, rate limits, model candidates and third-party/provider issue links. It is date-stamped and often labels unknowns appropriately, but its long candidate tables can look like an operationally current roster unless the snapshot date and status boundary remain prominent.

**Required action:** maintain an “observed at” date and source for each changing quota, plan, or account state; do not treat the contents of an older snapshot as current availability or as authority to activate a candidate. This review did not revisit provider accounts or refresh their terms.

## 3. Evidence and readiness effect

- The operational-state document clearly says code/policy changes belong on main via pull requests and telemetry writes belong on the separate operational-state branch; the state branch is not a feature-development branch.
- The key-readiness document says the validation workflow checks presence only and does not call providers; live qualification, billing, quota, rights, and GPU capacity require separate evidence.
- Provider error review's 2026-10-09 header needs reconciliation with later decisions, without overwriting the original incident timeline.
- No provider was contacted or called during this batch; no secret was viewed or changed.
- No ISO 704 clause assessment is performed; the full standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Preliminary review of provider incident, operational-state branch policy, and key-readiness semantics.
