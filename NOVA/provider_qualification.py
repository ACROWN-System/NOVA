"""Bounded, secret-safe diagnostic probes; never mutates NOVA production state."""
import json
import os
import re
import socket
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

MARKER = "NOVA_PROBE_OK"
MAX_BYTES = 65536
TIMEOUT = 18
HEADERS_OK = {"retry-after", "ratelimit-limit", "ratelimit-remaining",
              "ratelimit-reset", "x-ratelimit-limit", "x-ratelimit-remaining",
              "x-ratelimit-reset", "x-ratelimit-limit-requests",
              "x-ratelimit-remaining-requests", "x-ratelimit-limit-tokens",
              "x-ratelimit-remaining-tokens"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def classify(status):
    if 300 <= status < 400:
        return "REDIRECT_BLOCKED"
    if status == 401:
        return "AUTH_REJECTED"
    if status == 402:
        return "PAYMENT_REQUIRED_OR_CREDITS_EXHAUSTED"
    if status == 403:
        return "ACCESS_DENIED_OR_POLICY"
    if status == 404:
        return "ENDPOINT_OR_MODEL_NOT_FOUND"
    if status == 429:
        return "RATE_LIMITED_OR_QUOTA_EXHAUSTED"
    if status >= 500:
        return "PROVIDER_SERVER_ERROR"
    return "HTTP_ERROR"


def safe_headers(headers):
    result = {}
    if not headers:
        return result
    for key, value in headers.items():
        key = str(key).lower()
        value = str(value).strip()
        if key in HEADERS_OK and len(value) <= 80 and re.fullmatch(r"[A-Za-z0-9.,:/_+-]+", value):
            result[key] = value
    return result


def openai_text(payload):
    try:
        return payload["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return ""


def gemini_text(payload):
    try:
        return "".join(part.get("text", "") for part in payload["candidates"][0]["content"]["parts"])
    except (KeyError, IndexError, TypeError, AttributeError):
        return ""


def probe(name, kind, env_name, credential, url, method, headers, body, validator):
    base = {"provider": name, "provider_type": kind, "credential_env": env_name,
            "credential_configured": bool(credential), "http_status": None,
            "latency_ms": None, "rate_limit_headers": {}, "usage": {}}
    if not credential:
        base["status"] = "SKIPPED_MISSING_CREDENTIAL"
        return base

    request = urllib.request.Request(url, data=body, method=method, headers={
        "Accept": "application/json", "User-Agent": "NOVA-Provider-Qualification/1.0",
        **headers,
    })
    start = time.monotonic()
    opener = urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(request, timeout=TIMEOUT) as response:
            code = int(response.status)
            base["http_status"] = code
            base["rate_limit_headers"] = safe_headers(response.headers)
            raw = response.read(MAX_BYTES + 1)
        base["latency_ms"] = int((time.monotonic() - start) * 1000)
        if len(raw) > MAX_BYTES:
            base["status"] = "RESPONSE_TOO_LARGE"
            return base
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            base["status"] = "INVALID_JSON_RESPONSE"
            return base
        if not isinstance(payload, dict):
            base["status"] = "INVALID_RESPONSE_SHAPE"
            return base
        text = validator(payload)
        base["status"] = "PASS" if isinstance(text, str) and MARKER in text else "PROBE_RESPONSE_INVALID"
        usage = payload.get("usage") or payload.get("usageMetadata") or {}
        if isinstance(usage, dict):
            for out_key, possible_keys in {
                "input_tokens": ("prompt_tokens", "promptTokenCount"),
                "output_tokens": ("completion_tokens", "candidatesTokenCount"),
                "total_tokens": ("total_tokens", "totalTokenCount"),
            }.items():
                for key in possible_keys:
                    value = usage.get(key)
                    if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
                        base["usage"][out_key] = value
                        break
        return base
    except urllib.error.HTTPError as exc:
        base["http_status"] = int(exc.code)
        base["status"] = classify(int(exc.code))
        base["latency_ms"] = int((time.monotonic() - start) * 1000)
        base["rate_limit_headers"] = safe_headers(exc.headers)
        exc.close()
        return base
    except (TimeoutError, socket.timeout):
        base["status"] = "TIMEOUT"
        base["latency_ms"] = int((time.monotonic() - start) * 1000)
        return base
    except (urllib.error.URLError, OSError):
        base["status"] = "NETWORK_ERROR"
        base["latency_ms"] = int((time.monotonic() - start) * 1000)
        return base
    except Exception:
        # Avoid exception strings because upstream errors may contain request data.
        base["status"] = "PROBE_INTERNAL_ERROR"
        base["latency_ms"] = int((time.monotonic() - start) * 1000)
        return base


def chat_body(model, token_field="max_tokens"):
    body = {"model": model, "messages": [{"role": "user",
        "content": "Reply exactly with this marker and nothing else: " + MARKER}],
        token_field: 32, "temperature": 0, "stream": False}
    return json.dumps(body,
        separators=(",", ":")).encode("utf-8")


def build_report(environ=None):
    env = os.environ if environ is None else environ
    rows = []
    groq = env.get("GROQ_API_KEY_01", "").strip()
    gemini = env.get("GEMINI_API_KEY_01", "").strip()
    mistral = env.get("MISTRAL_API_KEY_01", "").strip()
    github = env.get("GitHub_Token", "").strip()
    cf = env.get("CLOUDFLARE_API_KEY_01", "").strip()
    cf_id = env.get("CLOUDFLARE_ACCOUNT_ID", "").strip()

    for name, key_env, key, url, model, token_field in [
        ("groq", "GROQ_API_KEY_01", groq,
         "https://api.groq.com/openai/v1/chat/completions", "openai/gpt-oss-20b", "max_completion_tokens"),
        ("mistral_requalification", "MISTRAL_API_KEY_01", mistral,
         "https://api.mistral.ai/v1/chat/completions", "mistral-small-latest", "max_tokens"),
    ]:
        rows.append(probe(name, "llm_inference", key_env, key, url, "POST",
            {"Authorization": "Bearer " + key, "Content-Type": "application/json"},
            chat_body(model, token_field), openai_text))

    gemini_body = json.dumps({"contents": [{"parts": [{"text":
        "Reply exactly with this marker and nothing else: " + MARKER}]}],
        "generationConfig": {"temperature": 0, "maxOutputTokens": 16}},
        separators=(",", ":")).encode("utf-8")
    rows.append(probe("gemini", "llm_inference", "GEMINI_API_KEY_01", gemini,
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent",
        "POST", {"x-goog-api-key": gemini, "Content-Type": "application/json"},
        gemini_body, gemini_text))

    rows.append(probe("github_api", "repository_management_not_inference", "GitHub_Token", github,
        "https://api.github.com/user", "GET",
        {"Authorization": "Bearer " + github, "X-GitHub-Api-Version": "2022-11-28"},
        None, lambda payload: MARKER if isinstance(payload.get("login"), str) and payload.get("login") else ""))

    if cf and cf_id:
        rows.append(probe("cloudflare", "llm_inference", "CLOUDFLARE_API_KEY_01", cf,
            "https://api.cloudflare.com/client/v4/accounts/" + cf_id + "/ai/v1/chat/completions",
            "POST", {"Authorization": "Bearer " + cf, "Content-Type": "application/json"},
            chat_body("@cf/zai-org/glm-4.7-flash", "max_tokens"), openai_text))
    else:
        missing = []
        if not cf:
            missing.append("CLOUDFLARE_API_KEY_01")
        if not cf_id:
            missing.append("CLOUDFLARE_ACCOUNT_ID")
        rows.append({"provider": "cloudflare", "provider_type": "llm_inference",
            "credential_env": "+".join(missing), "credential_configured": False,
            "status": "SKIPPED_MISSING_CREDENTIAL_OR_ACCOUNT", "http_status": None,
            "latency_ms": None, "rate_limit_headers": {}, "usage": {}})

    report = {"observed_at": datetime.now(timezone.utc).isoformat(), "diagnostic_only": True,
        "production_roster_mutated": False, "secret_values_exposed": False, "results": rows}
    return report


def render_markdown(report):
    lines = [
        "# NOVA provider qualification",
        "",
        "One fixed non-sensitive request per configured endpoint. No credential values, response text, or raw error bodies are logged.",
        "A pass does not prove remaining quota, $0 eligibility, commercial rights, or production capacity.",
        "",
        "| Provider | Type | Credential slot | Configured | Result | HTTP | Latency ms | Usage |",
        "|---|---|---|---|---|---:|---:|---|",
    ]
    for row in report.get("results", []):
        usage = ", ".join("{}={}".format(k, v) for k, v in sorted(row.get("usage", {}).items())) or "unavailable"
        lines.append("| {provider} | {provider_type} | {credential_env} | {configured} | {status} | {http} | {latency} | {usage} |".format(
            provider=row["provider"], provider_type=row["provider_type"],
            credential_env=row["credential_env"],
            configured="yes" if row.get("credential_configured") else "no",
            status=row["status"], http=row["http_status"] if row["http_status"] is not None else "—",
            latency=row["latency_ms"] if row["latency_ms"] is not None else "—",
            usage=usage))
    lines.extend([
        "",
        "Mistral is requalified for diagnostic purposes only and remains DEFERRED.",
        "GitHub API authentication is repository-management capacity, not LLM inference capacity.",
        "The diagnostic does not mutate provider roster, persisted health state, routing or billing settings.",
    ])
    return "\\n".join(lines) + "\\n"


def main():
    report = build_report()
    print(json.dumps(report, indent=2, sort_keys=True))
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "").strip()
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as out:
            out.write(render_markdown(report))


if __name__ == "__main__":
    main()
