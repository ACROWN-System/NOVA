# ISO 704:2022 Preliminary Semantic Review — Batch 001 (Repository READMEs)

**Review ID:** NOVA-ISO704-SEM-B001  
**Date:** 2026-10-17  
**Status:** AI-ASSISTED PRELIMINARY REVIEW COMPLETE FOR THESE SIX README FILES; HUMAN REVIEW REQUIRED  
**Scope baseline:** default-branch snapshot dated 2026-10-17; exact file blob IDs below  
**Method:** read full README content, assess declared purpose, term usage, boundaries, externally meaningful claims, evidence links and missing scope information.  
**Important boundary:** No ISO 704 clause-level conclusion is made because the complete edition has not been established as a controlled baseline. This is a content-review batch, not an independent audit or certification finding.

## 1. File-by-file disposition

| Batch item | Repository and path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B001-01 | NOVA / `README.md` | `09b016d29ad0502163006ca55836a439474fcb26` | REVIEWED — terminology conflict / naming-rollout finding open |
| B001-02 | Freebies- / `README.md` | `1fabb69d08419705fad2588465b1300f75888b0d` | REVIEWED — public claim substantiation required |
| B001-03 | AstroCrown_ACS_MC_Spec / `README.md` | `8c27b0f89844f3a3d8e8294e7ef27f8671dcead2` | REVIEWED — description insufficient to identify terminology scope |
| B001-04 | AI-Sanctuary-Core / `README.md` | `dc77e9d36d1ddd9de926e6414f4b0562efcc3d5f` | REVIEWED — conflict between stated domain boundary and proposed umbrella scope |
| B001-05 | ACROWN-SIMULATION-LAB / `README.md` | `7a06a6862634add8f631b33101e0b45e32ef7829` | REVIEWED — description contains title only; inspect the other active files before scope decision |
| B001-06 | AstroCrown-Web / `README.md` | `e046dab7b187949e1d9a5becf9a0c895fcb7c0bd` | REVIEWED — concise project and brand/licence boundaries; public-content review remains open |

The source files are identified by exact baseline blob SHA and public links:
- [NOVA README](https://github.com/ACROWN-System/NOVA/blob/main/README.md)
- [Freebies README](https://github.com/ACROWN-System/Freebies-/blob/main/README.md)
- [ACS/Monte Carlo specification README](https://github.com/ACROWN-System/AstroCrown_ACS_MC_Spec/blob/main/README.md)
- [AI Sanctuary Core README](https://github.com/ACROWN-System/AI-Sanctuary-Core/blob/main/README.md)
- [Simulation Lab README](https://github.com/ACROWN-System/ACROWN-SIMULATION-LAB/blob/main/README.md)
- [AstroCrown-Web README](https://github.com/ACROWN-System/AstroCrown-Web/blob/main/README.md)

## 2. Observations and findings

### B001-F01 — NOVA README has live HAAN naming

The baseline README names “HAAN” in the foundational mission and lists HAAN among protected brand identifiers. This is inconsistent with the stated project decision to use HSIAN for new naming, although legacy/history links may remain valid. The active naming transition through NOVA PR #122 and AstroCrown-Web PR #134 was still pending at this evidence snapshot.

**Required action:** review and resolve the named dependent PRs in the correct order; then repeat the active-path search and label each remaining occurrence as current, deprecated, or legitimately historical. Do not change backup/archive records. This is a project-terminology consistency finding, not an ISO clause result.

### B001-F02 — Freebies README contains unbounded public wording

The README identifies the resources as open-source and says they are designed to be “free — forever”; it also says the minimal token can be deployed “in minutes.” This wording may be intended as brand copy, but the README itself does not provide an evidence boundary covering every current/future resource, external asset, maintenance cost, availability dependency or user environment.

**Required action:** verify per-file licensing and the scope of “open-source”; ensure the free-forever promise has an authorized, realistic scope or rewrite it to describe the present intended offer without an unsupported perpetual guarantee. Substantiate or qualify deployment-time wording. This requires public-claim review and is not a finding that the claims are necessarily false.

### B001-F03 — ACS/Monte Carlo README is not a usable scope description

The entire README is a title and the phrase “AstroCrown ACS &amp; Monte Carlo Design Spec multiple version.” It does not identify the authoritative document, applicable version, purpose, status, source hierarchy or which definition governs ambiguous design terms; the literal entity spelling also appears to be an editorial artifact.

**Required action:** review the other two active paths in this repository and propose a README that points to the authoritative specification/version history and states status and scope. Do not infer token/economic definitions from this short README.

### B001-F04 — AI Sanctuary scope boundary needs a human decision

The AI-Sanctuary-Core README describes the repository as an independent, non-financial domain and explicitly says it is not part of AstroCrown tokenomics or Space Empire governance; it also states that it is outside AstroCrown audits. The current proposed ISO terminology scope includes this repository because it is among the six accessible organization repositories.

**Required action:** human maintainer must resolve this scope tension before the umbrella scope is frozen. Options to assess are (a) separate it from the AstroCrown/NOVA audit and document an explicit exclusion, or (b) declare a separately scoped terminology audit of its own terminology while preserving its stated governance/economic independence. Inclusion in one terminology review must not imply the two systems share governance authority or financial meaning. Until decided, AR-E01 remains BLOCKED.

### B001-F05 — Simulation Lab README provides no scope information

The README contains only the repository title. It does not identify its terminology domains, canonical model/spec sources, status or intended audience.

**Required action:** inspect the other seven active paths and derive the scope from authoritative content, not the title. Record any missing source-of-truth link; only then decide the applicability of individual terminology controls.

### B001-F06 — AstroCrown-Web README has a useful licence/brand distinction

The baseline README identifies the website project and states that the MIT software licence does not automatically relicense third-party assets or grant rights to brand identifiers. This is a useful boundary between software licence and brand ownership. It does not, by itself, establish that every file/asset notice or every live public claim is correct.

**Required action:** when the assessment refs are frozen, ensure the merged terminology governance guide is navigable from the source-of-truth branch and sample actual site/UI content, asset notices, product descriptions, accessibility text and public claims. The main-branch README reviewed here did not yet include the new guide link at this baseline.

## 3. Cross-file finding summary

1. **Naming alignment:** active HAAN references remain in NOVA main; dependent HSIAN rollout is pending.
2. **Evidence-backed public copy:** Freebies' “free forever” and “in minutes” language needs explicit scope and substantiation.
3. **Scope adequacy:** two project READMEs (ACS/Monte Carlo and Simulation Lab) do not provide enough information for audit scoping.
4. **Domain separation:** AI Sanctuary's declared exclusion from AstroCrown audits conflicts with the proposed six-repository umbrella scope. Human scope decision is mandatory.
5. **Good practice to preserve:** AstroCrown-Web's separation of source-code licensing and brand identifiers should be cross-checked against actual assets and notices.

## 4. Tracker and status reconciliation

For these six baseline README files only:
- Content has been read and a preliminary semantic review recorded in this batch.
- Individual tracker rows are updated to distinguish this preliminary review from an accepted internal audit result.
- No tracker status is a statement of ISO 704 conformity.
- Human validation, exact scope approval and follow-up closure remain open.
- The remaining 312 active-path content reviews are not completed by this batch.

## 5. Scope, limitations and backup boundary

The initial umbrella scope is still proposed. These README reviews do not resolve the AI Sanctuary scope conflict, declare the six-repository scope human-approved, test live/deployed surfaces, or inspect the 312 other active files. No backup/archive path has been reviewed for modification or changed by this batch. Backup/archive locations remain excluded and immutable.

## 6. Revision history

- **2026-10-17 / v0.1.0:** Preliminary semantic review of the six repository-level README files, with exact baseline blob identifiers and follow-up findings.
