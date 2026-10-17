# Semantic Review Batch 075 — AstroCrown Verification Opportunity, Visibility, Credibility, Adoption and Replication Registries

**Document ID:** NOVA-ISO704-SEM-B075  
**Review date:** 2026-10-18  
**Baseline repository:** ACROWN-System/AstroCrown-Web  
**Baseline commit:** 5faea74dd1b40ec98acf9d59d9e404fc18122032  
**Review status:** Preliminary full-file semantic review; human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report makes no conformity or nonconformity claim.

## Method and limits

Five complete Markdown files were fetched at the pinned baseline commit and their returned blob SHAs matched the tracker. The review considered concept scope, classification axes, definitions and relationships among readiness, visibility, credibility/trust, adoption, replicability and external authority. No runtime code, workflows, external services, credentials, billing, settings or backup/archive paths were changed, executed or inspected.

## Source manifest and dispositions

| ID | Exact source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B075-01 | development/verification/06-OPPORTUNITY-READINESS.md | f7c4f804fac71de3e1574c91fd22ca7bc373a569 | Preliminary review; no unique finding. |
| B075-02 | development/verification/07-VISIBILITY-REGISTRY.md | 08c6a5d7f24488f36483d973077e9ff234575257 | Preliminary review; no unique finding. |
| B075-03 | development/verification/08-CREDIBILITY-REGISTRY.md | 838860c1b04895a82d61e9340b893b1a3aee167b | Preliminary review; no unique finding. |
| B075-04 | development/verification/09-ADOPTION-REGISTRY.md | 2be563e078728e6b2c9d9b45007e0f43fcff10d4 | Preliminary review; no unique finding. |
| B075-05 | development/verification/10-NOVA-REPLICATION-REGISTRY.md | 245001b081ae3c925e6a95bc0f9f35ce740cf15f | Opens SWEEP-F-0055 for mixed classification axes in the replication-state field. |

## Semantic review results

### B075-01 — Opportunity readiness

The opening statement rejects a fixed Development-to-Institutional ladder and instead models opportunities through triggers, evidence, stage timing and preparation gaps. The records distinguish earliest practical stage, typical stage and latest useful stage, while acknowledging that some opportunities can be stage-independent or continuous. This separates opportunity timing from an assumed universal lifecycle.

The “Stage independent?” column uses values such as Yes, Sometimes and Usually, without explicit criteria for those qualitative judgments. As the registry is a planning aid rather than a controlled pass/fail decision, this is retained as a point for owner clarification; no unique finding was opened. These values should not be converted into an automated gate without approved meaning.

### B075-02 — Visibility registry

The file distinguishes visibility mechanisms from visibility dimensions such as direct publication, algorithmic ranking, search/discovery exposure, editorial coverage, community amplification and institutional reference. It explicitly states that visibility is not equivalent to credibility and that public ranking is not legal or security assurance. Requiring date, source, scope/population, methodology and limitations is a useful evidence boundary.

Some mechanisms are expressed at different operational levels, but the document is descriptive and does not claim that its values form a mutually exclusive classification. No unique finding was opened.

### B075-03 — Credibility / Trust registry

The registry identifies scope, methodology, accountable evaluation, reproducible evidence, limitations, version anchoring, retesting and monitoring as attributes that can support trust. It then explicitly distinguishes certification, attestation, audit, benchmark, regulatory status, listing, publication, reputation and community evidence, and warns that no single mechanism answers every trust question.

The combined title “Credibility / Trust” and phrase “strongest trust-bearing mechanisms” could be operationalized with more explicit concept definitions and selection criteria if used for comparative scoring. On this preliminary review, the file's explicit distinctions among assurance mechanisms are retained as a positive control; no finding is opened solely on the title.

### B075-04 — Adoption registry

The file distinguishes adoption impact from visibility and credibility and cautions that stars, followers, membership and engagement are adoption signals, not independent evidence of quality, security, legality or trustworthiness. Its rule against inferring causal adoption effects without evidence limits overclaiming. No unique terminology finding was opened.

### B075-05 — NOVA replication registry

The table usefully identifies what NOVA can reproduce and what it cannot legitimately claim for each methodology family. It preserves the distinction between internal preparation and an independent external decision or assurance.

However, the column named “NOVA replication state” combines values from different conceptual axes: extent of replication (FULL, PARTIAL), a non-replicability boundary (NOT REPLICABLE), combined or qualified states (FULL / PARTIAL), and a mixed operational/trust statement (FULL workflow / PARTIAL trust). Workflow completeness and the degree of independent trust are not the same property, so the mixed value cannot be compared directly with the other state values. This can make rows inconsistent and obscure what is being measured.

**Disposition:** open preliminary SWEEP-F-0055; human validation required.

## Finding and traceability

### SWEEP-F-0055 — NOVA replication-state field combines different classification axes

- **Status:** OPEN — preliminary; human validation required.
- **Affected path:** development/verification/10-NOVA-REPLICATION-REGISTRY.md, column “NOVA replication state”.
- **Observed issue:** The column combines replication extent (FULL/PARTIAL), NOT REPLICABLE, qualified states such as FULL / PARTIAL, and “FULL workflow / PARTIAL trust”, which combines operational workflow maturity with trust/independence.
- **Interpretation:** Replication extent, feasibility boundary, workflow maturity and external independence/trust are distinct properties. Current values are not directly comparable along one classification axis.
- **Required action:** Define the replication-state concept and permitted values, or separate the table into independent fields for replication extent/feasibility, internal workflow maturity, and external independence/authority boundary. Preserve the existing caution that internal replication does not confer external authority.
- **Closure evidence:** Human-approved concept definitions and classification rules, examples for each field, reviewed/migrated rows, and consistency checks against approved value sets.

## Batch disposition and counts

- Active paths in proposed scope: **318**
- Preliminary full-file reviews after Batch 075: **291**
- Partial targeted screens: **5**
- Not yet reviewed: **22**
- Human validation of preliminary reviews: pending
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: proposed; human approval pending

Arithmetic: 291 + 5 + 22 = 318.

This is not a formal ISO 704 clause assessment, conformity statement or operational verification of NOVA.
