# ISO 704 Semantic Review Batch 071 — AstroCrown Market Data, Pagination and Navigation Concepts

**Document ID:** NOVA-ISO704-SEM-B071  
**Review date:** 2026-10-18  
**Baseline repository:** `ACROWN-System/AstroCrown-Web`  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Scope:** Four homepage-section documentation files and the active development HTML entry point, retrieved at the pinned baseline and checked against the live tracker before review.  
**Review status:** Preliminary full-file semantic review; human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report does not claim conformity or nonconformity to any clause.

## Review method and limits

The five complete source files were read at the recorded baseline blob SHAs. Review emphasis: concept identity and boundaries; precise term designations and units; classification and measurement-method status; relation types among market metrics, assets, sections, and destinations; source-of-authority and migration traceability; and candidate-versus-approved status. `development/index.html` was reviewed as a minimal HTML scaffold, not treated as proof of a built/rendered homepage. This was a static content review; no code/runtime, browser output, tests, workflows, secrets, providers, billing, repository settings, or backup/archive paths were changed, executed, or inspected.

## Source manifest and dispositions

| # | Source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B071-01 | `development/index-section/MARKET-DATA-BAR.md` | `abccb55ba2f3c88ebca65a1c1eb8a3fc66406318` | Preliminary review; extend SWEEP-F-0038 and SWEEP-F-0049. |
| B071-02 | `development/index-section/PAGINATION.md` | `7048fe35517e99ee421b4fe1d8b9ffcd93cd9c00` | Preliminary review; extend SWEEP-F-0038 and open SWEEP-F-0051 on subsystem concept/source-boundary mismatch and duplicated directory excerpt. |
| B071-03 | `development/index-section/README.md` | `7380213b0aa909e09090b9f9c20dec170c698ae8` | Preliminary review; extend SWEEP-F-0038 for provenance of the stated pre-migration authority/source boundary. |
| B071-04 | `development/index-section/SECONDARY-NAVIGATION.md` | `08fe585ac93ec0bd058c125d9301b1f403aec574` | Preliminary review; extend SWEEP-F-0038. No unique navigation terminology finding. |
| B071-05 | `development/index.html` | `0832cf9e8bbee2221e9ee937f8a89a14b388d300` | Preliminary review; minimal HTML shell only; no unique terminology finding from this file alone. |

## File-level review notes

### B071-01 — Market Data Bar

The candidate list combines market-capitalization and volume measures, BTC/ETH dominance values, named assets (BTC, ETH, ACROWN), and generic market-state indicators. These are not the same semantic kind, but the section explicitly labels them candidate information and says the final set remains subject to usability/information-density evaluation; that candidate status is a positive control. The document also correctly requires source, freshness, source-versus-derived status, unavailable/stale behavior, and reference conventions before relying on displayed values.

The phrase “reference currency/device” repeats the undefined designation already recorded in SWEEP-F-0049 for the Directory. Since the Market Data Bar independently lists the same concept among its explicitly undefined choices, F-0049 is extended to this path. This review does not select the intended term or formula. The actual reference concept, units, conversion basis/timing, and effect on displayed market changes must be decided before implementation, not inferred from “device”.

### B071-02 — Pagination

The file is titled “Homepage Pagination”, and its migration note states that exact pagination is intentionally undefined. However, the source body after that note repeats the R-023 working-directory material—including the filter taxonomy, market intelligence examples, directory row fields, execution-data caveat, scrolling requirements, and the list of directory decisions left undefined. The same R-023 material is also present in `DIRECTORY.md`. The excerpt is identified as lines 1793–1858, an R-023 source range, rather than a defined pagination requirement; no pagination-specific concept or relation is stated beyond pagination appearing at the end of a directory flow.

The explicit decision not to invent pagination behavior is a positive control. The risk is the document's concept-to-content alignment and duplicate source scope: readers cannot easily tell whether this is deliberately a context-only pointer, a duplicate source excerpt, or the intended canonical pagination requirement. SWEEP-F-0051 records this without guessing the source author's intent. A human-maintained resolution should either make the file an explicit scope/placeholder record that points to the canonical directory requirements and clearly states the known pagination boundary, or attach the correctly identified source material if an approved pagination concept exists. Do not invent page size, cursor/page-number semantics, ordering preservation, or interaction rules.

### B071-03 — Homepage Section Requirements README

The README establishes a helpful source-of-authority model: section-specific documents are active sources; shared visual/interaction conventions live in the reference directory; reusable platform infrastructure has separate subsystem directories; and candidate/discovery/unresolved/approved states should not be silently collapsed. These are positive terminology-governance controls.

It also states that the pre-migration monolithic source remains in backup snapshots, solely for historical consultation, without identifying a retrievable immutable commit/blob or migration manifest in this active README. This review did not inspect those excluded snapshots. SWEEP-F-0038 is extended to include the README's unpinned source-of-authority/provenance statement; this does not establish that the historical source is missing or was never present.

### B071-04 — Secondary Navigation

R-024 gives the section a bounded purpose and preserves candidate destinations (market, research, analytics, exchange/swap, knowledge, ecosystem, and NOVA-powered systems) as candidates. It explicitly prohibits inventing destinations merely to fill space, prohibits duplication of primary card/directory information, and leaves exact destinations, quantity, ordering, content, composition, and responsive behavior undefined. These statements are useful controls over both term promotion and information-architecture drift.

Its historical line range is named but not pinned to a source commit/blob in the active file. SWEEP-F-0038 is extended to record that traceability gap. No separate concept defect was opened from this short source alone.

### B071-05 — Development HTML entry point

At the pinned baseline, this file contains only a doctype, English-language document declaration, charset, viewport metadata, the page title “AstroCrown”, and an empty body. It does not define homepage section concepts or establish that the homepage is rendered/populated. The baseline is recorded as a minimal scaffold; no implementation conclusion is inferred beyond its literal contents, and no browser/build verification was conducted. No unique terminology finding is opened from this file alone.

## Findings and traceability updates

1. **SWEEP-F-0038 — Homepage requirement source identity and extracted-reference traceability:** Extend to `MARKET-DATA-BAR.md`, `PAGINATION.md`, `SECONDARY-NAVIGATION.md`, and `index-section/README.md`. The first three cite historical line ranges without immutable origin pins; the README refers to a pre-migration monolithic source in backup snapshots without a retrievable immutable source identifier. No backup/archive content was inspected.
2. **SWEEP-F-0049 — “Reference device/currency” and percentage-change basis are underdefined:** Extend to `MARKET-DATA-BAR.md`, whose undefined-decision list repeats “reference currency/device”. Definition, unit, conversion basis and calculation behavior remain unresolved.
3. **SWEEP-F-0051 — Pagination document duplicates directory requirements without a defined pagination concept model:** New. The file titled `PAGINATION.md` reproduces the R-023 directory excerpt already in `DIRECTORY.md`, while saying exact pagination is undefined and stating no pagination-specific requirements beyond its mention in a flow. This obscures concept ownership and the distinction between context and a canonical requirement. Closure should clarify intentional placeholder/context status or trace the correct approved source; do not invent pagination behavior.

Positive controls include explicit candidate status for market metrics and secondary destinations; explicit undefined state for pagination behavior and reference conventions; clear active-source versus historical-source separation in the README; and the statement that destinations must not be invented. All findings remain open and preliminary pending designated human validation. No runtime defect is claimed.

## Batch disposition and counts

After recording these five full-file preliminary reviews, the row-derived sweep target is:

- Active files inventoried: **318**
- Preliminary full-file reviews: **271**
- Partial targeted screens: **5**
- Not yet reviewed: **42**
- Human validation of preliminary reviews: **pending**
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: **proposed; human approval pending**

Arithmetic check: 271 + 5 + 42 = 318.

No AstroCrown-Web source/runtime files, backup/archive paths, tests, workflows, credentials, provider calls, billing, or repository settings were changed or used. This is not a formal ISO 704 clause assessment or conformity statement.
