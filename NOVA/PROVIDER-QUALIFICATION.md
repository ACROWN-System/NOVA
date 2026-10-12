# NOVA Provider Qualification

This diagnostic evaluates configured provider credentials with one bounded, non-sensitive request per configured endpoint. It reports presence, authentication status, response validity, latency and allowed quota headers only. It never prints credential values, response text, raw error bodies or unapproved headers. It does not modify the provider roster, persistent health state, billing settings or live routing. A passing request is a timestamped observation, not proof of free-tier eligibility, remaining quota, commercial rights or production suitability.

Mistral qualification is a requalification observation only; its production lifecycle remains DEFERRED pending a separate policy decision. The GitHub API token is tested only for repository-management authentication and does not count as LLM inference capacity because GitHub Models inference was retired on 2026-07-30.
