# ISO 704:2022 Preliminary Semantic Review — Batch 024 (AstroCrown Public Claims and Homepage Header)

**Review ID:** NOVA-ISO704-SEM-B024  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR TWO FILES; HUMAN VALIDATION REQUIRED  
**Boundary:** This is a document/terminology review. It does not verify the current deployed website, legal claims, accessibility behavior in a browser, or ISO 704 clause conformity.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B024-01 | `development/audit/PUBLIC-CLAIMS-AND-LEGAL-COMMUNICATIONS.md` | `7bc015ef84e202940356943b17af428b99fd5841` | REVIEWED — public-claim governance procedure; live claim-by-claim evidence still needed |
| B024-02 | `development/index-section/HEADER.md` | `b04353e06f66e621e08d4f43b45d34d6043c1c32` | REVIEWED — homepage header requirements; not proof of deployed or accessible behavior |

## 2. Findings

### B024-F01 — A public-claims procedure is not evidence that every published claim has been verified

The public-claims/legal-communications document provides a process for substantiating material statements and distinguishing a legal/financial claim from marketing wording. It is useful governance evidence, but it does not itself prove that each current website statement, social claim, asset-rights statement, capability statement, or standards-related claim was individually checked against a current source and approved.

**Required action:** when the audit scope is approved, build a claim inventory for the actual public surfaces in scope. For each claim record exact wording/location, claim owner, concept/term references, authoritative source, source observation date, scope/jurisdiction, implementation status, validation result, reviewer and next-review trigger. Mark claims without evidence BLOCKED or NOT VERIFIED rather than treating the existence of a policy as a PASS. Keep external legal conclusions separate from project-defined terminology.

### B024-F02 — The header specification is requirements evidence, not implementation evidence

The homepage header document specifies interface components, labels and behaviors. A requirement may use a stable label such as a header, navigation control or account action, but a UI string is not a definition of a shared technical/governance concept. Likewise, “shall” or “must” in a design file establishes an intended requirement; it does not establish that the current HTML/CSS/JavaScript, deployed site, accessibility semantics, keyboard behavior or responsive rendering implements it correctly.

**Required action:** map shared project terms in public UI requirements to the canonical register where useful, and keep purely presentational labels in the UI vocabulary rather than inflating the domain ontology. During the public-use audit, verify the actual implementation and capture the exact commit/build/surface tested. Review visible text, accessible name, link/button purpose, keyboard/focus semantics, responsive behavior and the state exposed to users against the approved requirement. Do not claim implementation or accessibility conformance from the markdown specification alone.

## 3. Positive controls to preserve

- Public-facing marketing copy and technical statements are distinct evidence categories.
- Product intent, current implementation and externally verified performance/licence/legal status must remain separate.
- The homepage specification should remain a source of intended UI requirements; changes to labels must be checked for user comprehension and shared terminology consistency.
- No public claim is promoted to verified merely because it appears in an approved-looking document.

## 4. Limitations

- This review did not browse/render the production or preview website, inspect live page text, test keyboard/screen-reader behavior, or independently validate legal statements.
- The complete ISO 704:2022 text remains unavailable as a controlled audit baseline; no clause-level result is assigned.
- Both assessments are preliminary and require human validation.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Reviewed public-claim controls and homepage header requirements against exact main-branch blob identifiers.
