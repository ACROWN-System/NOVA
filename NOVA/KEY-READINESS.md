# NOVA key readiness

The credential-readiness report distinguishes whether a secret is present from whether the provider works.

## States

- REQUIRED_NOT_CONFIGURED: the expected environment slot was empty in that workflow run.
- CONFIGURED_NOT_VERIFIED: the slot was non-empty; authentication, API behavior, licensing, and quota have not been inferred.
- CANDIDATE_NOT_ACTIVATED: lifecycle status is independent of key presence. A configured GPU candidate remains inactive until its API adapter, account eligibility, and workload path are verified.

The NOVA Validation workflow reports presence for the active LLM slots (Groq, Gemini, Cloudflare Workers AI token plus account ID 02) and the two GPU candidates (Nosana and Hugging Face ZeroGPU). It prints environment-variable names and presence states only—never credential values—and does not call providers. A push to main affecting the readiness files generates a current report. It is also manually dispatchable from GitHub Actions.

## Cloudflare account 02 configuration

The active Cloudflare configuration is account 02 only:

- NOVA repository Actions secret: `CLOUDFLARE_API_TOKEN_02`.
- NOVA repository Actions variable: `CLOUDFLARE_ACCOUNT_ID_02`.
- AstroCrown-Web also needs the same account-02 token/ID while its staging deployment and NOVA portability checks run from that repository.
- Preserve the existing Worker Admin and D1 Read/Edit permissions for the staging deployment. Add Account → Workers AI → Read and Account → Workers AI → Edit to the same account-02 token before using it for NOVA inference or AstroCrown image generation. Cloudflare's custom-token Workers AI REST setup guide lists both permissions.
- The prior response-contract smoke evidence is historical evidence from account 01. It does not prove account-02 authentication or current quota. The manual account-02 smoke workflow must pass before reporting the new credential pair as requalified.

Account IDs are identifiers, not secrets. Keep `CLOUDFLARE_ACCOUNT_ID_02` in Actions variables and keep the token value only in Actions secrets.

## Known separations

- An LLM API key and a GPU allocation key are not interchangeable. Nosana LLM inference and Nosana GPU job/market APIs are separate operational paths, even if the vendor account may issue related credentials.
- The qualification diagnostic actively probes Groq and Gemini only. Mistral remains deferred and is excluded from the health-test environment. The Cloudflare provider now uses account 02 only (`CLOUDFLARE_API_TOKEN_02` plus `CLOUDFLARE_ACCOUNT_ID_02`). The prior live response-contract evidence was recorded under the inaccessible account 01; it does not establish that account 02's token and quota work. Re-run the manual Cloudflare smoke test against account 02 before treating its authentication as requalified.
- No GPU candidate is placed into providers merely because a token exists.
- Credential presence does not establish $0 eligibility, no-card access, commercial rights, free-tier persistence, or available GPU minutes. Those require their own evidence and runtime checks.
- RSI in AstroCrown-Web uses a separate repository's Actions secrets/variables; the NOVA report cannot see or infer their values.

## Live heartbeat behavior

The LLM heartbeat runs on its six-hour schedule and may also run after relevant changes to `NOVA/provider_qualification.py`, `NOVA/health.py`, or `NOVA/roster.json` on `main`. Its own workflow file is deliberately excluded from the push paths so merging a trigger change does not itself cause an incidental live LLM run. The credential-qualification step probes Groq and Gemini; Mistral remains diagnostic-only. Cloudflare Workers AI is not part of that provider-qualification diagnostic; its account-02 token and exact model/API response contract are checked by the separate manual Cloudflare smoke workflow.

The GPU heartbeat keeps its six-hour schedule and manual dispatch, and can additionally run after changes to its adapter, candidate roster, shared health primitives, or own workflow. Candidate checks use allowlisted, read-only endpoints; they do not create GPU jobs or infer available credits or GPU capacity from undocumented fields. The official Nosana endpoint is `GET https://api.nosana.com/credits/balance` (official API reference: https://api.nosana.com/api/docs). A successful credential check is not evidence of zero-cost eligibility or available compute.

