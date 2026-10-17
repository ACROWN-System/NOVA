# Active Plan — Open Pull Request and Issue Reconciliation

**Date:** 2026-10-18  
**Status:** COMPLETED — all mergeable/reviewable PRs processed; one draft retained for visual acceptance  
**Repository:** ACROWN-System/NOVA  
**Plan branch at creation:** docs/terminology-governance-iso704-2026-10-17  
**Scope:** Open pull requests and issues across the six user-approved planning repositories.  
**Objective:** Merge correct, verified changes in dependency order; correct materially stale or unsafe documentation/code; keep valid but unreviewable work explicitly pending; preserve issue history; close only with a truthful disposition.

## Process note

The named NAVIGATION-PROTOCOL.md and NAVIGATION-PLAN-TEMPLATE.md were not located in the inspected NOVA branch tree during prior work; that limitation remains disclosed. This plan follows the current task-plan/impact-analysis conventions. Every repository write must explicitly name its target branch and be immediately verified by fetching the exact path with that same ref.

## Scope and safety controls

- Repositories: NOVA, Freebies-, AstroCrown_ACS_MC_Spec, AI-Sanctuary-Core, ACROWN-SIMULATION-LAB and AstroCrown-Web.
- No backup/archive paths may be read as active targets, modified, moved, renamed or deleted.
- No paid service, external billable channel, provider credential, billing setting or live LLM/GPU probe may be used merely to verify a documentation/issue-management change.
- Preserve issue bodies and pull-request history; close with comments and appropriate reason rather than delete.
- Follow PR dependencies explicitly; do not merge a consumer/documentation PR before its canonical source PR.
- Apply quality/non-regression: changes must improve correctness or operability and not simply make docs look standardized.
- Drafts awaiting a necessary real-world/user review must remain open and explain the exact blocker.

## Repository evidence reviewed

- NOVA #128 was created to fix repeated provider-health issue flooding, add model-specific structured-response-contract gating, and keep automated health alerts on GitHub (not potentially chargeable SMS/voice). Both push and PR test workflows passed on exact PR HEAD `22365074ea946b86b3f2e6419bccd3bb69af981f`; it merged to main as `653e51ae0154e8b77b5d8a29c3ba8a47642c8f54`. Main health tests and the post-merge heartbeat/validation completed successfully.
- NOVA #122 was reviewed as a documentation-level canonical HSIAN mission/name change. Its PR and push health-test workflows passed on exact HEAD `83e3c5a580c9137569dd6f6c9da6fa7fe5bf226a`; its roster update was reconciled with #128 so merged model-contract gates were preserved. It merged as `61c0f4c2a22677d1349ecabad2a1b00035810a6f`.
- The NOVA automated-health issue backlog contained 63 historical alerts. They have been closed with comments and their original bodies retained: 4 Mistral alerts as NOT PLANNED under its existing deferment; 26 Groq 120B and 22 Gemini 3.8 Flash alerts as NOT PLANNED while those model-specific response contracts are blocked pending requalification; and 11 historical Groq 20B alerts as COMPLETED on the strength of a later exact-contract PASS, explicitly noting that the evidence is stale under the six-hour freshness rule. The repository API showed zero open NOVA issues after this reconciliation.
- NOVA #124 is a 96-file documentation/research package. Its exact-head CI passed, its changed paths are active governance/research documents only, no backup/archive path appears in its diff, and no runtime/source path overlaps with #128 or the #122 set. Its content explicitly calls the review preliminary, leaves 0 formal full-standard clause assessments complete, records remaining evidence gaps and does not claim conformity/certification. Before merge, current canonical files must be corrected for the latest scope and HSIAN dependency facts.
- AstroCrown-Web #134 depends on NOVA #122 and updates active documentation links/names; #122 is now merged and #134's exact-head CI passed.
- AstroCrown-Web #135 depends on NOVA #124 for canonical terminology source files; its terminology guide and PR body have been corrected to treat certification as outside the current objective and to preserve quality/non-regression.
- AstroCrown-Web #133 is a development-only homepage visual prototype. CI passed, but its own scope leaves visual appearance, responsive behavior and browser interaction review outstanding. Automated CI cannot substitute for actual visual acceptance, so it should remain draft/open.

## Required changes before completing the review

1. Update the canonical terminology standard so internal terminology quality/operability and evidence-backed alignment are the objective, not external certification. Provider discovery/contact must remain outside scope unless explicitly authorized later.
2. Update the canonical terminology register so it no longer says NOVA #122 is unmerged; keep rollout pending only where dependent AstroCrown-Web #134 still has work to merge and verify.
3. Update current readiness/access language so complete-text/full-matrix limitations remain explicit but do not stop source-bounded improvements; retain dated historical findings rather than silently rewriting the original snapshot meaning.
4. Refresh NOVA #124's PR body with the accurate changed-file count and current scope/dependency order. Re-fetch the body and the full changed path list.
5. Merge PRs only after the exact current HEAD is clean/mergeable and its relevant CI is successful: #124 before #135; #122 before #134 (already met). Leave #133 open/draft because visual acceptance is genuinely outstanding.
6. Complete the reconciliation plan and record final PR/issue status after the current body and source files are re-fetched and verified.

## Impact Analysis

**IF completed:** current source-of-truth documents match the approved human objective, dependencies are correctly sequenced, duplicated health alerts no longer obscure live faults, and issue history remains auditable.

**IF not completed:** stale PR references or outdated certification-goal wording could mislead future agents/reviewers; automated issues could again flood the backlog or use an external cost channel; dependent docs might be promoted before their canonical sources are available.



## Completion record — 2026-10-18

### Final pull-request dispositions

| PR | Repository | Disposition | Evidence / limitation |
|---|---|---|---|
| [#128 — Stop NOVA health-alert floods and gate failing model contracts](https://github.com/ACROWN-System/NOVA/pull/128) | NOVA | **MERGED** | Merge commit `653e51ae0154e8b77b5d8a29c3ba8a47642c8f54`. Exact-head PR tests passed; post-merge health tests and autonomous heartbeat passed. The change blocks unverified model/JSON response contracts before provider calls, deduplicates same-title alerts, emits on transition into UNACCEPTABLE, and keeps routine alerts on GitHub (no potentially billable SMS/voice). |
| [#122 — Adopt HSIAN canonical mission/name](https://github.com/ACROWN-System/NOVA/pull/122) | NOVA | **MERGED** | Merge commit `61c0f4c2a22677d1349ecabad2a1b00035810a6f`. Exact-head PR and push health-test runs passed. The branch roster was reconciled before merge so model-specific contract gates from #128 were preserved. |
| [#124 — Establish terminology governance aligned with ISO 704:2022](https://github.com/ACROWN-System/NOVA/pull/124) | NOVA | **MERGED** | Merge commit `c88159dca28e3e4fc7e8d3482cd4eb81bb9a899d`. 97 active governance/research paths, no backup/archive paths. Exact-head NOVA Health Tests passed. The merged documentation labels the content sweep preliminary, preserves missing artifacts/open findings, records zero formal complete-standard clause assessments, separates internal quality/conformance from certification, and carries the quality-preservation/non-regression control. This is not a claim that NOVA conforms fully to ISO 704. |
| [#134 — Align active documentation with HSIAN cognitive extension](https://github.com/ACROWN-System/AstroCrown-Web/pull/134) | AstroCrown-Web | **MERGED** | Merge commit `035f82c43dcdc5ef0dab3fb72c4cc15bbbee8b10`. Merged after NOVA #122 and after verifying the canonical HSIAN mission path exists on NOVA main. Three exact-head AstroCrown-Web CI workflows passed. The explanation on the completed-plan mirror was preserved; no backup/archive path was changed. |
| [#135 — Define AstroCrown brand language and terminology governance](https://github.com/ACROWN-System/AstroCrown-Web/pull/135) | AstroCrown-Web | **MERGED** | Merge commit `a7a3bd68f1fe65d7c5a545bb32a504122c97dd6a`. Three exact-head CI workflows passed. NOVA #124's canonical standard/register paths were fetched from main before merge. The guide states quality-first internal alignment and treats certification/provider discovery as outside current scope unless separately authorized. |
| [#133 — Build desktop-first homepage visual review prototype](https://github.com/ACROWN-System/AstroCrown-Web/pull/133) | AstroCrown-Web | **RETAIN OPEN / DRAFT** | Exact-head CI passed: NOVA RSI Engine, External Review Pipeline and CodeQL at `d4a4acc506c28cb4bbcbaa35048e2a67924d4874`. The current PR description's preview links now use that candidate SHA. The preview is development-only, with `_config.yml` explicitly excluding `development/` from the public Pages output. Real-browser visual appearance, responsive layout and full keyboard interaction have not been inspected here or accepted; keep the PR open until a human reviews the current preview and decides whether the design should be retained/promoted. This is the only remaining open PR, deliberately not closed just to reach zero. |

### Final issue disposition

An organization-wide GitHub search returned **0 open issues** across ACROWN-System. The 63 NOVA automated health-alert issues were closed with comments; the original issue bodies were retained and not deleted:

- 4 Mistral: `not_planned` under the already documented provider deferral; not a recovery claim.
- 26 Groq `openai/gpt-oss-120b`: `not_planned` for a reversible model-specific structured-JSON contract block pending requalification; not a provider-level outage or permanent-quality claim.
- 22 Gemini `gemini-3.8-flash`: `not_planned` for a reversible model-specific contract block pending requalification; not a provider-level outage claim.
- 11 historical Groq `openai/gpt-oss-20b`: `completed` because a later exact-contract PASS resolved those past episodes. Closure comments explicitly note that the PASS is stale under the six-hour health-freshness policy and does not guarantee present availability.

### Verification and preservation

- Re-fetched the merged PR metadata and current PR bodies; all five processed PRs are merged and verified by GitHub, while #133 remains open/draft.
- The cross-repository open-PR search returns the one justified draft above; the open-issue search returns zero results.
- No backup/archive paths were touched. The #124 change list had 97 paths and no backup/archive paths; the #133 change set is limited to development prototype and its preservation record.
- Routine alert correction and issue closure did not use paid channels or initiate external-provider requests. No paid service or certification-provider activity was undertaken.
- The repository checklist has not independently reviewed every source line in every PR in the same manner as an external audit; each merged PR's scope and own test/review evidence are recorded above. #133 remains unresolved for its specific visual acceptance gate.

### Impact Analysis

**IF this reconciliation is retained:** mergeable, evidence-backed changes are integrated in dependency order, the automated alert storm is addressed at root cause, canonical sources are corrected, issue history remains auditable, and the only open item has a concrete acceptance blocker.

**IF this reconciliation is not retained:** future work may repeat already-merged changes, depend on stale branch snapshots, close issues without cause, or treat a draft visual prototype as accepted solely because CI passed.
