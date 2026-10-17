# ISO 704:2022 Preliminary Semantic Review — Batch 027 (AstroCrown Prompt Guidance and Development Navigation)

**Review ID:** NOVA-ISO704-SEM-B027  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR TWO FILES; HUMAN VALIDATION REQUIRED  
**Boundary:** This is a documentation/terminology review, not proof of generated output correctness, deployment state, legal conformity or ISO 704 clause conformity.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B027-01 | `development/Prompt-Guide.md` | `18a8d42e5f238b8b570f5fb9b63d82c86df63c08` | REVIEWED — development prompting guidance; prompt text is not verification evidence |
| B027-02 | `development/README.md` | `55c932a042029fb234d215e388bc617305d73ae0` | REVIEWED — navigation/index guidance; path discovery does not establish implementation or document approval |

## 2. Findings

### B027-F01 — Prompt instructions must remain subordinate to canonical definitions and evidence

Prompt guides are instructions for generating, reviewing or changing work; they are not themselves the result of that work. An apparently complete prompt, model-generated explanation, acceptance checklist or summary cannot substitute for inspecting the changed source, running the applicable tests, validating claims against their sources, recording a human decision, or mapping an applicable standard requirement to objective evidence.

**Required action:** when prompt guidance is used for terminology-sensitive changes, include the canonical term-register path/commit, applicable domain specification, actual scope, required evidence type and a rule to mark missing inputs BLOCKED rather than infer them. Keep proposal, draft, tested, approved, deployed and independently verified as distinct statuses. Prompt examples should not override project governance, human authorization, immutable backup boundaries or the approved source of truth.

### B027-F02 — Development navigation is a discovery aid, not a status authority

A README or navigation page can direct readers to the right file, but the link's existence does not prove the target document is approved/current or that a feature is implemented. The terminology guide must remain a proposed source until its canonical dependency is approved and merged; branch-only paths must not be presented as if they already exist in the main branch.

**Required action:** check navigation targets against the exact assessed branch/commit; distinguish proposed/active/completed documents; record missing or stale links; and ensure the eventual audit package references immutable commit/version locations. Do not update any backup/archive index.

## 3. Positive controls to preserve

- Keep requirements and prompt procedures distinct from implementation evidence and independent assessment.
- State the repository/ref/commit, input documents, output artifact and review decision for substantive model-assisted changes.
- Reuse a canonical term entry rather than creating competing definitions in prompts, local README files or public copy.
- Preserve an explicit human gate for consequential or irreversible decisions.

## 4. Limitations

- No prompt was executed and no generated code/output was evaluated in this batch.
- No live website/navigation target was browser-tested.
- No ISO 704 clause is assessed; the complete controlled standard baseline remains blocked.
- Both reviews remain preliminary and require human validation.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Reviewed development prompt guidance and the development navigation README at exact main-branch blob IDs.
