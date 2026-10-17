# Semantic Review Batch 079 — AstroCrown Verification Status, Paths and Subsystem README

**Document ID:** NOVA-ISO704-SEM-B079  
**Review date:** 2026-10-18  
**Baseline repository:** ACROWN-System/AstroCrown-Web  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Review status:** Preliminary full-file semantic review; designated human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report makes no conformity or nonconformity claim.

## Method and limits

Five active documents were reviewed from the pinned baseline commit. Each fetched blob SHA matched its tracker record. The review examined concept boundaries, designation consistency, status/evidence-state distinctions, relation wording, cross-references and claim scope. This was a static document review only. No source file in AstroCrown-Web was changed; no tests, workflows, runtime code, credentials, provider calls, billing, repository settings or immutable backup/archive contents were executed, changed or inspected.

The batch-specific plan records the navigation/template lookup limitation and sequencing deviation. The existing terminology-governance plan states that standalone `NAVIGATION-PROTOCOL.md` and `NAVIGATION-PLAN-TEMPLATE.md` were not located in inspected active paths; likely root and `NOVA/` paths were retried without resolution. The batch plan therefore records scope, evidence, impact and verification explicitly without claiming strict use of an unavailable template.

## Source manifest and dispositions

| ID | Exact source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B079-01 | `development/verification/operations/STATUS-ENUM.md` | `0ac4d7b7ba37282894aa5e6aed1ffda23bb1d23c` | Opens SWEEP-F-0062 — “CANDIDATE” is used in two separate state dimensions with distinct intended meanings, but capitalization alone distinguishes the values. |
| B079-02 | `development/verification/operations/VERIFICATION-TRACKER.yaml` | `37fd81670d62f0316770d504ab0e1352490ae143` | Positive control for separating `evidence_state` from `operational_status`, preserving unknown/conflicting evidence, and defining refresh triggers. Cross-references SWEEP-F-0061 for schema constraints and SWEEP-F-0062 for state-value semantics. |
| B079-03 | `development/verification/paths/README.md` | `4f14816cb884473a71a576f9d80733ee300520da` | Positive control: “path” is contextualized as an external verification execution route; trigger-driven use is preferred over assumed lifecycle stages. |
| B079-04 | `development/verification/paths/VERIFICATION-PATHS.md` | `57306113d9999b5a15cfc2e6c0a8b0a9792eb931` | Useful pathway sequence and domain-specific routes. A few compact slash/composite labels (for example, “Entity/pathway”) could be made more explicit, but no additional finding was opened in this batch. |
| B079-05 | `development/verification/README.md` | `f8b0e26c35f2c0b547c0e7c3aab396f9a9cfa9bb` | Positive control for separating verification intelligence from records of actual audit activity and for explicitly preventing internal simulations from being represented as external decisions/certifications. |

## Semantic review results

### B079-01 — Verification Status Vocabulary

The document distinguishes **evidence states** (`VERIFIED`, `DERIVED`, `CANDIDATE`, `UNKNOWN`, `BLOCKED`) from **operational statuses** (for example, `Researching`, `Planned`, `In Progress`, `Passed`, `Failed`, `Expired`, `Superseded`, `Blocked`). That is a valuable conceptual separation: an evidence assessment and an activity’s lifecycle stage are not the same kind of property.

However, `CANDIDATE` appears as an evidence-state value and `Candidate` appears as an operational-status value. The document says the dimensions are separate, but does not define each operational value or provide typed codes/field-qualified examples. Capitalization is the only visible distinction between these two same-word values. A reader or downstream consumer that case-folds values could conflate “evidence is candidate” with “activity is at the Candidate stage.” This is a distinct semantic ambiguity from the structural-schema gap in SWEEP-F-0061.

**Disposition:** open preliminary SWEEP-F-0062. Define the two meanings separately, provide stable field-qualified or namespace-qualified values, and document allowed transitions/usage where relevant. Do not silently collapse or rename existing values without human approval and a migration decision.

### B079-02 — Verification Tracker YAML

The tracker explicitly declares separate `evidence_state` and `operational_status` dimensions. Its controls preserve unknowns and conflicts, prohibit converting blocked to pass, prohibit treating rankings as verification, and require provenance and date-sensitive refresh. It identifies a detailed entity registry as the source of richer entity records and calls itself the operational control layer, reducing the risk of silently duplicating the full registry.

The file lists required record fields and controlled values, but does not itself define their data types, cardinality, null/unknown/N/A handling, or cross-field validation. This supports the previously opened SWEEP-F-0061 rather than creating a duplicate finding. The same lexical collision between evidence-state `CANDIDATE` and operational-status `Candidate` remains visible in the declared vocabularies and supports SWEEP-F-0062.

**Disposition:** positive controls plus cross-references to SWEEP-F-0061 and SWEEP-F-0062; no separate finding.

### B079-03 — Verification Paths README

The title and content frame “paths” as external verification execution routes rather than filesystem paths. The text states that detailed routes belong in this area once they have enough implementation detail, gives examples across exchange, regulatory, audit, research and media pathways, and favors trigger-driven entry rather than an assumed fixed lifecycle stage.

This is concise and conceptually useful. The terms “path” and “pathway” are used near one another; a future glossary may choose one preferred term and explain any distinction, but the reviewed text gives enough local context to avoid opening a separate finding.

**Disposition:** positive control; no unique finding.

### B079-04 — Verification Paths

The pathway model gives an ordered sequence: entity/pathway, trigger, prerequisites, evidence package, execution, result, publication/evidence retention, expiry/change detection and re-verification. The domain-specific examples cover security, formal verification, bug bounty, exchange readiness, regulatory work, research, reserve assurance and media. The principle that stage is secondary to trigger is consistent with the paths README and the tracker’s date-/change-triggered review cycle.

The slash construction “Entity/pathway” is compressed and could be expanded into an explicit relation between a verified entity and its applicable pathway; other sequences could also identify whether arrows mean temporal order, dependency or required transition. Those are editorial precision opportunities, not independently established errors in the present context. No additional finding was opened.

**Disposition:** positive control with a low-priority wording improvement opportunity; no unique finding.

### B079-05 — Verification Intelligence README

The README describes the subsystem’s role and points to registries, standards, assessments, evidence, benchmarks, paths and operational records. It distinguishes the intelligence layer—which discovers and prepares possible verification mechanisms—from `development/audit/`, which records actual audit/verification activity, including scope, criteria, method, evidence, findings, remediation, re-test and closure.

The evidence rules expressly preserve provenance, conflict, uncertainty and version/date scope. They prohibit converting UNKNOWN to FALSE, CANDIDATE to FACT or BLOCKED to PASS, and prohibit representing internal NOVA simulation as external certification, audit, regulatory, exchange, accounting or editorial decisions. These are strong controls against concept-category and authority confusion.

The subsystem’s broad verb list (“evaluate, validate, audit, benchmark, review, certify, challenge, monitor, rank”) includes activities with different authority and evidentiary force, but the text’s subsequent boundary statements prevent reading all of them as equivalent outcomes. This batch did not establish a concrete contradiction requiring a separate finding.

**Disposition:** positive control; no unique finding.

## Finding and traceability

### SWEEP-F-0062 — “Candidate” is overloaded across evidence-state and operational-status dimensions

- **Status:** OPEN — preliminary; human validation required.
- **Affected paths:** `development/verification/operations/STATUS-ENUM.md`; `development/verification/operations/VERIFICATION-TRACKER.yaml`.
- **Observed issue:** The evidence-state enumeration includes `CANDIDATE`; the operational-status enumeration separately includes `Candidate`. The intended dimensions are stated to be separate, but the same lexical value is distinguished only by capitalization, and the reviewed files do not provide a complete field-qualified definition/example for each use.
- **Interpretation:** “Candidate evidence” and “an activity whose operational status is Candidate” are different concepts. A case-insensitive reader, normalization step or untyped record could conflate them, causing ambiguity in reports, filtering, validation or lifecycle interpretation. This is a value-semantics issue; SWEEP-F-0061 separately concerns the absence of a normative structural schema.
- **Required action:** Define every evidence-state and operational-status value within its own dimension; use field-qualified examples and stable namespace/code values or another unambiguous representation. Document transition/usage rules where applicable. Review existing records and consumers before adopting any migration; do not assume the two meanings should be merged.
- **Closure evidence:** Human-approved definitions and field/value bindings; examples showing `evidence_state: CANDIDATE` separately from `operational_status: Candidate`; validation against case normalization or equivalent downstream handling; and evidence that affected records/consumers preserve the distinction.

## Batch disposition and counts

- Active paths in proposed scope: **318**
- Preliminary full-file reviews after Batch 079: **311**
- Partial targeted screens: **5**
- Not yet reviewed: **2**
- Human validation of preliminary reviews: pending
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: proposed; human approval pending

Arithmetic: 311 + 5 + 2 = 318.

This is a preliminary semantic review, not a formal ISO 704 clause assessment, conformity statement or certification claim.
