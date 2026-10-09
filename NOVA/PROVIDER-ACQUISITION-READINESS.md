# NOVA Provider Acquisition Readiness

## Purpose

This document defines what must be verified before adding any new AI/LLM or GPU credential to NOVA.

Credentials themselves must never be committed to Git. Only secret environment-variable names belong in repository configuration.

## Current development objective

The immediate objective is **$0 operational validation**:
1. Obtain free/no-cost credentials or credits where currently available.
2. Verify the provider's current API contract and model availability.
3. Add the provider only after verification.
4. Run NOVA health probes.
5. Run quality verification before treating a model/provider as operationally preferred.
6. Preserve measured evidence in NOVA health memory.
7. Keep fallback providers available.

"Free" means a documented free allocation, free credits, or shared free compute; it does not mean unlimited capacity.

## LLM acquisition queue

### Groq — high-priority verification

NOVA currently contains openai/gpt-oss-120b and openai/gpt-oss-20b.

Official rate-limit documentation currently lists both at 30 RPM, 1,000 requests/day, 8K TPM and 200K TPD on the free plan. Exact account limits must still be read from the provider account because limits apply at organization level.

Source: https://console.groq.com/docs/rate-limits
Credential slot: GROQ_API_KEY_01

### Google Gemini — high-priority verification

NOVA currently contains Gemini models, but model availability and free limits must be verified in the active AI Studio project before activation. Google states that limits vary by model/project and are visible in AI Studio.

Sources: https://ai.google.dev/gemini-api/docs/rate-limits ; https://ai.google.dev/gemini-api/docs/pricing
Credential slot: GEMINI_API_KEY_01

### Cloudflare Workers AI — high-priority verification

Workers AI currently provides a 10,000-Neuron/day free allocation. NOVA's roster was changed to the currently documented free-plan model candidate: @cf/zai-org/glm-4.7-flash.

Source: https://developers.cloudflare.com/workers-ai/platform/pricing/
Credential slots: CLOUDFLARE_API_KEY_01, CLOUDFLARE_ACCOUNT_ID

### Mistral — verify before activation

Keep the provider configuration only after current account access, model availability, and free-mode terms are verified.
Credential slot: MISTRAL_API_KEY_01

### Cerebras — blocked under the current $0 / no-payment-method rule

Current official pricing says a one-time $5 promotional credit requires a valid payment method and expires 30 days after activation. Access pauses when the promotional credit expires or is exhausted unless paid credits are purchased separately. It is not a perpetual free tier and is not eligible under the current no-payment-method requirement.

Source: https://www.cerebras.ai/pricing
Credential slot: CEREBRAS_API_KEY_01 (retain for compatibility; do not prioritize)

### Additional candidates — evidence classification (2026-10-09)

| Candidate | Proposed secret slot | Evidence and boundary | Current classification |
| --- | --- | --- | --- |
| OpenRouter | `OPENROUTER_API_KEY_01` | Official free plan lists 25+ free models, four free providers and 50 requests/day; current support guidance says 20 RPM. It is an aggregator/proxy, so it expands model access but does not provide fully independent upstream capacity. Free models and upstream availability can change. Sources: https://openrouter.ai/pricing/ ; https://openrouter.zendesk.com/hc/en-us/articles/39501163636379-OpenRouter-Rate-Limits-What-You-Need-to-Know | CANDIDATE — useful breadth, low daily quota |
| Hugging Face Inference Providers | `HF_INFERENCE_API_KEY_01` | Official docs state free accounts receive $0.10/month in credits, subject to change, across a routed catalog of 200+ models/providers. It is another aggregation layer, not an independent provider for every model route. Never purchase credits or enable paid usage under the current rule. Source: https://huggingface.co/docs/inference-providers/pricing | CANDIDATE — small experimentation budget |
| Cohere trial API | `COHERE_TRIAL_API_KEY_01` | Trial API keys are free but limited (including 1,000 calls/month for trial keys); Cohere says trial keys are not permitted for production/commercial use. Source: https://cohere.com/pricing ; https://docs.cohere.com/v2/docs/rate-limits | NON-COMMERCIAL DEVELOPMENT ONLY — not a production fallback |
| SambaNova Cloud | `SAMBANOVA_API_KEY_01` | Current official plan page states users must add a payment method and purchase credits to run first requests. Source: https://cloud.sambanova.ai/plans | NOT ELIGIBLE under current no-card/$0 rule |
| NVIDIA NIM / API Catalog | `NVIDIA_NIM_API_KEY_01` | NVIDIA's current NIM/API Catalog material advertises no-charge use under applicable license terms and free developer access. Exact hosted endpoint quotas, payment-method requirements, data-use terms and long-term entitlement for this project remain unverified. Source: https://docs.nvidia.com/nim/ | CANDIDATE — verify account and endpoint terms before enabling |
| Requesty Gateway | `REQUESTY_API_KEY_01` | Official pricing offers a $0 plan, free models, 200 requests/day and no credit card. It is an aggregator/router, so underlying model availability and independence vary. Source: https://www.requesty.ai/pricing | CANDIDATE — useful no-card routing/fallback breadth |
| Kilo AI Gateway | No key for anonymous access; optional `KILO_API_KEY_01` only after account terms checked | Official docs say free models can be called anonymously at up to 200 requests/hour/IP; free model availability changes. Some NVIDIA free endpoints have trial/data-use conditions. Source: https://kilo.ai/docs/gateway/authentication ; https://kilo.ai/docs/gateway/models-and-providers | CANDIDATE — promising no-key test, but treat routed prompts as potentially logged; do not send confidential data until route-specific terms are checked |
| OpenCode Zen / Console | `OPENCODE_ZEN_API_KEY_01` only if a verified $0 entitlement appears | Current official console docs say users must add billing details and credits for pay-as-you-go models; secondary lists of free promo models do not establish a durable free API tier. Source: https://opencode.ai/v2/docs/console/models/ | DEFERRED — verify only if official $0 promotional access is confirmed |
| OpenInference directories | — | FreeInference.dev and community maintained free-API lists currently aggregate many models/providers and can reveal new candidates; they are discovery indexes, not authoritative provider terms. Sources: https://freeinference.dev/ ; https://github.com/pacocartones/free-llm-api-hub | DISCOVERY SOURCE — use to expand search, then verify each candidate's official terms |
| GitHub Models | — | GitHub officially retired the playground, catalog, inference API and BYOK on July 30, 2026. Source: https://github.blog/changelog/2026-07-30-github-models-is-now-retired/ | RETIRED — do not acquire a key |

### Newly discovered candidates requiring a wider official-term audit

A fresh discovery pass surfaced additional gateways/directories beyond the shortlist above. This is not an exhaustive final ranking and does not authorize adding all of them to the runtime roster.

| Lead | Proposed slot / access | What is known now | State |
| --- | --- | --- | --- |
| Nous Portal | `NOUS_PORTAL_API_KEY_01` if an account key is needed | Appears in a third-party free-API catalog; official quota, no-card status, API compatibility and data-use terms have not yet been verified. | UNKNOWN / INVESTIGATE |
| OVHcloud AI Endpoints | `OVHCLOUD_AI_ENDPOINTS_API_KEY_01` if using authenticated API | Appears in a third-party catalog as a hosted endpoint with some free models; exact current official model/quota/anonymous-access terms have not yet been verified here. | UNKNOWN / INVESTIGATE |
| Aion Labs API | `AION_API_KEY_01` if an API key is available | Found in secondary free-API listings; official current endpoint, allocation, account requirements and terms still need direct verification. | UNKNOWN / INVESTIGATE |
| OpenCode Zen free promotions | `OPENCODE_ZEN_API_KEY_01` only if applicable | Do not assume promotional free model listings mean a general or permanent free API tier; the official console page currently describes credit-funded paid usage. | DEFERRED |
| More candidates from discovery catalogs | None until selected | FreeInference.dev currently indexes 100+ model entries across dozens of provider/gateway entries; community directories provide leads, not proof. Search until new finds begin to repeat, then classify each lead. | ONGOING DISCOVERY |

Candidate directories and community lists may help discover providers, but their claims are leads only. Before a provider enters the active roster, verify current official terms, payment-method requirement, commercial-use conditions, model/API compatibility, data policy, limits and a live minimal response. Do not make every discovered candidate a runtime dependency.

## GPU acquisition queue

### Nosana — first GPU candidate

Nosana currently advertises free GPU credits for new builders and provides an API/SDK for GPU markets and workloads. Amount and eligibility must be verified in the actual account before NOVA treats the credit as available.

Sources: https://www.nosana.com/blog/the-new-nosana-experience-is-now-live/ ; https://learn.nosana.com/api/markets ; https://www.nosana.com/gpu-workloads/
Credential slot: NOSANA_GPU_API_KEY_01

Activation requires a provider-specific adapter. A generic GET health endpoint must not be treated as proof that a GPU workload can actually run.

### Hugging Face ZeroGPU — shared/free GPU candidate

Hugging Face currently documents ZeroGPU as shared GPU infrastructure for Spaces, with a free-account daily quota. This is not a generic GPU rental API and therefore requires a dedicated adapter.

Source: https://huggingface.co/docs/hub/main/spaces-zerogpu
Credential slot: HF_ZEROGPU_TOKEN_01 when authentication is required by the selected integration. Keep this GPU token scope distinct from `HF_INFERENCE_API_KEY_01` used for routed LLM inference.

## Activation gates

A provider is not operational merely because a key exists.

NOVA should record:
- provider name
- credential environment name
- model/service name
- requested model
- actual model returned by the provider
- API status
- authentication result
- response-contract result
- latency
- baseline latency
- quality verification state
- quota/rate-limit evidence when exposed
- timestamp
- resulting action

## Quality gate

Availability and quality are separate dimensions.

A provider can be reachable but low quality, fast but low quality, high quality but unreliable, high quality but too slow, or available but outside the intended free-cost boundary.

NOVA must therefore never promote a provider solely because its API health probe succeeds.

Quality remains UNVERIFIED until an explicit benchmark has produced evidence.

## Future scaling

The same provider contract must remain usable when the project moves from free prototype -> free credits -> low-cost operation -> paid operation -> multi-provider production.

No architecture should require replacing the router when a provider, model, GPU class, or billing model changes.

## Security

Never store API keys, access tokens, wallet private keys, passwords, or provider secrets in roster.json, gpu_roster.json, health_state.json, source code, README files, or workflow YAML.

GitHub Actions secrets are the intended initial credential boundary.
