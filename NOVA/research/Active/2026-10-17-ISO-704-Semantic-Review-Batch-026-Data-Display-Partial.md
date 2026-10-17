# ISO 704:2022 Targeted Semantic Screen — Batch 026 (AstroCrown Data-Display Conventions)

**Review ID:** NOVA-ISO704-SEM-B026  
**Date:** 2026-10-17  
**Status:** PARTIAL TARGETED SCREEN ONLY — FULL SEMANTIC REVIEW NOT COMPLETE  
**Path:** `development/index-reference/DATA-DISPLAY-CONVENTIONS.md`  
**Baseline blob SHA:** `e300be472be18f4cf3c15a3600195a1262f7e0e2`  
**Size:** 43589 characters / 858 lines  
**Boundary:** This screen is not a full file-by-file semantic assessment, a browser test of the deployed UI, a validation of market data, or an ISO clause-conformity result.

## 1. Targeted screen method

The text was scanned for terminology and evidence-boundary patterns relevant to display conventions:
- source/provenance and provider/methodology language;
- currency, units, price and numeric precision;
- timestamps, freshness and rolling-period wording;
- unknown, unavailable, blocked, missing and error states;
- concept/definition/label language;
- claims, verification and licence wording.

The counts below are search-hit counts only; they do not establish that a term is correct, that every applicable passage was reviewed, or that a corresponding control is implemented.

| Screen dimension | Pattern-hit count |
|---|---:|
| source/provenance | 201 |
| currency/units | 10 |
| time/freshness | 15 |
| unavailable/error states | 27 |
| concept/label definitions | 7 |
| license/claim caveats | 17 |

## 2. Evidence disposition

### B026-F01 — Display-convention screen is not yet evidence of display correctness

A data-display convention is a requirements/meaning source: it can define how a price, market statistic, time window, unavailable value or label should appear. It does not prove that each current interface element uses that definition, that the displayed data came from the stated source, that its units and observation time are correct, or that failure/unknown states are rendered honestly.

The current pass is intentionally partial. No individual UI field is marked conformant from keyword presence alone.

**Required action:** perform a full section-by-section review of the document, then map each in-scope displayed concept to (a) its canonical/domain definition, (b) authoritative data source and transformation, (c) unit/currency/time-window semantics, (d) freshness and stale/unavailable behavior, and (e) a real implementation test or recorded sample from the exact assessed build. For every public-facing output, distinguish the specified display behavior from observed runtime behavior. If a unit, method, source timestamp, or fallback is missing, record a finding rather than inferring it.

## 3. Limitations and next step

- This is a partial text-pattern screen, not a completed semantic review.
- No live market feed or website build was inspected, and no UI/browser test was performed.
- The precise meaning of any project-defined display label must be verified in its own context and linked to a canonical/domain entry where appropriate.
- The document remains **NOT FULLY REVIEWED** in the content sweep tracker.
- No ISO 704 clause result is assigned; the complete controlled standard baseline remains blocked.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Recorded a targeted selected-term screen only; full section-by-section semantic review remains open.
