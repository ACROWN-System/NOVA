# NOVA key readiness

The credential-readiness report distinguishes whether a secret is present from whether the provider works.

## States

- REQUIRED_NOT_CONFIGURED: the expected environment slot was empty in that workflow run.
- CONFIGURED_NOT_VERIFIED: the slot was non-empty; authentication, API behavior, licensing, and quota have not been inferred.
- CANDIDATE_NOT_ACTIVATED: lifecycle status is independent of key presence. A configured GPU candidate remains inactive until its API adapter, account eligibility, and workload path are verified.

The NOVA Validation workflow reports presence for the active LLM slots (Groq, Gemini, Cloudflare plus its account ID) and the two GPU candidates (Nosana and Hugging Face ZeroGPU). It prints environment-variable names and presence states only—never credential values—and does not call providers. A push to main affecting the readiness files generates a current report. It is also manually dispatchable from GitHub Actions.

## Known separations

- An LLM API key and a GPU allocation key are not interchangeable. Nosana LLM inference and Nosana GPU job/market APIs are separate operational paths, even if the vendor account may issue related credentials.
- Current NOVA LLM providers have health checks but each provider's key and account slots still require runtime presence/authentication evidence.
- No GPU candidate is placed into providers merely because a token exists.
- Credential presence does not establish $0 eligibility, no-card access, commercial rights, free-tier persistence, or available GPU minutes. Those require their own evidence and runtime checks.
- RSI in AstroCrown-Web uses a separate repository's Actions secrets/variables; the NOVA report cannot see or infer their values.
