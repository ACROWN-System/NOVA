# Active Plan — Open Pull Request and Issue Reconciliation

**Date:** 2026-10-18  
**Status:** ACTIVE — reconciliation in progress  
**Repository:** ACROWN-System/NOVA  
**Branch:** docs/terminology-governance-iso704-2026-10-17  
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

