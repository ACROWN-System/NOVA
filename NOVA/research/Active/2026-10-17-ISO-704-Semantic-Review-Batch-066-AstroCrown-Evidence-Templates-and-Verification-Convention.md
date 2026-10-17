# Semantic Review Batch 066 — AstroCrown Evidence Templates and Verification Convention

**Document ID:** NOVA-ISO704-SEM-B066  
**Date:** 2026-10-17  
**Review status:** PRELIMINARY FULL-FILE REVIEW — human validation required  
**Scope status:** PROPOSED / NOT HUMAN-APPROVED  
**Baseline rule:** All five target files were reviewed at AstroCrown-Web `main` tree baseline commit `5faea74dd1b40ec98acf9d59d9e404fc18122032`, not at the active assessment PR head.  
**Review lens:** Concept and designation clarity, separation of classification dimensions, concept-to-requirement traceability, controlled meanings of result/status terms, and alignment between a stated verification claim and its evidence. This is ISO 704 preparation, not a formal clause-by-clause assessment. The full applicable standard remains unavailable for controlled review in this workstream; no clause mapping or conformity claim is made.

## 1. Target manifest and source identity

| ID | Exact source path | Verified baseline blob SHA | Disposition |
|---|---|---|---|
| B066-01 | `development/audit/templates/FACT-OBSERVATION-RECORD.md` | `e7e527050f2d9485201b6b31f59949228d1d5427` | SWEEP-F-0041 |
| B066-02 | `development/audit/templates/TEST-CASE.md` | `8f4fc0167353b3e336e2444fa2f6e2a40e48b1b4` | No unique finding |
| B066-03 | `development/audit/tests/HOMEPAGE-BASELINE.md` | `cf588fd90ecf6510a4f32e4a19f1d249f11f9dcf` | Extends SWEEP-F-0038 |
| B066-04 | `development/audit/tests/SECURITY-BASELINE-TESTS.md` | `fda3f291aa504034e7ce868ec6dd0b5779acd94f` | SWEEP-F-0042 |
| B066-05 | `development/DEVELOPMENT-AND-AUDIT-CONVENTION.md` | `f38d9d823c947740be1ecc8b145a132442d4dd3a` | No unique finding; positive control |

All five exact-path blob SHAs fetched at the recorded baseline match the tracker. The source files were read only and remain unchanged.

## 2. Semantic review results

### B066-01 — Fact observation / research evidence template

The template is comparatively strong at separating an observation from a source's claim and from inference; it requires source identity, version/date, acquisition provenance, uncertainty, reproducibility, source multiplicity, use rights, evidence retention, and amendment history. It repeatedly warns that a label or hash does not by itself establish legal permission, truth, authorship, or ownership.

One top-level field, `Primary category`, nevertheless puts distinct classification dimensions in one single-choice list: epistemic/evidential kinds (`FACT-OBSERVATION`, `SOURCE-CLAIM`, `HYPOTHESIS-INFERENCE`), methodological/material kinds (`GENERAL-PRINCIPLE-METHOD`, `EXPRESSIVE-MATERIAL`, `LICENSED-COMPONENT`), information-handling status (`CONFIDENTIAL-RESTRICTED`), and an uncertainty/state pair (`UNKNOWN-BLOCKED`). These classes are not mutually exclusive and are not at one conceptual level. For example, one source can make a claim, contain expressive material, be confidential, and remain unverified at the same time. Other fields record some of those dimensions separately, but there is no rule for selecting one `primary` label or representing multiple simultaneous classifications.

**Disposition:** SWEEP-F-0041 — classification scheme mixes dimensions in one primary-category field. A maintainer should separate the axes or define explicit, non-overlapping category rules and a multi-label/primary-selection policy. The review does not prescribe a final taxonomy.

### B066-02 — Verification test template

The template asks for objective, project criterion, external reference and versioned reference ID, preconditions, method, expected result, actual result, one of four outcome states, evidence/version and re-test. This provides useful fields for connecting an intended criterion to an observed result. The shared development convention defines PASS, FAIL, N/A and BLOCKED, so the template's compact result checklist has a discoverable definition elsewhere in the same development documentation set.

**Disposition:** no unique finding. In future use, external references should be identified at the correct version and tests should point to the exact requirement concept they verify, rather than only repeating a broad topic label.

### B066-03 — Homepage baseline verification matrix

The matrix turns `R-001` through `R-013` into individual tests and describes methods for page structure, accessibility, security, scroll behavior and release evidence. It usefully states that a missing verification method is not PASS, and that conditional techniques should be explicitly scoped.

At the reviewed baseline, `development/HOMEPAGE-REQUIREMENTS.md` does not resolve, while this matrix refers to its `R-001`–`R-013` identifiers without reproducing the requirement names or giving an immutable historical reference. Consequently a reviewer can read the test activity but cannot recover from this baseline the exact requirement concept, boundaries and approved wording each `R-###` represents. This corroborates and extends SWEEP-F-0038; it does not establish that the requirements artifact never existed at the earlier historic audit date.

**Disposition:** extend SWEEP-F-0038 to include this test matrix as a dependent traceability artifact. Preserve the test IDs; resolve the source-reference/history without guessing or silently authoring replacement requirements.

### B066-04 — Security baseline test inventory

The inventory identifies 15 named control areas and an evidence type for each. It is a useful inventory of what needs inspection, but it does not itself state a verification procedure, acceptance condition or executed result for each row. A result in the companion dated security audit therefore needs to be judged against its stated evidence, not against the inventory's title alone.

In particular, SEC-015 is named `Recovery after compromise`, and its inventory asks for a `Backup and restore process`. The corresponding dated security audit marks SEC-015 PASS because versioned backup structure and recovery-oriented backup copies exist. That evidence establishes backup artefact presence, but by itself does not demonstrate that recovery from compromise was successfully rehearsed or that a restoration was verified. The distinction matters because `recovery capability` is a stronger concept than `backup availability`.

**Disposition:** SWEEP-F-0042 — recovery assurance is recorded as PASS from evidence of backup existence without recorded restore/recovery verification. This is a preliminary evidence-semantic finding, not proof that recovery is impossible or that a restore was never tested outside the inspected record.

### B066-05 — Development and audit convention

The convention gives the development work a traceable chain from requirement through implementation, verification, evidence, findings, remediation, re-test and promotion. It defines PASS/FAIL/N/A/BLOCKED; says blocked is not pass; requires versioned external references, evidence identity, criteria, observed conditions and reproduction methods; and explicitly states that a finding is not closed merely because code changed. It distinguishes static, unit, contract, integration and promotion evidence and guards against claiming external compatibility from a local test.

These provisions are useful controlled-vocabulary and evidence-governance practices. The convention also names NIST SSDF, OWASP ASVS and ISO/IEC 25010 with explicit editions/versions and disclaims certification claims. This review did not independently verify external standard contents, current editions, or operational use of the convention.

**Disposition:** no unique finding. Treat the convention as a documented process control, not evidence that each project record follows it consistently.

## 3. Findings

### SWEEP-F-0041 — Fact-evidence template mixes distinct classification dimensions in one primary category

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** `AstroCrown-Web/development/audit/templates/FACT-OBSERVATION-RECORD.md`, field `Primary category`.
- **Observed issue:** One single-choice field places evidential/epistemic classes, material/method classes, confidentiality handling and uncertainty/state classes in the same list, although the classes may apply simultaneously to one source or research record.
- **Interpretation:** The category values are not mutually exclusive and do not occupy one conceptual level. This may produce inconsistent classification and make records incomparable even when they describe the same kind of evidence.
- **Required action:** Separate independent classification axes (for example evidence/evaluation type, material kind, information-handling status and verification state) or document a controlled primary-category rule with permitted secondary labels. Define terms and relations before changing existing records.
- **Closure evidence:** Human-approved concept structure; definitions and inclusion/exclusion rules for each category; examples demonstrating multi-dimensional cases; and a transition rule for existing records.

### SWEEP-F-0042 — Recovery-after-compromise assurance is not distinguished from backup existence

- **Status:** OPEN — preliminary; human validation required.
- **Affected paths:** `AstroCrown-Web/development/audit/tests/SECURITY-BASELINE-TESTS.md` (SEC-015) and `AstroCrown-Web/development/audit/records/SECURITY-AUDIT-2026.09.20-001.md` (SEC-015 result).
- **Observed issue:** The control is titled `Recovery after compromise`, while the audit's PASS evidence only says versioned backup structure and recovery-oriented backup copies exist. The record does not cite a restore exercise, measured recovery outcome, or equivalent evidence demonstrating the recovery function.
- **Interpretation:** The recorded evidence supports existence of backup artefacts, but does not by itself establish recoverability. This is a gap between the control concept implied by the result and the evidence type cited.
- **Required action:** A human security owner should decide whether SEC-015 means backup presence, restore capability, or complete recovery after compromise; define the acceptance criterion accordingly; and record a controlled restoration/recovery exercise if required and authorized. Do not run recovery or alter backups as part of this terminology sweep.
- **Closure evidence:** Approved control definition, explicit acceptance criteria, and traceable evidence matching the chosen meaning. If the test remains unperformed, its status should not imply verified recovery capability.

## 4. Existing finding extended

### SWEEP-F-0038 — Homepage audit references a requirements artifact absent from the reviewed baseline

Batch 066 adds `development/audit/tests/HOMEPAGE-BASELINE.md` as a dependent affected artifact. The verification matrix uses requirement identifiers `R-001` through `R-013`, but the referenced `development/HOMEPAGE-REQUIREMENTS.md` is unavailable at the reviewed main baseline and the matrix does not contain the requirement definitions. A human maintainer should establish an immutable historical reference or approved retained requirement source, preserving the historic baseline and without reconstructing requirements from test descriptions.

## 5. Counts, limits, and safety boundary

- Row-derived post-batch counts: **246 preliminary full-file reviews + 5 partial targeted screens + 67 not reviewed = 318 active paths**.
- Human validation remains pending for all 246 preliminary full-file reviews; formal ISO 704 clause-level assessments completed by this batch: **0**.
- The review explicitly examines concept-category boundaries, requirement-to-test traceability and the difference between backup existence and demonstrated recovery. These observations are preliminary ISO 704-oriented terminology/evidence analysis, not asserted ISO 704 clauses.
- All five target blob SHAs match the exact recorded baseline entries.
- No AstroCrown-Web source/runtime file, backup/archive path, workflow, test, credential, provider call, billing or repository setting was changed. No test, restore, recovery exercise or workflow was executed.
- Scope remains proposed and not human-approved; controlled lawful access to the full applicable ISO 704 standard remains a prerequisite for formal clause mapping.