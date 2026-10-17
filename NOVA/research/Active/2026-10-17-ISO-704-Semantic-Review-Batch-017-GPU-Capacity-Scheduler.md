# ISO 704:2022 Preliminary Semantic Review — Batch 017 (GPU Capacity Qualification and Expiry Scheduler)

**Review ID:** NOVA-ISO704-SEM-B017  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/STATE-MODEL REVIEW COMPLETE FOR FOUR FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA `main`, exact blob SHAs below  
**Boundary:** This review checks terminology, evidence states, and intended-use boundaries. The Python tests were read but not run; no GPU provider was called.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B017-01 | `NOVA/gpu_capacity.py` | `b6a6dc8c33a9b808cc2e7e8c83fac4a24ecb4853` | REVIEWED — stringent evidence gates and qualified-versus-active separation |
| B017-02 | `NOVA/tests/test_gpu_capacity.py` | `8e6e42fae7a2cf5f16c6cf4c9723c3af5bf3222a` | REVIEWED — tests cover scope, evidence freshness, no double-counting and usage unknowns |
| B017-03 | `NOVA/tests/test_capacity.py` | `1682448c3b498157c24eaa8180c977054915c674` | REVIEWED — tests preserve resource/call distinction, comparable value units, expiry and required-work boundary |
| B017-04 | `NOVA/probe_scheduler.py` | `d196d7636da569eb0aba35518a2c0917e2a21c90` | REVIEWED — rolling order and expiry preemption are tightly bounded in design; timing/runtime not tested |

## 2. Positive controls

### B017-C01 — Capacity eligibility is an evidence-gated concept, not an advertised quota

The GPU capacity report only counts recurring or one-time allocations where all required gates have the exact verified/pass state, capacity values are positive finite numbers, evidence URLs are HTTPS, observation timestamps are timezone-aware and not in the future, validity has not expired, and the provider is activated in the current GPU roster before it is treated as operationally available.

It explicitly separates:
- advertised monthly allowances (shown, not counted as usable);
- verified eligible capacity that is not active;
- active recurring capacity;
- one-time credit-backed capacity;
- allocation/use measurements and unmetered or unknown usage;
- the planning reference from a mandatory target.

This is a strong terminology/evidence design. Preserve it and do not relax it merely to make aggregate capacity figures look better.

### B017-C02 — Intended-use mode is a qualification dimension

The module supports separate modes for non-commercial R&D and commercial production. A provider qualification performed for one mode is blocked if the requested/current mode differs. This prevents a technical access test or an R&D eligibility statement from silently becoming evidence of commercial rights.

The `free_without_payment_method` gate remains a particularly sensitive concept because “account creation without a payment method”, “usable GPU allocation without a payment method”, and “no risk of paid overage” are not automatically equivalent. The roster's evidence fields still need the split noted in finding B013-F03; the strict boolean gate in this module does not repair an ambiguous upstream proposition by itself.

### B017-C03 — Unknown values and malformed evidence do not become convenient numbers

The GPU module rejects booleans as numeric GPU-minute values, non-finite/negative values, future observation times, expired evidence, invalid/non-HTTPS source URLs, and qualifications with unresolved or explicitly excluded gate states. The tests exercise these cases, check recurring versus one-time non-double-counting, require every active provider to be covered before aggregating usage, and preserve `UNKNOWN` instead of reporting unmetered usage as zero.

These are valuable controls, but reading the tests does not mean they were executed in this review, nor that the evidence register's real provider rows are correct.

### B017-C04 — Expiry scheduling cannot create artificial work

The probe scheduler has explicit preconditions for expiry preemption: an observed expiry opportunity, a normal scheduled check that would miss the deadline, already-required health work, and a provider not currently `UNACCEPTABLE`. It only moves providers actually checked to the end of the rolling ring, retains the remaining active-provider order, and describes its action as `EXPIRY_REALLOCATION` or `ROLLING_INTERVAL`.

The capacity helpers separately label expiry pressure as a scheduling signal, not proof of provider truth or economic benefit. Unknown economics do not by themselves create extra work; the constrained exception allows an already-required health probe to reuse capacity that would otherwise expire.

## 3. Scope notes / follow-up

- The report's 86,400 GPU-minute monthly reference is explicitly provisional and unvalidated, not a requirement. Do not phrase a shortfall against it as failure to meet a formally approved service requirement unless a separate project decision changes its status.
- A provider-specific gate reported as `VERIFIED` is only as strong as its linked source, intended-use scope, timestamp, freshness and review. The test fixture that says `VERIFIED` is synthetic evidence for the code path, not a real provider qualification.
- The command-line `main()` reports against an empty default active-provider set unless a caller supplies live roster names; the docstring says workflow integration supplies the live roster. Manual output should be labelled accordingly and must not be mistaken for operationally active capacity when no roster input was supplied.
- The probe scheduler's timing, race behavior and actual workflow cadence were not tested here.
- No ISO 704 clause result is assigned because the complete controlled baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed GPU-capacity evidence algorithm/tests, generic capacity economic tests, and the rolling expiry-aware scheduling algorithm/tests.
