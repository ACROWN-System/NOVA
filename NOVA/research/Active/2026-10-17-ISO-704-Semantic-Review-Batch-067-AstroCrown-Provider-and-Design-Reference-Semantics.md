# Semantic Review Batch 067 — AstroCrown Provider and Design-Reference Semantics

**Document ID:** NOVA-ISO704-SEM-B067  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Review lens:** concept relations and ordering, controlled terminology for provider lifecycle/verification, source-version traceability of extracted design references, and accuracy of terms such as “current”, “candidate”, “intermediate”, “verified” and “approved”. This is an ISO 704 preparation review, not a formal clause-by-clause assessment. No ISO clause mapping or conformity claim is made.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B067-01 | `development/gpu-infrastructure/NOSANA-INFERENCE-ADAPTER.md` | `fdcbc82d2e8b3039ed510696a288c34735055c2c` | Extends SWEEP-F-0009 |
| B067-02 | `development/gpu-infrastructure/README.md` | `1cb4c8b813b94ec90f39be0fa2c19bd819d2f6bc` | No unique finding |
| B067-03 | `development/index-reference/BORDERS-AND-RADIUS.md` | `ea00e8f99c67318c40471ff1d37fc2af2b4b85fb` | Extends SWEEP-F-0038 |
| B067-04 | `development/index-reference/CARDS-CONVENTIONS.md` | `3fbb34e4e5e50bec6fadfa1b586a82582f47e95d` | Extends SWEEP-F-0038 |
| B067-05 | `development/index-reference/COLORS.md` | `e64d8e3093ac7c09d266dc116f0781edb1f15b57` | Extends SWEEP-F-0038; opens SWEEP-F-0043 |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. The source files were read only and remain unchanged.

## 2. Semantic review results

### B067-01 — Nosana inference adapter candidate

The note correctly distinguishes the adapter candidate from approval of Nosana as AstroCrown's permanent GPU provider. It records the advertised OpenAI-compatible base URL and operations, explains that the served-model list is dynamic, names the credential by environment-variable name only, and explicitly refuses to assume unlimited or zero-cost GPU capacity. The provider credential and operational-readiness boundary are clear positive controls.

However, it calls the document status `candidate / externally verified interface` and describes the Nosana API as the current interface used by the NOVA RSI proposer implementation. Existing SWEEP-F-0009 records that, at the same reviewed baseline, `rsi_policy.json` and `provider_client.py` use Groq / `GROQ_API_KEY_01`, while the RSI implementation runbook contains contradictory Groq/Nosana configuration. The adapter document is additional evidence of the same terminology/configuration conflict. Its source URL does not state when the provider documentation was checked, so “externally verified” should not be read as evidence of a live end-to-end integration test or a permanent API contract.

**Disposition:** extend SWEEP-F-0009 to include this adapter record. Human maintainers must reconcile the intended provider against one approved revision and distinguish documented-interface review from runtime/integration verification. No provider call was made.

### B067-02 — GPU infrastructure README

The README presents GPU infrastructure as a shared, development-only capability subsystem, distinguishes it from the AI media-generation application, and says provider, model, capacity and performance remain candidates until backed by evidence. Its reuse language is conditional and does not force application coupling or claim a provider is already approved.

**Disposition:** no unique finding. The README's subsystem/application boundary and candidate qualification language are useful positive controls.

### B067-03 — Borders and radius reference index

The file identifies itself as an extracted navigation aid rather than a replacement for originating requirements and explicitly preserves original status, including candidate/TBD/undefined states. It cites selected ranges from `HOMEPAGE-REQUIREMENTS.md` and preserves the warning that extracted candidate technologies are not automatically approved.

Those references identify the source filename and line ranges, but do not identify the source commit, content hash, or extraction date. Since `development/HOMEPAGE-REQUIREMENTS.md` is not present at the reviewed baseline, a reader cannot confirm which revision those line ranges describe or reliably detect drift. This extends SWEEP-F-0038's source-and-requirement traceability concern; it does not establish the historical source never existed.

**Disposition:** extend SWEEP-F-0038. Add immutable provenance for the source revision and a maintainable relation from each extraction to that exact source; retain the disclaimer that this index is not the requirement source.

### B067-04 — Cards conventions reference index

The card reference carefully distinguishes a preferred three-card direction from approved implementation requirements. It preserves uncertainty around sentiment consensus methods, agreement/spread formulas, mover-ranking logic, influence strength, weighting, confidence and update cadence. It warns against inferring causation from influence and preserves current/stale/missing/conflicting/insufficient input distinctions. These are strong conceptual boundaries: the same numerical form does not guarantee semantic comparability, and an absent provider must not silently become zero.

Like the borders index, it identifies source ranges from `HOMEPAGE-REQUIREMENTS.md` but does not pin the source to a commit or hash. The reference contains substantial extracted content, so the missing source identity creates an ongoing traceability/drift question even though the file expressly says it is only a navigation aid.

**Disposition:** extend SWEEP-F-0038. The card definitions, concepts and candidate statuses themselves have no additional unique finding in this batch.

### B067-05 — Colors reference index

The index does important semantic work by assigning distinct intentions to brand Gold, Warning Yellow, the blue hierarchy, positive/negative financial states, structural borders and readable text. It explicitly retains AstroCrown Space Blue as TBD and says it must be evaluated against the other blues and accessibility criteria rather than picked by name, midpoint arithmetic or preference alone.

A relationship in the extracted R-005 text contradicts the intended three-level hierarchy described immediately above it. The file defines `#081426` (Deep Space Blue) as the darkest blue and `#16345A` (Light Space Blue) as the lightest blue, with Space Blue intended to be between them. It then says the candidate Space Blue must be “darker than `#16345A` and lighter than `#081426`.” Those two directional relations are reversed: `#081426` has lower red, green and blue channel values than `#16345A` and is the darker endpoint. The intended intermediate should be lighter than `#081426` and darker than `#16345A`, subject to the approved color model and visual/accessibility verification.

The index, like the other design-reference indexes, cites line ranges in `HOMEPAGE-REQUIREMENTS.md` without an immutable source revision. The source being absent at the reviewed baseline therefore also extends SWEEP-F-0038.

**Disposition:** SWEEP-F-0043 — reversed relative-lightness relation in the blue hierarchy. Human review must confirm the intended relation and update the controlled source/extract through the approved process; this batch does not change the design values or approve any Space Blue candidate.

## 3. Findings

### SWEEP-F-0043 — AstroCrown Space Blue lightness relation is reversed

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/index-reference/COLORS.md`, extracted R-005 “Visual system” hierarchy.
- **Observed issue:** The text defines `#081426` as Deep Space Blue/darkest and `#16345A` as Light Space Blue/lightest, then requires the intermediate Space Blue to be darker than `#16345A` and lighter than `#081426`. This places the proposed value outside rather than between the stated endpoints under the intended lightness relation.
- **Interpretation:** The relation terms `darker than` / `lighter than` invert the stated concept hierarchy. As written, a maintainer could select a candidate with the wrong relative lightness while believing R-005 had been followed.
- **Required action:** Verify the approved endpoint order, correct the relation wording in the authoritative requirement and dependent extracted index, and pin their provenance. Keep Space Blue TBD until it passes the separately required rendered hierarchy, distinction and accessibility evaluation.
- **Closure evidence:** Human-approved source revision with correct relation direction; synchronized index extraction; recorded color-model/rendered-state evaluation and applicable contrast evidence. Do not resolve this only by choosing a HEX value without defining and verifying the relationship.

## 4. Existing findings extended

### SWEEP-F-0009 — Groq versus Nosana configuration conflict

Batch 067 adds `AstroCrown-Web/development/gpu-infrastructure/NOSANA-INFERENCE-ADAPTER.md` as another affected reference. It labels Nosana as the current interface used by the RSI proposer, while prior same-baseline evidence recorded in F-0009 says the RSI policy/client select Groq and the implementation runbook has contradictory credential/endpoint guidance. The adapter does call itself a candidate and does not approve a permanent provider, so the issue is conflicting current-state wording, not proof that Nosana cannot work. Human maintainers should reconcile the approved provider and clearly distinguish documentation/contract review from actual integration evidence.

### SWEEP-F-0038 — Homepage requirement source identity and extracted-reference traceability

Batch 067 adds `development/index-reference/BORDERS-AND-RADIUS.md`, `development/index-reference/CARDS-CONVENTIONS.md`, and `development/index-reference/COLORS.md`. Each cites source line ranges from `HOMEPAGE-REQUIREMENTS.md` without a source commit/blob hash or extraction date. Because the source path is absent at the reviewed baseline, the extracted indexes cannot be tied unambiguously to a specific originating revision or used to verify that the extracts still match that revision. The files' disclaimers that they are indexes—not replacements—are positive safeguards, but do not close the provenance gap. Preserve the extracted content and status; a human maintainer should supply immutable source provenance or an approved retained replacement, not reconstruct the missing source by guessing.

## 5. Counts, limitations and safety boundary

- Row-derived post-batch counts: **251 preliminary full-file reviews + 5 partial targeted screens + 62 not reviewed = 318 active paths**.
- Human validation remains pending for all 251 preliminary full-file reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- The review records a concept-relation defect and updates two existing source/configuration traceability findings; it does not treat candidate terminology as approved terminology or infer API operation from documentation.
- All five target blob SHAs match the exact recorded baseline entries.
- No AstroCrown-Web source/runtime file, backup/archive path, workflow, test, credential, provider call, billing or repository setting was changed. No GPU capacity, live interface or color rendering test was performed.
- Scope remains proposed and not human-approved. Controlled lawful access to the full applicable ISO 704 standard remains a prerequisite for formal clause mapping.