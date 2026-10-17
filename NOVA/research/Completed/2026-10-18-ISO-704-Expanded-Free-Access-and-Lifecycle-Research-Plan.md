# Active Plan — Expanded Search for Lawful No-Cost ISO 704 Access and Latest Edition

**Date:** 2026-10-18  
**Status:** COMPLETED — expanded public-source search recorded; full-text access remains blocked  
**Repository:** ACROWN-System/NOVA  
**Branch:** docs/terminology-governance-iso704-2026-10-17  
**Decision constraints:** Six-repository planning scope approved; English initial assessment language; $0-only access policy.  
**Objective:** Search public and institutional sources for lawful no-cost access to the complete applicable ISO 704 text; distinguish selected-section preview from full text; verify the latest published edition and assess the surfaced ISO/PWI 704 proposal without treating it as a released standard.

## Navigation and sequencing note

The prior completed no-cost access check was limited to the official ISO product page and official BIS pages. In response to the human maintainer's request for a broader internet search, expanded research began before this task-specific plan was added. This sequencing deviation is disclosed. The existing repository navigation-protocol/template lookup limitation remains as documented in the terminology-governance plan. This plan governs the remaining searches, findings record, and repository updates.

## Scope and source categories

1. Official ISO product page, Online Browsing Platform (OBP) help/preview rules, and the public ISO/TC 37/SC 1 work programme.
2. Proposal-stage lifecycle records from a national standards body; separate proposal status from official published edition status.
3. Official GSO (GCC Standardization Organization) preview/store system, its preview documentation and published access/licensing policy.
4. BIS library and national-standards portal information.
5. Public/university library standards subscriptions (including institutional access restrictions and any lawful open-reader option).
6. General indexed-web discovery for exact-title copies, with copyright/distribution authorization assessed before any source is classified as a lawful no-cost full-text route.

## Method and constraints

- Do not download, store, reproduce, or redistribute the copyrighted standard from any source unless lawful access/usage rights are established.
- A publicly reachable URL or a full-looking search snippet does not establish authorization to distribute; classify the source and its permitted scope first.
- Do not treat a preview, table of contents, abstract, selected clauses, a draft/proposal, or a national adoption as the complete applicable ISO edition.
- Do not purchase, join a paid library membership, start a subscription, submit a billable enquiry, hire a provider/adviser or incur any cost.
- If no lawful no-cost route is verified, keep AR-E02 BLOCKED and the clause matrix template-only.
- No code/runtime, credentials, settings, provider operations or immutable backup/archive paths may be changed or inspected as part of this research.

## Impact Analysis

**IF completed:** the access record will distinguish published edition, proposal-stage developments, selected-section preview and lawful complete-text access; the project avoids prematurely stopping at a narrow search or relying on unauthorized copies.

**IF not completed:** the project could miss a legitimate free route, or incorrectly treat a partial preview or unverified online copy as an authoritative controlled baseline.

## Exit criteria

- Record official lifecycle evidence and any proposal-stage lead with dates/status and source.
- Identify which preview sections are exposed and whether the substantive standard clauses/annexes are absent.
- Determine whether any lawful no-cost full-text route has been verified; state search limits and institutional-access restrictions.
- Update the standard-access investigation, readiness dossier AR-E02, tracker notes and PR summary consistently.
- Re-fetch all updated records, verify the $0-only constraint, AR-E02 BLOCKED if access remains unconfirmed, and no clause matrix population from public preview/snippets.
- Move this plan to Completed after execution and verification evidence are recorded.

## Completion record — 2026-10-18

### Research outcome

- The official ISO help page confirms that the free OBP preview is limited to selected parts of standards; no lawful no-cost public online route to the complete applicable ISO 704 text was verified.
- The official ISO catalogue still lists ISO 704:2022, Edition 4, as published. A separate DPS listing identifies ISO/PWI 704 at stage 00.00, “Proposal for new project received”; it is proposal-stage evidence, not a published successor. The current public ISO/TC 37/SC 1 work-programme list reviewed does not show a later published ISO 704 edition.
- IIT Delhi Central Library lists ISO standards as subscribed resources and says its Reader Services Division supports outside users through a library-visit facility. Public pages do not establish whether a non-member can consult the complete ISO 704:2022 text without cost. A free informational inquiry remains the next bounded action; no right of access is assumed.
- BIS library membership requires payment and does not meet the user's $0-only policy. Unverified document-sharing uploads were not accepted as lawful baseline sources.
- Updated the expanded research report, standard-access investigation, readiness dossier AR-E02, tracker and draft PR #124. AR-E02 remains BLOCKED and the clause matrix remains template-only.

### Tool-routing incident and root-cause prevention

During report creation, one GitHub create-file call omitted its optional branch argument; the API therefore created the report on the default branch instead of the intended review branch. The error was detected when the report could not be fetched from the intended branch. The content was recreated on the intended review branch, the misplaced file was deleted from the default branch in a subsequent commit, and verification confirmed the report exists on the review branch and the same path is absent from the current default-branch tree. This was a documentation-only path, not runtime/source code; no backup/archive path was involved.

**Root cause:** the write action permits the branch parameter to be omitted, which silently selects the repository default branch; the call site lacked a mandatory explicit branch argument and immediate verification had not run until later.

**Prevention control:** for all future GitHub create/update/delete operations in this workstream, explicitly pass the target branch on every write; re-fetch the exact path using that same ref immediately afterward; and verify the default branch separately only when needed to confirm an accidental-write containment. Do not rely on the optional API default.

### Impact Analysis

**IF corrected and recorded:** the intended review-branch workflow is restored in the current tree and the root cause is actionable rather than concealed.

**IF not corrected:** a later review artifact could again bypass the intended draft PR and land on a default branch, weakening change control and audit traceability.

### Final disposition

**COMPLETED for expanded access/lifecycle research and its documentation.** This does not resolve full-text access or readiness. The $0-only policy remains binding; no purchase, paid enquiry, subscription, membership or provider outreach was made.
