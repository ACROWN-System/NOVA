# ISO 704:2022 Scope Proposal and Repository Inventory

**Document ID:** NOVA-ISO704-SCOPE-001  
**Version:** 0.1.7  
**Snapshot date:** 2026-10-17  
**Status:** PROPOSED SCOPE / INITIAL PATH INVENTORY — human approval and detailed content review pending  
**Related dossier:** [ISO 704:2022 Audit-Readiness Dossier](2026-10-17-ISO-704-Audit-Readiness-Dossier.md)  
**Machine-readable evidence:** [Active Path Inventory JSON](2026-10-17-ISO-704-Active-Path-Inventory.json); [File-by-File Content Sweep Tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json); [Initial Sweep Findings](2026-10-17-ISO-704-Initial-Sweep-Findings.md)

## 1. Proposed audit scope

For planning, the proposed scope is the controlled terminology work and terminology use of the six currently accessible non-archived repositories in the ACROWN-System GitHub organization, limited to active non-backup/non-archive content and relevant terminology in technical artefacts, documentation, product descriptions, website/UI strings and public claims.

The proposed cross-repository source of truth is NOVA's canonical register and governance procedure. Each repository remains a distinct domain; inclusion does not mean all repositories share the same economics, governance authority or legal status. In particular, AI-Sanctuary-Core's stated separation from AstroCrown tokenomics and Space Empire governance must remain explicit in concept definitions and domain relations.

This scope is **not yet frozen or approved**. In particular, the AI-Sanctuary-Core README's assertion that it is outside AstroCrown audits conflicts with its provisional inclusion here; the protocol files were reviewed only provisionally, and no inclusion decision is inferred. The designated human maintainer must approve the final entity/scope wording, domains, repository list, paths, activities, languages, period and exclusions before the evidence matrix can be treated as complete.

## 2. Repository baseline

The following default-branch tree snapshots were retrieved from GitHub's Git database on 2026-10-17. The counts are path inventory evidence, not a completed content audit.

| Repository | Baseline tree SHA | Active files inventoried | Files excluded under immutable backup/archive directories | Proposed terminology domain |
|---|---|---:|---:|---|
| [NOVA](https://github.com/ACROWN-System/NOVA) | `2a1f5c496474aa099703432e99b3d3dfddfd3fd7` | 96 | 0 | Canonical terminology, governance, technical architecture and project-level definitions |
| [Freebies-](https://github.com/ACROWN-System/Freebies-) | `795153408b796412fa8b929cc9ba3090aeb5946d` | 3 | 0 | Public resources, tutorials, templates and smart-contract examples |
| [AstroCrown_ACS_MC_Spec](https://github.com/ACROWN-System/AstroCrown_ACS_MC_Spec) | `b5df828b53eb9c14e97ed857adeea8eb0a728285` | 3 | 0 | ACS and Monte Carlo technical/economic specification |
| [AI-Sanctuary-Core](https://github.com/ACROWN-System/AI-Sanctuary-Core) | `8ca3adab836117106257ee1d0c2e74d258d4e3fd` | 8 | 0 | Separate AI Sanctuary identity/governance domain, without implying integration into AstroCrown tokenomics |
| [ACROWN-SIMULATION-LAB](https://github.com/ACROWN-System/ACROWN-SIMULATION-LAB) | `35f150a971f7500812f1657e53a2a27a0f23700d` | 8 | 0 | Simulation models, scenarios, definitions and results |
| [AstroCrown-Web](https://github.com/ACROWN-System/AstroCrown-Web) | `5faea74dd1b40ec98acf9d59d9e404fc18122032` | 200 | 843 | Public website, brand language, UI/documentation and product claims |

**Inventory totals:** 6 repositories; 318 active files inventoried; 843 files under immutable backup/archive directories excluded. GitHub reported no truncated tree response for these six snapshots.

## 3. Immutable backup/archive boundary

- Never create, update, rename, move or delete a file under any backup/archive directory, regardless of capitalization.
- Treat dated system mirrors, nested archive directories and names such as `index-archive/` as immutable when they are backup/archive locations.
- The machine-readable inventory records only active file paths and blob SHAs; excluded archive paths are not listed individually.
- The active-path content sweep must not use a backup/archive file as a target for correction. If historical information is relevant, preserve it read-only and record the scope limitation.
- Before every proposed change and the final package snapshot, compare changed paths against the complete repository tree and affirm that no immutable path changed.

## 4. Coverage limits and exclusions to resolve

This is a snapshot of active file paths at the recorded Git tree SHAs. The tracker records a selected-term lexical scan of all 318 inventoried active files, with all rows marked `FETCHED_AND_LEXICALLY_SCANNED`. Preliminary semantic reviews have now been recorded for six repository-level README files in [Batch 001](2026-10-17-ISO-704-Semantic-Review-Batch-001-READMEs.md) and five NOVA governance/operational files in [Batch 002](2026-10-17-ISO-704-Semantic-Review-Batch-002-NOVA-Core.md); the five additional NOVA core files are also reviewed in [Batch 002](2026-10-17-ISO-704-Semantic-Review-Batch-002-NOVA-Core.md), and the large 28,490-line NOVA state-ledger README has a separately marked PARTIAL targeted screen in [Batch 003](2026-10-17-ISO-704-Semantic-Review-Batch-003-Large-NOVA-README.md). Currently 29 active files have preliminary full-file reviews, one file has a partial targeted screen, and the other 289 active-file rows remain `NOT_REVIEWED` / `NOT_ASSESSED`. The six preliminary reviews are not human-validated ISO conformity results. The lexical scan does **not** establish that context has been interpreted, all terms have been located, or repository usage is consistent. See the [initial sweep findings](2026-10-17-ISO-704-Initial-Sweep-Findings.md).

The inventory includes all non-archive blobs regardless of file extension so that file types are not excluded merely because their content format is unfamiliar. During the audit, classify each file as applicable text/content, non-text asset, generated artefact, secret-bearing/restricted material or justified exclusion; record the reason and reviewer. Do not treat a file as non-applicable solely from its extension.

The current inventory is based on each repository's `main` snapshot and does not include the current draft-branch content for NOVA PR #124 or AstroCrown-Web PR #135. Once the documentation changes are reviewed/merged—or a different intended assessment ref is approved—refresh the final inventory and record exact commit SHAs.

Languages: English is the initial authored language in the current draft framework. The scope must state whether the initial assessment is English-only or includes every active locale. Do not claim localization equivalence without reviewed evidence.

## 5. Next scope actions

1. Human approval of the provisional six-repository scope, with domain separation preserved.
2. Confirm whether any additional repositories, deployments, published websites, social/public communication channels or externally maintained term systems are within the target scope; the six repositories above are the currently accessible organization inventory, not automatic proof that every external use is covered.
3. Decide and record the language/locale boundary for the first assessment.
4. Classify each active path in the machine-readable inventory and perform the full content sweep within the approved scope.
5. Use the [file-by-file content sweep tracker](2026-10-17-ISO-704-Content-Sweep-Tracker.json) to record content reviews. Its extension/path hints are not audit findings; inspect actual content and preserve objective evidence.
6. Refresh the path inventory at the frozen assessment commit before completing the audit package.

## 6. Current disposition

**AR-E01 — Scope and boundaries: DRAFT / NOT APPROVED.** Repository discovery has produced an initial evidence-backed inventory. Content coverage, scope approval, language boundaries and final assessment refs remain open. No certification provider has been searched for or contacted as part of this readiness-first workstream.


## 7. Revision history

- **2026-10-17 / v0.1.1:** Reconciled the scope narrative with the machine-readable tracker: all 318 active paths have a lexical scan, but none of the 318 content-review assessments is closed. Scope approval remains pending.


## 8. Revision history

- **2026-10-17 / v0.1.2:** Corrected the narrative to reflect the tracker after the first semantic review batch: six README files preliminarily reviewed; 312 active-file content assessments remain open; scope approval and human validation are still pending.


## 9. Revision history

- **2026-10-17 / v0.1.3:** Updated the narrative after Batch 002: 11 files now have preliminary content-review records; 307 active-file reviews remain outstanding. All assessments remain preliminary and the scope is still not human-approved.


## 10. Revision history

- **2026-10-17 / v0.1.4:** Recorded preliminary review of five NOVA core paths and a partial targeted screen of `NOVA/README.md`. The README remains partial because it contains a large operational/status-report dataset whose factual claims and scope are not fully reviewed.


## 11. Revision history

- **2026-10-17 / v0.1.5:** Recorded preliminary review of the Freebies MIT licence and token-example contract in [Batch 004](2026-10-17-ISO-704-Semantic-Review-Batch-004-Freebies.md). The “open-source/free forever” and “ERC-20/BSC ready” public claims remain evidence-gated; no code/security or ISO conformity test was performed.


## 12. Revision history

- **2026-10-17 / v0.1.6:** Reviewed the ACS/Monte Carlo specification and licence in [Batch 005](2026-10-17-ISO-704-Semantic-Review-Batch-005-ACS-MC-Spec.md). The spec baseline ends midway through section H while claiming sections A–P; this internal source-completeness issue blocks treating the document as an authoritative complete spec until a reviewed restoration is evidenced.


## 13. Revision history

- **2026-10-17 / v0.1.7:** Updated counts after Batch 006 (Simulation Lab) and Batch 007 (AI Sanctuary). The 29 preliminary reviews include all eight inventoried paths in each of those repositories. AI Sanctuary remains a human scope-decision blocker; 289 active-file content reviews remain and one large state-ledger file remains only partially screened.
