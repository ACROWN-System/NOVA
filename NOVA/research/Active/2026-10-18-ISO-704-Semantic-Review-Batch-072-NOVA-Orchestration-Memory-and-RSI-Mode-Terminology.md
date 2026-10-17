# ISO 704 Semantic Review Batch 072 — NOVA Orchestration, Memory and RSI-Mode Terminology

**Document ID:** NOVA-ISO704-SEM-B072  
**Review date:** 2026-10-18  
**Baseline repository:** `ACROWN-System/AstroCrown-Web`  
**Baseline commit:** `5faea74dd1b40ec98acf9d59d9e404fc18122032`  
**Scope:** Two development-subsystem README files, the RSI credential-readiness guide, the repeat-state cycle detector, and the RSI operating-modes document, read at the pinned baseline and reconciled against the tracker before review.  
**Review status:** Preliminary full-file semantic review; human validation required.  
**Standards status:** No ISO 704 clause-level assessment was performed. This report does not claim conformity or nonconformity to any clause.

## Review method and limits

The complete Markdown sources and Python module were inspected statically at their exact recorded blob SHAs. The review focused on concept boundaries, precise designations for subsystem roles and lifecycle states, separation of credential presence from operational eligibility, definitions of workflow states/cycle quantities, provenance, and whether candidates are distinguished from approved/operational capabilities. The Python module was not executed, imported, tested, or changed. No workflow, provider, credential, live API, repository setting, runtime path, or backup/archive path was used.

## Source manifest and dispositions

| # | Source path | Baseline blob SHA | Disposition |
|---|---|---|---|
| B072-01 | `development/nova-ai-orchestration/README.md` | `cc833fe126972e3752a20ee2cf93427c63f61645` | Preliminary review; no unique terminology finding. |
| B072-02 | `development/nova-context-memory-optimization/README.md` | `a84575b4aed3d5bc100f251c8bd792402af8f2ef` | Preliminary review; no unique terminology finding. |
| B072-03 | `development/nova-recursive-self-improvement/CREDENTIAL-READINESS.md` | `60b521a557e0d0fb86c5af6b04e6b9048017ec6b` | Preliminary review; no unique finding in the wording reviewed. |
| B072-04 | `development/nova-recursive-self-improvement/cycle_detector.py` | `d6c8f216ce792902b099adefae09095592208a44` | Preliminary static review; open SWEEP-F-0052 on “RSI pass” terminology versus workflow-run records. |
| B072-05 | `development/nova-recursive-self-improvement/RSI-OPERATING-MODES.md` | `989b8036bee959314e0ff5d5780c527fe9d341d0` | Preliminary review; no unique finding; cross-reference F-0052 as applicable clarification. |

## File-level review notes

### B072-01 — NOVA AI Orchestration

The README defines **NOVA AI Orchestration** as the reusable architectural capability and the **NOVA AI Assistant** as one possible consumer, rather than allowing a UI/chatbot use case to become the architectural definition. It distinguishes participant/provider/model eligibility constraints, response comparison, evidence/claim evaluation, arbitration, distillation, provenance, uncertainty, and the final governance/decision process.

The document explicitly prohibits inferring consensus, verification, certainty, source support, or authoritative governance decisions beyond collected evidence. Its overall subsystem, specific algorithms, providers, models, and policies remain candidate/under evaluation. These statements create useful concept boundaries and status controls; no unique finding was opened.

### B072-02 — NOVA Context & Memory Optimization

The README distinguishes external API/token cost, local inference computation, context/retrieval work, and cache/prefix reuse. It explicitly states that the techniques solve different cost problems and are not interchangeable. Memory categories are distinguished (working context, reusable semantic knowledge, episodic/task history, decisions, research findings, verification evidence, and superseded/temporal knowledge); the document does not mandate a storage technology.

Its core rule is to reduce unnecessary computation and context without sacrificing correctness, provenance, freshness, security, or reliability. Candidate frameworks and a context-packing candidate are explicitly not approved implementations or complete production systems. The source also distinguishes a software license from the separate licensing/eligibility of models, datasets, providers, and outputs. These are useful terminology and concept-model safeguards. No unique finding was opened.

### B072-03 — RSI Credential Readiness

The document defines this workflow as a **presence-only** check and explicitly states that it does not make provider calls or establish key validity, live provider health, price/free-tier status, commercial-use eligibility, or sufficient availability. It also explicitly warns against treating a non-empty Groq key slot as unlimited or permanently free capacity. This is an appropriate distinction between credential existence and operational eligibility; no unique finding was opened.

### B072-04 — Repeat-state cycle detector

The code compares native Git tree/blob object IDs for a declared set of RSI-related source scopes and preserves limitations: object identity does not establish capability quality, and the absence of a repeat in the bounded window does not establish improvement or rule out older cycles. It separates an unavailable diagnostic from the “no repeat” result, and records each history row's workflow `conclusion`.

However, the history collector selects prior runs by branch (`main`) and trigger event (`schedule` or `workflow_dispatch`), without filtering or otherwise constraining their `conclusion`; the analyzer then treats every included record as one element in the sequence. The output fields and message name the resulting interval `cycle_length_passes` and “RSI pass(es)”. Consequently, the count is the number of included workflow-run records between observed state entries, not necessarily a count of successful or even fully executed RSI passes. A failed, cancelled, or otherwise incomplete workflow invocation can still be part of the selected history. The issue is the semantic designation/definition and its interpretation, not a claim that the underlying exact-state comparison is wrong. SWEEP-F-0052 records this terminology boundary.

### B072-05 — RSI Operating Modes

The document separates **Weak RSI** (manual, human-in-the-loop, one request maximum under the stated procedure) from **Strong RSI** (suspended and inactive pending all required release gates). It explicitly says Weak RSI neither authorizes Strong RSI nor changes its readiness, and that a valid `NO_CHANGE` result is a report rather than an empty patch/candidate PR. It also distinguishes GitHub-managed repository authentication from an LLM API key, credential presence from GPU capacity, and benchmark/test success from demonstrated capability improvement.

Strong RSI is explicitly marked “SUSPENDED” with implementation readiness “INCOMPLETE”; the required release criteria and no-degradation logic are retained. These are positive controls and should remain intact. This document supplies context for SWEEP-F-0052 because terms such as “pass” and “pass(es) since repeat” need to be aligned with the actual history unit used by the diagnostic, not confused with approval or readiness state.

## Finding

### SWEEP-F-0052 — Cycle diagnostic labels workflow-run intervals as “RSI passes” without defining eligible pass outcomes

- **Status:** OPEN — preliminary; human validation required.
- **Affected paths:** `AstroCrown-Web/development/nova-recursive-self-improvement/cycle_detector.py`, particularly `recent_prior_runs()`, `analyze_history()`, `cycle_length_passes`, and the report text; related lifecycle vocabulary in `AstroCrown-Web/development/nova-recursive-self-improvement/RSI-OPERATING-MODES.md`.
- **Observed issue:** The history collector records each selected `schedule` or `workflow_dispatch` run from `main` with its `conclusion`, but it does not limit eligible records based on that conclusion. The analyzer computes the interval using record indices and describes that interval as `cycle_length_passes` or a number of “RSI pass(es)”. Failed, cancelled, or incomplete workflow runs can therefore contribute to the count even if “pass” is understood to mean a completed/eligible RSI execution.
- **Interpretation:** “Workflow run/attempt”, “completed RSI pass”, “successful RSI pass”, and “source-state observation” are distinct concepts. If the intended metric counts all eligible workflow invocations, the field/message should name that unit. If it is intended to count completed or successful RSI passes, the eligible-history criteria and their treatment of failed/cancelled/incomplete runs must be defined and implemented. The existing caveats about bounded history and lack of proof of capability improvement are useful controls and should remain intact.
- **Required action:** Define the intended history unit and exact eligibility criteria. Then align the field names, report wording, calculation, and tests with that definition; if outcomes are filtered, keep incomplete/unavailable history distinguishable from a genuine no-repeat result. Do not infer improvement from absence of a repeated source state.
- **Closure evidence:** Human-approved definitions for run/attempt/pass and repeat interval; reviewed outcome-eligibility rules; test evidence covering successful, failed, cancelled/incomplete, repeated-state, and no-repeat histories; and output wording consistent with the measured quantity.

No code was executed or modified during this content review. The finding does not claim runtime regression or determine the intended unit; it asks that the term match the defined measurement.

## Batch disposition and counts

After recording these five full-file preliminary reviews, the row-derived sweep target is:

- Active files inventoried: **318**
- Preliminary full-file reviews: **276**
- Partial targeted screens: **5**
- Not yet reviewed: **37**
- Human validation of preliminary reviews: **pending**
- Formal ISO 704 clause-level assessments completed: **0**
- Scope approval: **proposed; human approval pending**

Arithmetic check: 276 + 5 + 37 = 318.

No source/runtime files, backup/archive paths, tests, workflows, credentials, providers, billing, or repository settings were changed or used. This is not a formal ISO 704 clause assessment or conformity statement.
