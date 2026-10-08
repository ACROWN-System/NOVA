#!/usr/bin/env python3
"""NOVA AI heart: live provider/model health probe with failover.

The AI heart always performs a live probe; it never suppresses the probe because
the last observation was identical. Non-heart observations use fingerprinted
memory elsewhere so expensive reasoning calls can be reused when appropriate.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from . import alerts  # package execution
    from .health import (
        atomic_write_json,
        load_health_state,
        load_json,
        provider_health_status,
        record_probe,
    )
    from .capacity import annotate_probe
except ImportError:  # direct script execution
    import alerts
    from health import (
        atomic_write_json,
        load_health_state,
        load_json,
        provider_health_status,
        record_probe,
    )
    from capacity import annotate_probe
ROOT = Path(__file__).resolve().parent
ROSTER_PATH = ROOT / "roster.json"
HEALTH_POLICY_PATH = ROOT / "health_policy.json"
HEALTH_STATE_PATH = ROOT / "health_state.json"

COMMON_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "NOVA-AI-Heartbeat/1.0",
}

PERMANENT_ERROR_MARKERS = [
    "decommissioned",
    "deprecated",
    "no longer supported",
    "no longer available",
    "has been retired",
    "model_not_found",
    "does not exist",
]

HEALTH_PROMPT = (
    'NOVA live health probe. Respond with ONLY this JSON object, with no markdown: '
    '{"nova_health":"OK","ack":"NOVA_HEALTH_PROBE"}'
)


def load_roster() -> dict[str, Any]:
    return json.loads(ROSTER_PATH.read_text(encoding="utf-8"))


def save_roster(roster: dict[str, Any]) -> None:
    atomic_write_json(ROSTER_PATH, roster)


def get_env(name: str) -> str:
    return os.environ.get(name, "").strip().strip('"').strip("'")


def classify_http_error(exc: urllib.error.HTTPError) -> tuple[str, str]:
    try:
        body = exc.read().decode("utf-8", errors="ignore").lower()
    except Exception:
        body = ""
    if exc.code == 404 or any(marker in body for marker in PERMANENT_ERROR_MARKERS):
        return "permanent", body
    return "transient", body


def validate_health_payload(content: Any) -> tuple[bool, str]:
    if not isinstance(content, str) or not content.strip():
        return False, "EMPTY_RESPONSE"
    try:
        payload = json.loads(content)
    except json.JSONDecodeError:
        return False, "INVALID_JSON"
    if payload.get("nova_health") != "OK":
        return False, "HEALTH_MARKER_MISSING"
    if payload.get("ack") != "NOVA_HEALTH_PROBE":
        return False, "HEALTH_ACK_MISSING"
    return True, "PASS"


def call_openai_compatible(provider: dict[str, Any], prompt: str, validator=validate_health_payload) -> tuple[str | None, str, list[dict[str, Any]]]:
    api_key = get_env(provider["api_key_env"])
    if not api_key:
        return None, "unconfigured", [{
            "provider": provider["name"],
            "credential_env": provider["api_key_env"],
            "requested_model": None,
            "actual_model": None,
            "api_status": None,
            "authentication": "NOT_CONFIGURED",
            "response_valid": False,
            "quality_status": "NOT_APPLICABLE",
            "latency_ms": None,
            "error_class": "credential_not_configured",
            "error_detail": "Credential is not configured.",
        }]

    base_url = provider["base_url"]
    if "account_id_env" in provider:
        account_id = get_env(provider["account_id_env"])
        if not account_id:
            return None, "unconfigured", [{
                "provider": provider["name"],
                "credential_env": provider["api_key_env"],
                "requested_model": None,
                "actual_model": None,
                "api_status": None,
                "authentication": "BLOCKED",
                "response_valid": False,
                "quality_status": "NOT_APPLICABLE",
                "latency_ms": None,
                "error_class": "account_id_not_configured",
                "error_detail": "Required account identifier is not configured.",
            }]
        base_url = base_url.format(CF_ACCOUNT_ID=account_id)

    headers = {**COMMON_HEADERS, "Authorization": f"Bearer {api_key}"}
    probes: list[dict[str, Any]] = []

    for model in provider["models"]:
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "max_tokens": 64,
        }
        if provider["name"] == "groq":
            data["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "nova_health_probe",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "nova_health": {"type": "string", "enum": ["OK"]},
                            "ack": {"type": "string", "enum": ["NOVA_HEALTH_PROBE"]}
                        },
                        "required": ["nova_health", "ack"],
                        "additionalProperties": False
                    }
                }
            }
        req = urllib.request.Request(
            base_url,
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        started = time.perf_counter()

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read()
                latency_ms = (time.perf_counter() - started) * 1000
                result = json.loads(raw.decode("utf-8"))
                choices = result.get("choices")
                message = choices[0].get("message") if isinstance(choices, list) and choices else None
                content = message.get("content") if isinstance(message, dict) else None
                valid, quality = validator(content)
                actual_model = result.get("model") or model
                probe = {
                    "provider": provider["name"],
                    "credential_env": provider["api_key_env"],
                    "requested_model": model,
                    "actual_model": actual_model,
                    "api_status": response.status,
                    "authentication": "PASS",
                    "response_valid": valid,
                    "quality_status": quality,
                    "latency_ms": latency_ms,
                    "error_class": None if valid else "response_contract",
                    "error_detail": None if valid else quality,
                }
                annotate_probe(
                    probe,
                    provider=provider["name"],
                    headers=response.headers,
                    usage=result.get("usage") if isinstance(result.get("usage"), dict) else None,
                )
                probes.append(probe)
                if valid:
                    return content, "success", probes
                # A provider responded but failed NOVA's deterministic health contract.
                # Try its remaining models before falling back to another provider.
        except urllib.error.HTTPError as exc:
            latency_ms = (time.perf_counter() - started) * 1000
            signal, body = classify_http_error(exc)
            probes.append({
                "provider": provider["name"],
                "credential_env": provider["api_key_env"],
                "requested_model": model,
                "actual_model": None,
                "api_status": exc.code,
                "authentication": "FAIL" if exc.code in {401, 403} else "UNKNOWN",
                "response_valid": False,
                "quality_status": "NOT_APPLICABLE",
                "latency_ms": latency_ms,
                "error_class": signal,
                "error_detail": body[:400],
                "capacity": annotate_probe(
                    {
                        "provider": provider["name"],
                    },
                    provider=provider["name"],
                    headers=exc.headers,
                ).get("capacity"),
            })
            print(
                f"[{provider['name']}] HTTP {exc.code} on model '{model}' "
                f"({signal}): {body[:200]}"
            )
        except Exception as exc:
            latency_ms = (time.perf_counter() - started) * 1000
            probes.append({
                "provider": provider["name"],
                "credential_env": provider["api_key_env"],
                "requested_model": model,
                "actual_model": None,
                "api_status": None,
                "authentication": "UNKNOWN",
                "response_valid": False,
                "quality_status": "NOT_APPLICABLE",
                "latency_ms": latency_ms,
                "error_class": "exception",
                "error_detail": str(exc)[:400],
            })
            print(f"[{provider['name']}] Exception on model '{model}': {exc}")

    if not probes:
        return None, "transient", []
    if any(probe["error_class"] == "permanent" for probe in probes):
        return None, "permanent", probes
    return None, "quality_or_transient", probes


def call_gemini(provider: dict[str, Any], prompt: str, validator=validate_health_payload) -> tuple[str | None, str, list[dict[str, Any]]]:
    api_key = get_env(provider["api_key_env"])
    if not api_key:
        return None, "unconfigured", [{
            "provider": provider["name"],
            "credential_env": provider["api_key_env"],
            "requested_model": None,
            "actual_model": None,
            "api_status": None,
            "authentication": "NOT_CONFIGURED",
            "response_valid": False,
            "quality_status": "NOT_APPLICABLE",
            "latency_ms": None,
            "error_class": "credential_not_configured",
            "error_detail": "Credential is not configured.",
        }]

    headers = {**COMMON_HEADERS, "x-goog-api-key": api_key}
    probes: list[dict[str, Any]] = []

    for model in provider["models"]:
        url = f"{provider['base_url']}/{model}:generateContent"
        data = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0,
                "maxOutputTokens": 64,
                "responseMimeType": "application/json",
                "responseSchema": {
                    "type": "OBJECT",
                    "properties": {
                        "nova_health": {"type": "STRING", "enum": ["OK"]},
                        "ack": {"type": "STRING", "enum": ["NOVA_HEALTH_PROBE"]}
                    },
                    "required": ["nova_health", "ack"],
                    "propertyOrdering": ["nova_health", "ack"]
                }
            },
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        started = time.perf_counter()
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read()
                latency_ms = (time.perf_counter() - started) * 1000
                result = json.loads(raw.decode("utf-8"))
                candidates = result.get("candidates")
                parts = (
                    candidates[0].get("content", {}).get("parts", [])
                    if isinstance(candidates, list) and candidates
                    else []
                )
                content = parts[0].get("text") if parts and isinstance(parts[0], dict) else None
                valid, quality = validator(content)
                probe = {
                    "provider": provider["name"],
                    "credential_env": provider["api_key_env"],
                    "requested_model": model,
                    "actual_model": model,
                    "api_status": response.status,
                    "authentication": "PASS",
                    "response_valid": valid,
                    "quality_status": quality,
                    "latency_ms": latency_ms,
                    "error_class": None if valid else "response_contract",
                    "error_detail": None if valid else quality,
                }
                annotate_probe(
                    probe,
                    provider=provider["name"],
                    headers=response.headers,
                    usage=result.get("usageMetadata")
                    if isinstance(result.get("usageMetadata"), dict)
                    else None,
                )
                probes.append(probe)
                if valid:
                    return content, "success", probes
        except urllib.error.HTTPError as exc:
            latency_ms = (time.perf_counter() - started) * 1000
            signal, body = classify_http_error(exc)
            probes.append({
                "provider": provider["name"],
                "credential_env": provider["api_key_env"],
                "requested_model": model,
                "actual_model": None,
                "api_status": exc.code,
                "authentication": "FAIL" if exc.code in {401, 403} else "UNKNOWN",
                "response_valid": False,
                "quality_status": "NOT_APPLICABLE",
                "latency_ms": latency_ms,
                "error_class": signal,
                "error_detail": body[:400],
            })
            print(
                f"[{provider['name']}] HTTP {exc.code} on model '{model}' "
                f"({signal}): {body[:200]}"
            )
        except Exception as exc:
            latency_ms = (time.perf_counter() - started) * 1000
            probes.append({
                "provider": provider["name"],
                "credential_env": provider["api_key_env"],
                "requested_model": model,
                "actual_model": None,
                "api_status": None,
                "authentication": "UNKNOWN",
                "response_valid": False,
                "quality_status": "NOT_APPLICABLE",
                "latency_ms": latency_ms,
                "error_class": "exception",
                "error_detail": str(exc)[:400],
            })
            print(f"[{provider['name']}] Exception on model '{model}': {exc}")

    if any(probe["error_class"] == "permanent" for probe in probes):
        return None, "permanent", probes
    return None, "quality_or_transient", probes


def call_provider(provider: dict[str, Any], prompt: str, validator=validate_health_payload) -> tuple[str | None, str, list[dict[str, Any]]]:
    if provider["kind"] == "gemini":
        return call_gemini(provider, prompt, validator)
    return call_openai_compatible(provider, prompt, validator)


def rotate_starting_provider(providers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not providers:
        return providers
    raw_index = get_env("NOVA_PROVIDER_ROTATION_INDEX")
    if not raw_index:
        return providers
    try:
        offset = int(raw_index) % len(providers)
    except ValueError:
        print(f"[router] Invalid NOVA_PROVIDER_ROTATION_INDEX={raw_index!r}; using roster order.")
        return providers
    return providers[offset:] + providers[:offset] if offset else providers


def order_providers(providers: list[dict[str, Any]], state: dict[str, Any]) -> list[dict[str, Any]]:
    rotated = rotate_starting_provider(providers)
    preferred, degraded = [], []
    for provider in rotated:
        status = provider_health_status(
            state,
            provider=provider["name"],
            namespace="ai-heart",
        )
        (degraded if status in {"DEGRADED", "UNACCEPTABLE"} else preferred).append(provider)
    return preferred + degraded


def intelligent_router(prompt: str) -> tuple[str, dict[str, Any]]:
    print(f"[{datetime.now(timezone.utc).isoformat()}] NOVA AI Heart Pulse Initiated...")
    roster = load_roster()
    policy = load_json(HEALTH_POLICY_PATH, {})
    state = load_health_state(HEALTH_STATE_PATH)
    active = [p for p in roster["providers"] if p["status"] == "active"]
    active = order_providers(active, state)

    latency_policy = policy.get("latency", {})
    failure_policy = policy.get("failure", {})
    all_probes: list[dict[str, Any]] = []

    for provider in active:
        print(f"Trying provider: {provider['name']}")
        text, signal, probes = call_provider(provider, prompt)

        for probe in probes:
            observation = record_probe(
                state,
                namespace="ai-heart",
                provider=str(probe["provider"]),
                credential_env=str(probe["credential_env"]),
                requested_model=probe.get("requested_model"),
                actual_model=probe.get("actual_model"),
                api_status=probe.get("api_status"),
                authentication=str(probe.get("authentication", "UNKNOWN")),
                response_valid=bool(probe.get("response_valid")),
                quality_status=str(probe.get("quality_status", "NOT_APPLICABLE")),
                latency_ms=probe.get("latency_ms"),
                error_class=probe.get("error_class"),
                error_detail=probe.get("error_detail"),
                capacity=probe.get("capacity") if isinstance(probe.get("capacity"), dict) else None,
                max_samples=int(latency_policy.get("max_samples_per_target", 24)),
                latency_degraded_multiplier=float(latency_policy.get("degraded_multiplier", 2.0)),
                latency_min_samples=int(latency_policy.get("minimum_samples_for_comparison", 4)),
                unacceptable_failure_streak=int(failure_policy.get("unacceptable_consecutive_failures", 3)),
            )
            all_probes.append(observation)
            if observation["health_status"] == "UNACCEPTABLE":
                alerts.send_all_alerts(
                    title=f"NOVA AI heart: {provider['name']} health is unacceptable",
                    body=json.dumps(observation, indent=2, sort_keys=True),
                    severity="urgent",
                )

        atomic_write_json(HEALTH_STATE_PATH, state)

        if text:
            summary = {
                "heart": "AI",
                "status": "HEALTHY",
                "provider": provider["name"],
                "probes": all_probes,
                "action": "MAINTAIN",
            }
            return f"[ROUTED via {provider['name'].upper()}] {text}", summary

        if signal == "permanent":
            print(f"[{provider['name']}] Permanent model/provider failure detected — marking provider DOWN.")
            provider["status"] = "down"
            provider["marked_down_at"] = datetime.now(timezone.utc).isoformat()
            save_roster(roster)

            remaining = [p for p in roster["providers"] if p["status"] == "active"]
            analysis = alerts.generate_comparative_analysis(
                roster, provider["name"], remaining
            )
            severity = "urgent" if len(remaining) <= 2 else "notice"
            alerts.send_all_alerts(
                title=f"NOVA roster alert: {provider['name']} appears permanently unavailable",
                body=analysis,
                severity=severity,
            )

    summary = {
        "heart": "AI",
        "status": "FAILED",
        "provider": None,
        "probes": all_probes,
        "action": "FAILOVER_EXHAUSTED",
    }
    return "CRITICAL FAULT: All roster providers unresponsive this cycle.", summary


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-alert":
        roster = load_roster()
        remaining = [p for p in roster["providers"] if p["status"] == "active"]
        analysis = alerts.generate_comparative_analysis(roster, "test-provider", remaining)
        alerts.send_all_alerts(
            title="[TEST] NOVA roster alert simulation",
            body=analysis,
            severity="urgent",
            force_all_channels=True,
        )
        print("Test alert dispatched to every configured channel.")
        raise SystemExit(0)

    test_prompt = HEALTH_PROMPT
    system_state, summary = intelligent_router(test_prompt)

    # README is documentation, not operational memory. Scheduled heartbeats persist
    # structured state only, preventing unbounded documentation churn.
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("NOVA AI heart state synced to structured health memory.")
