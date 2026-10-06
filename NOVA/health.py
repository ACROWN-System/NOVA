#!/usr/bin/env python3
"""Shared NOVA health telemetry, memory, and safe-action primitives.

This module is dependency-free and intentionally separates:
1. live service probes (which must run when a heart beats),
2. historical health memory,
3. reusable observation memory for non-heart intelligence, and
4. reversible routing/action decisions.

Secrets are never persisted; only credential environment-variable names are.
"""

from __future__ import annotations

import hashlib
import json
import os
import statistics
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonicalize(value: Any) -> Any:
    """Normalize JSON-like observations while preserving meaningful content."""
    if isinstance(value, dict):
        return {
            str(key): canonicalize(value[key])
            for key in sorted(value)
            if str(key).lower() not in {
                "timestamp",
                "observed_at",
                "request_id",
                "trace_id",
                "run_id",
            }
        }
    if isinstance(value, list):
        normalized = [canonicalize(item) for item in value]
        try:
            return sorted(normalized, key=lambda item: json.dumps(item, sort_keys=True))
        except TypeError:
            return normalized
    if isinstance(value, float):
        return round(value, 9)
    return value


def fingerprint(value: Any) -> str:
    payload = json.dumps(
        canonicalize(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def atomic_write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".nova-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def _state_defaults() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "updated_at": None,
        "targets": {},
        "observations": {},
        "events": {},
    }


def load_health_state(path: Path) -> dict[str, Any]:
    state = load_json(path, _state_defaults())
    if not isinstance(state, dict):
        state = _state_defaults()
    for key, value in _state_defaults().items():
        state.setdefault(key, value)
    return state


def _target_key(namespace: str, name: str, model: str | None = None) -> str:
    return ":".join([namespace, name, model or "-"])


def record_probe(
    state: dict[str, Any],
    *,
    namespace: str,
    provider: str,
    credential_env: str,
    requested_model: str | None,
    actual_model: str | None,
    api_status: int | None,
    authentication: str,
    response_valid: bool,
    quality_status: str,
    latency_ms: float | None,
    error_class: str | None,
    error_detail: str | None,
    max_samples: int,
    latency_degraded_multiplier: float,
    latency_min_samples: int,
    unacceptable_failure_streak: int,
) -> dict[str, Any]:
    """Record one live probe and return the resulting health/action decision."""
    key = _target_key(namespace, provider, actual_model or requested_model)
    target = state["targets"].setdefault(
        key,
        {
            "namespace": namespace,
            "provider": provider,
            "credential_env": credential_env,
            "requested_model": requested_model,
            "actual_model": actual_model,
            "history": [],
            "latency_ms": [],
            "failure_streak": 0,
            "health_status": "UNKNOWN",
            "last_action": "INITIALIZE",
        },
    )

    if actual_model:
        target["actual_model"] = actual_model
    if requested_model:
        target["requested_model"] = requested_model
    target["credential_env"] = credential_env

    success = authentication == "PASS" and api_status is not None and 200 <= api_status < 300 and response_valid
    if success:
        target["failure_streak"] = 0
        if latency_ms is not None:
            target["latency_ms"].append(round(latency_ms, 3))
            target["latency_ms"] = target["latency_ms"][-max_samples:]
    else:
        target["failure_streak"] = int(target.get("failure_streak", 0)) + 1

    samples = [float(value) for value in target.get("latency_ms", [])]
    baseline_ms = round(statistics.median(samples[:-1] if len(samples) > 1 else samples), 3) if samples else None
    latency_degraded = (
        success
        and latency_ms is not None
        and baseline_ms is not None
        and len(samples) >= latency_min_samples
        and latency_ms > baseline_ms * latency_degraded_multiplier
    )

    if not success:
        health_status = (
            "UNACCEPTABLE"
            if target["failure_streak"] >= unacceptable_failure_streak
            else "DEGRADED"
        )
    elif quality_status not in {"PASS", "NOT_APPLICABLE"}:
        health_status = "DEGRADED"
    elif latency_degraded:
        health_status = "DEGRADED"
    else:
        health_status = "HEALTHY"

    if health_status == "HEALTHY":
        action = "MAINTAIN"
    elif health_status == "DEGRADED":
        action = "MONITOR_AND_DEPRIORITIZE"
    else:
        action = "FAILOVER_AND_ALERT"

    observation = {
        "observed_at": utc_now(),
        "provider": provider,
        "credential_env": credential_env,
        "requested_model": requested_model,
        "actual_model": actual_model,
        "api_status": api_status,
        "authentication": authentication,
        "response_valid": response_valid,
        "quality_status": quality_status,
        "latency_ms": round(latency_ms, 3) if latency_ms is not None else None,
        "baseline_latency_ms": baseline_ms,
        "latency_degraded": latency_degraded,
        "error_class": error_class,
        "error_detail": error_detail,
        "health_status": health_status,
        "action": action,
    }

    target["health_status"] = health_status
    target["last_action"] = action
    target["last_observation"] = observation
    target["history"].append(observation)
    target["history"] = target["history"][-max_samples:]

    state["updated_at"] = utc_now()
    return observation


def provider_health_status(
    state: dict[str, Any],
    *,
    provider: str,
    namespace: str,
) -> str:
    statuses = []
    prefix = namespace + ":" + provider + ":"
    for key, target in state.get("targets", {}).items():
        if key.startswith(prefix):
            statuses.append(target.get("health_status", "UNKNOWN"))
    if "UNACCEPTABLE" in statuses:
        return "UNACCEPTABLE"
    if "DEGRADED" in statuses:
        return "DEGRADED"
    if "HEALTHY" in statuses:
        return "HEALTHY"
    return "UNKNOWN"


def remember_observation(
    state: dict[str, Any],
    *,
    namespace: str,
    source: str,
    observation: Any,
    analysis: dict[str, Any] | None = None,
    valid_for_seconds: int | None = None,
) -> dict[str, Any]:
    """Remember a non-heart observation and determine whether it changed."""
    canonical = canonicalize(observation)
    fp = fingerprint(canonical)
    key = f"{namespace}:{source}"
    previous = state["observations"].get(key)

    unchanged = bool(previous and previous.get("fingerprint") == fp)
    record = {
        "namespace": namespace,
        "source": source,
        "fingerprint": fp,
        "observed_at": utc_now(),
        "unchanged_from_previous": unchanged,
        "observation": canonical,
    }

    if previous and analysis is None:
        record["analysis"] = previous.get("analysis")

    if analysis is not None:
        record["analysis"] = analysis
        record["analysis_fingerprint"] = fp

    if valid_for_seconds is not None:
        record["analysis_valid_for_seconds"] = int(valid_for_seconds)

    state["observations"][key] = record
    state["updated_at"] = utc_now()
    return record


def reusable_analysis(
    state: dict[str, Any],
    *,
    namespace: str,
    source: str,
    current_observation: Any,
) -> dict[str, Any] | None:
    """Return a previous analysis only when the meaningful observation is unchanged.

    Validity windows are enforced by the caller using the recorded timestamp.
    This function deliberately does not suppress live heart probes.
    """
    key = f"{namespace}:{source}"
    previous = state.get("observations", {}).get(key)
    if not previous or previous.get("fingerprint") != fingerprint(current_observation):
        return None
    analysis = previous.get("analysis")
    return analysis if isinstance(analysis, dict) else None
