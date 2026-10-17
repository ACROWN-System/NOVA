# Active Plan — Preserve Project Quality While Applying ISO 704

**Date:** 2026-10-18  
**Status:** COMPLETED — quality-preservation controls recorded and verified  
**Repository:** ACROWN-System/NOVA  
**Branch:** docs/terminology-governance-iso704-2026-10-17  
**Objective:** Ensure ISO 704 improves terminology clarity, concept integrity, operability and long-term maintainability without degrading useful domain semantics, architecture, documentation, navigation or user outcomes.

## Navigation / sequencing note

The branch tree previously inspected did not expose the repository's named navigation protocol/template at the expected locations. This limitation is recorded rather than claiming compliance with an unavailable template. This plan uses the established task-specific plan structure and is written to the explicitly named review branch; the file will be fetched immediately for same-ref verification after every write.

## Governing principle

**ISO 704 is a method for improving terminology work, not a reason to damage the project in order to make its documents look standardized.** The project aims to obtain useful, precise, coherent and operationally effective terminology, using ISO 704's methods where they materially improve the result. It must not optimize for superficial conformity, standardized-looking form, or the ability to mark a checklist complete at the expense of real project quality.

ISO's published scope describes principles and methods for preparing and compiling terminologies and links among objects, concepts, definitions and designations. It applies across domains, but this does not make every project document, architecture component, interface, workflow, or governance mechanism a terminological entry. Source: https://www.iso.org/standard/79077.html

## Non-regression and quality-preservation requirements

1. **Purpose before form:** understand why a record or distinction exists before changing its form. Never flatten a purposeful architectural/domain distinction merely to make labels uniform.
2. **Preserve semantic richness:** keep necessary nuance, context, rationale, examples, provenance, constraints, assumptions, operational consequences and domain boundaries. A concise canonical definition does not require deleting its supporting explanation.
3. **Preserve operability:** evaluate how proposed terminology changes affect navigation, search/retrieval, discoverability, human understanding, automation, API/data contracts, workflows, traceability, maintenance and backward compatibility.
4. **Prefer additive clarification when safer:** if the confusion is caused by missing context, add a distinct definition, scope note, synonym relation, example, typed relation, or cross-reference instead of destructively rewriting useful content.
5. **Do not over-generalize:** distinguish shared concepts from project/domain-specific concepts; use domain and purpose-related granularity. Keep AI-Sanctuary-Core's identity/governance domain distinct from AstroCrown tokenomics and Space Empire governance.
6. **Evaluate evidence and benefit:** each material proposed change must identify its current problem, evidence, expected quality/operability benefit, alternatives considered (including no change), expected regression risk, validation method, and observable acceptance criteria.
7. **Use explicit dispositions:** ACCEPT when benefit and evidence are adequate; ADAPT when the idea is useful but direct application causes avoidable loss; REJECT when application degrades correctness/usefulness or has no supported benefit; DEFER when evidence is insufficient. Record rationale and residual risk.
8. **Separate standards alignment from a conformance claim:** where project needs motivate a deliberate choice different from a method or provision, document it honestly, preserve the project requirement, assess the trade-off, and do not claim full ISO conformity for an area that has not been shown to conform. Never conceal a conflict or silently relabel it N/A.
9. **Protect existing intent and behavior:** documentation-only harmonization must not silently alter runtime meaning, security boundaries, business rules, permissions, protocol/schema fields, public commitments or architectural ownership. Changes requiring those effects must follow their actual engineering/governance change process.
10. **Measure both sides of the change:** use the project's required Impact Analysis with **IF modified** and **IF not modified**. A change is not justified simply because it makes a standard-mapping row easier to fill.

## Required change-review record

For every material ISO-inspired change, capture:

- Concept / file / domain / exact baseline reference.
- Problem and evidence supporting the problem.
- User or operational need served.
- Proposed change and the ISO 704 method/principle it appears to support (only when evidenced).
- Expected benefits: concept clarity, distinction, retrieval, interoperability, traceability, maintainability, etc.
- Potential losses/regressions: removed nuance, collapsed domains, confusing names, duplicate concepts, navigation burden, migration breaks, runtime/API effects or loss of useful explanatory documentation.
- Alternatives, including keeping the current design and adding only a note/reference.
- Disposition: ACCEPT / ADAPT / REJECT / DEFER.
- Validation: before/after review, example cases, navigation/retrieval check, tests where behavior is affected, and reviewer.
- Residual ambiguity, follow-up owner and retest evidence.

## Decision sequence

1. Identify the real terminology or concept problem without assuming that unfamiliar, domain-specific or long-form wording is wrong.
2. Confirm intended meaning and use with existing documentation, architecture, users/workflows, and authoritative evidence.
3. Separate the canonical concept definition from richer explanation, examples, constraints, implementation notes and governance rationale; preserve each layer when it serves a distinct purpose.
4. Apply ISO 704 methods visible in reliable source material to the terminology layer where useful.
5. Compare current and proposed states against explicit quality/operability criteria.
6. Review non-regression and impact, then accept/adapt/reject/defer with written rationale.
7. Update references, cross-links, aliases/synonyms, migrations and dependent records as appropriate.
8. Re-review resulting text in its actual repository/domain context and confirm no intended meaning or operability was lost.

## Boundaries

- This policy does not authorize ignoring any actual mandatory requirement in an eventual complete-standard assessment while still claiming full conformity. If a real conflict appears, document it transparently and separate project-quality judgment from any claim of ISO conformity.
- Public previews support only source-bounded assessment of provisions directly visible. Unseen sections remain NOT ASSESSED.
- Do not rewrite work simply to increase apparent standards coverage or counts of “resolved” findings.
- No paid activity is authorized. External certification remains outside the objective.
- Immutable backup/archive paths remain excluded.

## Impact Analysis

**IF this plan is applied:** ISO 704 can strengthen the precision and usefulness of project terminology while protecting domain-specific intent, operability and documentation quality. Changes become evidence-based, reversible where practical, and reviewable for benefit and regression.

**IF this plan is not applied:** the project risks cargo-cult standardization: superficial uniformity, loss of nuance, degraded navigation or domain semantics, and a false sense of quality because documents appear easier to classify.

## Exit criteria

- The core terminology-governance record includes the non-regression rule and its decision sequence.
- The public-preview partial map says it is a tool for improvement, not a blanket mandate to restructure unrelated project architecture or delete explanatory content.
- The complete-matrix template requires quality/impact rationale for recommended project actions, and permits disposition of project responses without faking the standard's own requirement or claim.
- Tracker metadata records the principle without rewriting the 318-path review counts.
- PR #124 summary reflects the quality-preservation rule.
- Every write specifies the branch and is immediately verified by fetching the exact path on the same ref.
- This plan is moved to Completed only after all updates and the PR body are verified.



## Completion record — 2026-10-18

### Results

- Added the quality-preservation/non-regression control to the canonical [terminology-governance record](2026-10-17-ISO-704-Terminology-Governance.md), blob `85387ec5825e15fea67789e3ff4b682777f4a73d`.
- Added the explicit project-quality guardrail to the [public-preview partial mapping](2026-10-18-ISO-704-Public-Preview-Partial-Mapping.md), blob `d9c11b3aef99874ef158de7e1bcee41ba07d33a2`.
- Added rationale, non-regression, alternatives and ACCEPT / ADAPT / REJECT / DEFER fields to the [complete matrix template](2026-10-17-ISO-704-Clause-Evidence-Matrix.md), blob `cd76e9d87d6535d25826825b1ac5e5b05e43cc39`. The matrix remains template-only; this change does not make it a completed assessment.
- Added the same change-quality gate to the [readiness dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md), blob `a76fefcc6bc3071300a1a423e4826acb9f3b21b4`, and recorded the policy in the [machine-readable tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json), blob `00358e356b994f0c96a1244922c2a4cc2154e5a8`. Sweep counts were not changed.
- Updated [draft PR #124](https://github.com/ACROWN-System/NOVA/pull/124). The PR remains open and draft; 96 changed paths are listed, and the refreshed changed-path list contains no backup/archive paths.
- Every write explicitly named the review branch and was immediately verified by fetching the exact path on that branch. No source/runtime file, workflow, credential, provider operation, repository permission, paid service or backup/archive path was changed.

### Remaining safeguards

- This is a project quality/non-regression rule, not permission to ignore an actual verified ISO requirement while claiming full conformity.
- Source-bounded preview work remains partial; provisions not directly visible remain NOT ASSESSED.
- Each substantial change still requires evidence, an intended benefit, alternatives including no change, risk of regression, verification criteria, a disposition and the IF-modified / IF-not-modified impact analysis.
- The $0-only policy remains binding; no certification-provider discovery/contact or paid activity is authorized.

### Impact Analysis

**IF applied:** ISO 704 can improve conceptual clarity, consistency, retrieval and operability without needlessly discarding domain-specific meaning or useful explanatory documentation.

**IF not applied:** superficial uniformity may replace actual quality, degrade project-specific semantics and operability, and create a misleading appearance of compliance.
