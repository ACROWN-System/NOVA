# Branch-Integrity Incident — File Creation Targeted the Default Branch

**Incident ID:** NOVA-ISO704-TOOLING-INC-001  
**Date:** 2026-10-17  
**Status:** RECOVERED IN REPOSITORY STATE; HISTORICAL MAIN-BRANCH COMMITS RETAINED  
**Affected repository:** `ACROWN-System/NOVA`  
**Intended branch:** `docs/terminology-governance-iso704-2026-10-17`  
**Related change:** [NOVA PR #124](https://github.com/ACROWN-System/NOVA/pull/124)

## 1. Summary

Four supplementary audit-readiness documents were created with an intended draft-branch target, but the file-creation action committed them to the default branch instead. The mismatch was detected during final diff verification because the files could be read from the default branch but were not present at the expected paths on the draft branch or in the PR's changed-path list.

This was a branch-integrity process failure. The documents were not runtime changes, and no file under any backup/archive directory was involved.

## 2. Affected paths

- `NOVA/research/Active/2026-10-17-ISO-704-Certification-Context-Review.md`
- `NOVA/research/Active/2026-10-17-ISO-704-Register-Quality-Review.md`
- `NOVA/research/Active/2026-10-17-ISO-704-Pilot-Entry-Review-HSIAN.md`
- `NOVA/research/Active/2026-10-17-ISO-704-Concept-Relation-Map-Draft.md`

## 3. Detection evidence

- A fetch against the intended draft branch did not resolve the newly created paths.
- The PR changed-file list initially omitted those paths.
- The default-branch tree showed the paths existed there.
- This mismatch was treated as a stop condition rather than assuming the requested `branch` parameter had worked.

## 4. Root-cause assessment

**Observed cause at the integration boundary:** the GitHub file-creation action did not deliver the new files to the intended branch, despite the branch being supplied. The exact internal connector/API behavior that caused the parameter to be ignored or misapplied has not been independently diagnosed; do not claim more specific technical root cause than the evidence supports.

**Process weakness that enabled the incident:** the workflow initially trusted the action's success result without immediately verifying the exact path at the requested branch ref and checking the PR changed-path list. The post-action branch verification was delayed until final validation.

## 5. Recovery performed

1. Re-fetched the exact four documents from the branch where the content existed.
2. Constructed a Git tree based on the current NOVA PR #124 head, created a commit whose parent was that exact PR head, and advanced the intended draft branch using an expected-head check.
3. Removed only the four unintended active research paths from `main`, each through an exact-path deletion with the current file SHA and explicit `main` target.
4. Re-fetched the PR and compared the draft branch and default-branch trees.
5. Verified all four paths are present on the draft branch and listed in PR #124, and absent from the current `main` tree.
6. Verified the PR's complete changed-path list contains no backup/archive path.

The corrective deletion commits remain in the shared `main` history. No force-push or history rewrite was attempted because rewriting shared branch history would be a more destructive action than retaining the add/remove history while restoring the current tree state.

## 6. Prevention / required control

Effective immediately for repository file operations:

1. **For new files on non-default branches, prefer the explicit Git-tree → commit → ref-update sequence**, with the current intended branch head as parent and an expected-head guard, rather than trusting a generic create-file action to honor its branch parameter.
2. After every file creation or update, immediately fetch the exact path from the intended branch/ref and compare the returned content/blob SHA with the intended result.
3. Fetch the relevant PR changed-file list and verify the new/changed path appears in the PR.
4. For cross-repository work, repeat the same verification in each repository and each intended ref; a successful API response alone is not enough.
5. Before concluding any change, compare the entire changed-path list against the immutable backup/archive boundary, including case variants, dated mirrors and names such as `index-archive/`.
6. If the result ref does not match the requested ref, stop further writes, preserve the evidence, determine the actual target, restore the intended tree state, record the incident, and verify recovery before proceeding.

A new default-branch file must not be considered safely delivered merely because an action returned a commit SHA. The path, ref, tree state and PR diff are the acceptance evidence.

## 7. Impact and residual risk

**Current tree state:** the four affected paths are on the intended PR branch and not present on current `main`. PR #124 now lists all 13 intended NOVA paths. No backup/archive path was changed.

**Historical state:** the temporary default-branch commits and recovery deletions remain visible in `main` history. This incident record intentionally preserves that history rather than attempting an unapproved history rewrite.

**Residual limitation:** this incident record documents one observed integration failure and a preventive method. It does not prove the method is infallible; the verification steps above remain mandatory.

## 8. Revision history

- **2026-10-17 / v0.1.0:** Recorded the observed branch-target failure, recovery and mandatory verification controls.
