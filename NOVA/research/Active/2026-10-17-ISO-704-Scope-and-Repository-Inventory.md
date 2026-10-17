# ISO 704:2022 Scope Proposal and Repository Inventory

**Document ID:** NOVA-ISO704-SCOPE-001  
**Version:** 0.1.24  
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

This is a snapshot of active file paths at the recorded Git tree SHAs. The tracker records a selected-term lexical scan of all 318 inventoried active files, with all rows marked `FETCHED_AND_LEXICALLY_SCANNED`. Preliminary semantic reviews have now been recorded for six repository-level README files in [Batch 001](2026-10-17-ISO-704-Semantic-Review-Batch-001-READMEs.md) and five NOVA governance/operational files in [Batch 002](2026-10-17-ISO-704-Semantic-Review-Batch-002-NOVA-Core.md); the five additional NOVA core files are also reviewed in [Batch 002](2026-10-17-ISO-704-Semantic-Review-Batch-002-NOVA-Core.md), and the large 28,490-line NOVA state-ledger README has a separately marked PARTIAL targeted screen in [Batch 003](2026-10-17-ISO-704-Semantic-Review-Batch-003-Large-NOVA-README.md). Currently 94 active files have preliminary full-file reviews, one file has a partial targeted screen, and the other 223 active-file rows remain `NOT_REVIEWED` / `NOT_ASSESSED`. The six preliminary reviews are not human-validated ISO conformity results. The lexical scan does **not** establish that context has been interpreted, all terms have been located, or repository usage is consistent. See the [initial sweep findings](2026-10-17-ISO-704-Initial-Sweep-Findings.md).

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


## 14. Revision history

- **2026-10-17 / v0.1.8:** Added [Batch 008 — Resource Readiness](2026-10-17-ISO-704-Semantic-Review-Batch-008-Resource-Readiness.md), documented the conflicting Hugging Face inference-credit status across two active documents, and reconciled the summary count using row-level statuses. Current counts: 32 preliminary full-file reviews, one partial targeted screen and 285 not reviewed, across 318 rows.


## 15. Revision history

- **2026-10-17 / v0.1.9:** Added Batch 009 reviews of the Cloudflare image qualification record and cross-cutting RSI principle. Current tracker summary: 34 preliminary reviews, one partial screen, 283 not reviewed, across 318 active paths.


## 16. Revision history

- **2026-10-17 / v0.1.10:** Added Batch 010 reviews of provider-error evidence, operational-state controls and key readiness. The tracker now records 37 preliminary file reviews, one partial targeted screen and 280 not reviewed out of 318 active paths.


## 17. Revision history

- **2026-10-17 / v0.1.11:** Added Batch 011 reviews of GPU heartbeat and Weak RSI workflow/test files. The tracker records 41 preliminary content reviews, one partial targeted screen and 276 not reviewed, with human validation pending.


## 18. Revision history

- **2026-10-17 / v0.1.12:** Added Batch 012 review of the provider qualification implementation, its tests and workflow. A cross-source Cloudflare LLM qualification status conflict is now recorded for resolution; current counts are 44 preliminary reviews, one partial screen and 273 not reviewed.


## 19. Revision history

- **2026-10-17 / v0.1.13:** Added Batch 013 reviews of LLM/GPU rosters, health policy and GPU capacity evidence. The candidate catalog schema, legacy naming and Lightning no-card scope are recorded; current counts are 48 preliminary reviews, one partial screen and 269 not reviewed.


## 20. Revision history

- **2026-10-17 / v0.1.14:** Added Batch 014 review of completed Mistral/provider diagnostics, rolling scheduler and Sanctuary roadmap. Current tracker status: 52 preliminary full-file reviews, one partial screen and 265 not reviewed out of 318. The Sanctuary scope and cross-repository path remain unresolved.


## 21. Revision history

- **2026-10-17 / v0.1.15:** Added Batch 015 reviews of the opportunistic probe scheduler, credential validation workflow and manual Cloudflare image qualification workflow. Counts: 55 preliminary full-file reviews, one partial screen and 262 not reviewed; all assessments remain preliminary, and live side effects were not tested.


## 22. Revision history

- **2026-10-17 / v0.1.16:** Added Batch 016 reviews of router, router tests, shared health telemetry and capacity observation helpers. Current row-derived counts: 59 preliminary full reviews, one partial screen and 258 not reviewed.


## 23. Revision history

- **2026-10-17 / v0.1.17:** Added Batch 017 reviews of GPU capacity qualification and tests plus capacity economics tests and expiry-aware scheduling. Current row-derived counts: 63 preliminary full reviews, one partial screen and 254 not reviewed.


## 24. Revision history

- **2026-10-17 / v0.1.18:** Added Batch 018 reviews of scheduler tests, health tests, credential readiness and GPU heartbeat. Current row-derived counts: 67 preliminary full-file reviews, one partial screen and 250 not reviewed.


## 25. Revision history

- **2026-10-17 / v0.1.19:** Added Batch 019 structural/freshness review of `NOVA/health_state.json`. Snapshot is valid JSON but stale under its own six-hour freshness policy as of the assessment date; 68 preliminary reviews, one partial screen and 249 not reviewed remain.


## 26. Revision history

- **2026-10-17 / v0.1.20:** Added Batch 020 review of quality-gate code/tests, reasoning payload validation, and economic accounting. Current row-derived counts: 72 preliminary full reviews, one partial screen and 245 not reviewed.


## 27. Revision history

- **2026-10-17 / v0.1.21:** Added Batch 021 review of action policy, alerts, tests and external-source watchlist. Current row-derived counts: 77 preliminary full reviews, one partial screen and 240 not reviewed.


## 28. Revision history

- **2026-10-17 / v0.1.22:** Added Batch 022 review of economic/pricing policy and state, provider-independent pricing and payment intent, and related tests. Current row-derived counts: 84 preliminary full reviews, one partial screen and 233 not reviewed.


## 29. Revision history

- **2026-10-17 / v0.1.23:** Added Batch 023 review of allocation algorithm/tests, capacity policy, development test budget, dated Gemini/Mistral observations and credential-readiness tests. Current row-derived counts: 91 preliminary full reviews, one partial screen and 226 not reviewed.


## 30. Revision history

- **2026-10-17 / v0.1.24:** Added Batch 025 review of the AstroCrown entity registry, emphasizing separate meanings for necessity, feasibility, credibility, adoption and operability. Current row-derived counts: 94 preliminary reviews, one partial screen and 223 not reviewed.
