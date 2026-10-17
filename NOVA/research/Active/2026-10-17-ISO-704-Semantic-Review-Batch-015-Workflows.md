# ISO 704:2022 Preliminary Semantic Review — Batch 015 (Probe Scheduler, Credential Validation and Image Qualification Workflow)

**Review ID:** NOVA-ISO704-SEM-B015  
**Date:** 2026-10-17  
**Status:** PRELIMINARY CONTENT/CONTROL REVIEW COMPLETE FOR THREE FILES; HUMAN VALIDATION REQUIRED  
**Baseline:** NOVA main snapshot dated 2026-10-17; exact blob SHAs below  
**Boundary:** Source-language and status-control review only. No workflow was triggered, no credential was read, and no live provider request was made. This is not a security audit or ISO clause-conformity result.

## 1. Files reviewed

| Batch item | Path | Baseline blob SHA | Preliminary disposition |
|---|---|---|---|
| B015-01 | `.github/workflows/nova_probe_scheduler.yml` | `ccdd55bbe8854d7f382d3bc2e2f78c350e1acea3` | REVIEWED — bounded decision/probe split and explicit permissions; operational timing and side effects not tested |
| B015-02 | `.github/workflows/nova_validation.yml` | `fee807bfb8bea849d2ce31eb4156314f85ef45fc` | REVIEWED — presence-only credential check is explicit; must not be described as provider qualification |
| B015-03 | `.github/workflows/astrocrown-cloudflare-image-qualification.yml` | `bb1acd59abd5192dd6b2e0b086bbad92273f6129` | REVIEWED — manual/main/no-payment-attestation gates and explicit artifacts; attestation is not billing telemetry and outputs remain unqualified by workflow success alone |

## 2. Findings and positive controls

### B015-F01 — Probe scheduler decision is separated from probe execution

The scheduler has a lightweight scheduled/manual decision job with contents-read permissions and a separate probe job that executes only on `main` if the decision output requests a heartbeat. The probe job has explicit contents/issue write permissions for operational-state publishing and uses a concurrency group. The trigger comments state that the cadence is rolling and that an early probe is allowed only to reuse capacity for already-required work before expiry.

These are useful distinctions between a scheduling decision and provider work. However, this file review does not establish the actual timing behavior, concurrency interaction with the separate heartbeat, GitHub schedule reliability or whether the Python scheduler implementation preserves every documented invariant. Those need their own code/test/runtime evidence.

**Disposition:** retain the least-permission split and accurate boundary that a scheduled tick is not itself proof the provider ran or that usable capacity existed.

### B015-F02 — Credential validation reports presence, not provider qualification

The validation workflow injects the names of LLM and GPU credential slots into a job running `NOVA.credential_readiness` and labels its step “Inspect credential slot presence only”. The workflow does not run provider inference in that job.

**Disposition:** do not cite this workflow as evidence of authentication, terms eligibility, actual API health, quality, remaining quota, $0/no-card status or GPU-minutes. Those require separate status records and appropriately scoped observations. This is consistent with the key-readiness vocabulary.

### B015-F03 — Manual image qualification protects against automatic inference but uses an operator gate

The image workflow is manual-only, runs its inference job only from `main` when `no_payment_confirmed == yes`, keeps token/account values in secret-derived environment variables, checks secret presence without printing values, pins the public AstroCrown adapter to an immutable reviewed SHA, and uploads image/provenance artifacts. The prompt is passed through environment variables and command arguments, rather than interpolated directly into the shell program.

The required `no_payment_confirmed=yes` input is still an operator declaration; it is not a verified account billing state, quota meter, invoice, or proof that future requests cannot trigger charges. The workflow's success proves technical completion for that run only, not prompt acceptance, alpha transparency, licensing, commercial rights or sustainable no-payment eligibility.

**Required action:** preserve the distinction between an explicit human gate and independent billing/eligibility evidence. Keep the documented successful run/artifacts and the failed visual acceptance status as separate evidence. Do not dispatch a live run merely to complete this terminology review.

### B015-F04 — Artifact output paths allow format variation, but their meaning needs adapter-level evidence

The workflow lists candidate PNG and JPEG image/sidecar artifact paths, matching the known Cloudflare response-header/payload mismatch. The reviewed YAML itself does not prove the adapter will create exactly one correct detected-format path or that the sidecar accurately records MIME/provenance. That depends on the pinned adapter's implementation/tests and the actual uploaded artifact.

**Disposition:** cross-reference the adapter's offline tests and run-specific artifact evidence; do not mark format validation PASS from this YAML alone.

## 3. Evidence and status limitations

- Exact workflow blob IDs are recorded above.
- No workflow execution, external API call, billing check, quota measurement or secret inspection was performed.
- Static review of permissions/triggers/env mapping is design/source evidence only; real configuration, action platform behavior, and run results are distinct evidence types.
- No ISO clause result is assigned.

## 4. Revision history

- **2026-10-17 / v0.1.0:** Reviewed the opportunistic probe scheduler, credential-readiness workflow and manual Cloudflare image-qualification workflow, focusing on terminology/status boundaries rather than live execution.
