# ISO 704:2022 Preliminary Semantic Review — Batch 025 (AstroCrown Entity Registry)

**Review ID:** NOVA-ISO704-SEM-B025  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT REVIEW COMPLETE FOR ONE FILE; HUMAN VALIDATION REQUIRED  
**Baseline:** `development/verification/02-ENTITY-REGISTRY.md` on AstroCrown-Web main  
**Baseline blob SHA:** `356a39485404f2fa3d4e97c23bf1591c43636116`  
**Boundary:** Review of the registry's status dimensions and relationship to canonical terminology; this is not verification of every listed entity or a legal opinion.

## 1. Registry role and scope

This document is a verification/entity registry, not the shared canonical terminology register and not a certificate/accreditation register. Its row dimensions include separate concepts such as necessity, feasibility, credibility, adoption and operability. Those dimensions answer different questions and should not be collapsed into one general “verified” state.

The file can support traceability for entities and verification decisions, but its existence does not by itself prove that every row's underlying external claim is current or that each entity is adopted/operational. Any later reuse of a row in public claims or terminology records must retain its own scope and evidence.

## 2. Finding

### B025-F01 — Registry status dimensions must remain separate from concept approval and implementation state

Necessity, feasibility, credibility, adoption and operability are distinct dimensions. A candidate may be necessary but infeasible; credible but not adopted; adopted as a project decision but not yet operational; or operational for a narrow scope without external certification. A generic row status must not erase these differences.

**Required action:** retain the dimension-specific fields and document a glossary for their exact allowed values and evidentiary meaning. Where a row says “verified” or equivalent, preserve the exact claim, source, assessed scope and observation/review date if present; do not translate that label into “ISO 704 conformant”, “certified”, “implemented” or “approved by an external standards body” unless separate evidence directly supports that stronger claim. Link any shared project concept to its canonical term ID without duplicating or silently redefining that concept.

## 3. Positive controls to preserve

- The registry's multi-dimension structure is better than a single boolean readiness field.
- Entity-level verification should remain separate from definition/term approval in the canonical register.
- Adoption and operability must remain distinguishable, so a project decision does not become a claim of deployed functionality.
- External verification records should remain traceable to their evidence scope rather than being copied as timeless facts.

## 4. Limitations

- The reviewed file is one registry artifact; this batch did not independently recheck every entity's external source or verify the state of any website/service.
- No repository-wide claim sweep was performed here.
- This is a preliminary content review, not a clause-level ISO 704 result. The complete standard baseline remains blocked.

## 5. Revision history

- **2026-10-17 / v0.1.0:** Reviewed the entity registry's multi-dimension status semantics against the exact main-branch blob.
