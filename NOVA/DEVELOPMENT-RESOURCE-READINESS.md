# NOVA Development Resource Readiness

## Objective

Define the minimum external resources required for effective NOVA development, live smoke tests, provider failover tests, capacity tests, economic tests, and future GPU/media work while maintaining the $0 development objective.

## Current rule

Unit tests and deterministic architecture tests must run without provider credentials and must never consume external quota.

Live tests are separate. They require real credentials and must be deliberately limited so that development does not accidentally consume the available free allocation.

## Important quota rule

NOVA must not assume that a quota belongs to an individual API key. Providers may measure limits at organization, project, account, or other scopes. The capacity record must preserve the provider's actual scope.

## Minimum LLM resources

| Provider | Secret(s) | Minimum development role | Live measurements to capture | Current free-development evidence | State |
| --- | --- | --- | --- | --- | --- |
| Groq | GROQ_API_KEY_01 | Primary fast LLM smoke/failover provider | requests remaining, tokens remaining, reset intervals, usage, model | Free plan documents RPM/RPD/TPM/TPD and exposes remaining/reset headers | REQUIRED |
| Google Gemini | GEMINI_API_KEY_01 | Independent model-family benchmark and multimodal testing | project quota/limits, token usage, model, response latency; account/dashboard quota where API does not expose remaining | Free tier provides access to selected models and limits are visible in AI Studio; limits are project-level | REQUIRED |
| Mistral | MISTRAL_API_KEY_01 | Independent fallback and quality benchmark | monthly included usage, rate limits, token usage, remaining credit when account data exposes it | Free mode provides API access without a credit card; included monthly usage and limits are shown in the account | REQUIRED |
| Cloudflare Workers AI | CLOUDFLARE_API_KEY_01 + CLOUDFLARE_ACCOUNT_ID | Independent inference path and free Neuron testing | Neurons used/remaining, reset, model availability, request errors | 10,000 Neurons/day on Free; many models remain free, including GLM-4.7 Flash | REQUIRED |
| Cerebras | CEREBRAS_API_KEY_01 | Additional independent LLM/failover benchmark | usage/rate-limit data exposed by account/API, token usage, latency | Current documentation provides a $0 Free tier with lower rate limits | RECOMMENDED |

### Mistral account-specific observation (2026-10-08)

The selected Mistral Studio workspace currently displays the Free plan but also displays “Upgrade to use your API keys,” with no API key present. NOVA therefore treats Mistral as **BLOCKED / not configured for this workspace** and does not require a paid upgrade for current $0 development. This account-specific state must be re-verified before changing the provider to VERIFIED_AVAILABLE.

## GPU resources

| Provider | Credential/resource | Development role | Measurements required | State |
| --- | --- | --- | --- | --- |
| Nosana | NOSANA_GPU_API_KEY_01 | First real GPU workload path; image/video/model experiments | available credits, reserved credits, settled credits, available credits, spending history, workload runtime, GPU class | REQUIRED for GPU/media development |
| Hugging Face ZeroGPU | HF_TOKEN_01 when authentication is needed | Shared GPU validation and provider-independent experiments | GPU-seconds remaining, reset time, queue/priority, over-quota credit usage if applicable | SECONDARY |

Nosana's current API exposes credit balance, spending history and transactions. API-key scopes include `credits:read`, `jobs:read`, and workload-writing scopes; least privilege should be used. Free-credit eligibility can also be checked through the API. See: https://learn.nosana.com/api/credits.html and https://learn.nosana.com/api/scopes.html

Hugging Face currently documents free ZeroGPU access and a programmatic `get_zero_gpu_quota()` path returning base quota, remaining GPU-seconds and reset time. Free accounts have a 5-minute daily quota under the current documentation. See: https://huggingface.co/docs/huggingface_hub/main/guides/manage-spaces and https://huggingface.co/docs/hub/en/spaces-zerogpu

## What is required before live development can start

### A. Architecture-only development

No external key is required for:

- Python compilation
- unit tests
- provider routing tests using mocks
- quota parser tests
- economic accounting tests
- pricing tests
- crypto payment-intent validation
- autonomy-boundary tests
- deterministic observer/fingerprint tests

### B. Minimum live LLM development

Obtain and configure at least:

- GROQ_API_KEY_01
- GEMINI_API_KEY_01
- MISTRAL_API_KEY_01
- CLOUDFLARE_API_KEY_01
- CLOUDFLARE_ACCOUNT_ID

CEREBRAS_API_KEY_01 should be added as an additional independent fallback if its current account terms are acceptable.

### C. Live development test categories

Each configured provider must pass, where technically applicable:

1. Authentication test.
2. Minimal deterministic response-contract test.
3. Actual-model identification test.
4. Usage accounting test.
5. Remaining-quota/reset measurement test.
6. Error and rate-limit handling test.
7. Latency baseline test.
8. Provider failover test.
9. Quality benchmark test.
10. Quota-exhaustion or simulated-quota test.

Tests 1-7 should use the smallest practical requests. Tests 8-10 should normally use mocks/simulations first so free quota is reserved for genuine live verification.

## Live quota protection

NOVA should maintain a dedicated `development_test_budget` per provider.

The budget should define:

- maximum live smoke requests per day
- maximum test tokens per day
- maximum test GPU-seconds per day
- minimum remaining quota reserve
- maximum percentage of free allocation that tests may consume
- reset time
- whether the resource is renewable, one-time, promotional, or purchased

Until measured consumption proves otherwise, live automated testing should use a conservative fraction of the provider's free allocation rather than the entire allowance.

## Development resource states

Every resource should be one of:

- REQUIRED_NOT_CONFIGURED
- CONFIGURED_NOT_VERIFIED
- VERIFIED_AVAILABLE
- DEPLETING
- EXHAUSTED
- EXPIRED
- PAYMENT_REQUIRED
- BLOCKED
- UNKNOWN

## Provider scope

Capacity must store whether the measurement is scoped to:

- credential/key
- project
- organization
- account
- subscription
- workspace
- provider-wide

Never label a project-level limit as a key-level limit.

## Free-to-paid transition during development

Free resources are consumed first only when their measured economic and quality value justifies doing so. Their use does not reduce the public price.

When a free resource approaches its minimum reserve, NOVA should prepare the next development resource or paid fallback before exhaustion.

## Before production

Development readiness is not production readiness. Before public deployment, NOVA must additionally verify:

- authoritative billing/credit access
- provider invoices or spend measurements where applicable
- payment destination verification
- crypto settlement adapter where required
- public-price continuity headroom
- provider replacement capacity
- disaster/failover behavior
- data/privacy terms for each selected provider
- commercial-use rights for the selected models and generated assets

## Evidence principle

Provider pricing, quotas and model catalogs change. The values recorded in this file are planning evidence, not permanent constants. NOVA must retain source URL, observation time, scope and verification state for live provider measurements.
