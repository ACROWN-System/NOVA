#!/usr/bin/env python3
"""Shared NOVA health telemetry, memory, and safe-action primitives.

Live heart probes are never skipped: a heart exists to test the live service.
External observations are fingerprinted separately so a future reasoning layer
can reuse prior analysis when meaningful inputs have not changed.

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
    """Normalize JSON-like observations without retaining volatile transport fields."""
    volatile = {
        "timestamp",
        "observed_at",
        "request_id",
        "trace_id",
        "run_id",
        "latency_ms",
        "duration_ms",
    }
    if isinstance(value, dict):
        return {
            str(key): canonicalize(value[key])
            for key in sorted(value)
            if str(key).lower() not in volatile
        }
    if isinstance(value, list):
        # List order can be transport noise for sets of annotations/events.
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
    capacity: dict[str, Any] | None = None,
    max_samples: int,
    latency_degraded_multiplier: float,
    latency_min_samples: int,
    unacceptable_failure_streak: int,
) -> dict[str, Any]:
    """Record one live probe and return its resulting health/action decision."""
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

    target["credential_env"] = credential_env
    if requested_model:
        target["requested_model"] = requested_model
    if actual_model:
        target["actual_model"] = actual_model

    not_configured = authentication in {"NOT_CONFIGURED", "BLOCKED"} and error_class in {
        "credential_not_configured",
        "health_url_not_configured",
        "unsupported_auth_type",
    }

    success = (
        authentication == "PASS"
        and api_status is not None
        and 200 <= api_status < 300
        and response_valid
    )

    if not_configured:
        target["health_status"] = "UNCONFIGURED"
        target["last_action"] = "WAIT_FOR_CONFIGURATION"
    else:
        if success:
            target["failure_streak"] = 0
            if latency_ms is not None:
                target["latency_ms"].append(round(latency_ms, 3))
                target["latency_ms"] = target["latency_ms"][-max_samples:]
        else:
            target["failure_streak"] = int(target.get("failure_streak", 0)) + 1

        samples = [float(value) for value in target.get("latency_ms", [])]
        baseline_source = samples[:-1] if len(samples) > 1 else samples
        baseline_ms = (
            round(statistics.median(baseline_source), 3) if baseline_source else None
        )
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

        target["health_status"] = health_status
        target["last_action"] = action

    samples = [float(value) for value in target.get("latency_ms", [])]
    baseline_ms = (
        round(statistics.median(samples[:-1] if len(samples) > 1 else samples), 3)
        if samples
        else None
    )
    latency_degraded = (
        success
        and latency_ms is not None
        and baseline_ms is not None
        and len(samples) >= latency_min_samples
        and latency_ms > baseline_ms * latency_degraded_multiplier
    )

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
        "capacity": capacity or {},
        "health_status": target.get("health_status", "UNKNOWN"),
        "action": target.get("last_action", "INITIALIZE"),
    }

    target["last_observation"] = observation
    target["history"].append(observation)
    target["history"] = target["history"][-max_samples:]
    state["updated_at"] = utc_now()
    return observation


def provider_health_status(
    state: dict[str, Any], *, provider: str, namespace: str
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
    if "UNCONFIGURED" in statuses:
        return "UNCONFIGURED"
    return "UNKNOWN"


def remember_observation(
    state: dict[str, Any],
    *,
    namespace: str,
    source: str,
    observation: Any,
    analysis: dict[str, Any] | None = None,
    valid_for_seconds: int | None = None,
    max_analysis_history: int = 12,
) -> dict[str, Any]:
    """Remember a non-heart observation and retain prior analyses when it changes."""
    canonical = canonicalize(observation)
    fp = fingerprint(canonical)
    key = f"{namespace}:{source}"
    previous = state["observations"].get(key)

    unchanged = bool(previous and previous.get("fingerprint") == fp)
    history = list(previous.get("analysis_history", [])) if previous else []

    previous_analysis = previous.get("analysis") if previous else None
    if previous and not unchanged and isinstance(previous_analysis, dict):
        history.append({
            "fingerprint": previous.get("fingerprint"),
            "observed_at": previous.get("observed_at"),
            "analysis": previous_analysis,
        })
        history = history[-max_analysis_history:]

    record = {
        "namespace": namespace,
        "source": source,
        "fingerprint": fp,
        "observed_at": utc_now(),
        "unchanged_from_previous": unchanged,
        "observation": canonical,
        "analysis": analysis if analysis is not None else (previous.get("analysis") if previous else None),
        "analysis_history": history,
    }

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
    now: datetime | None = None,
) -> dict[str, Any] | None:
    """Return previous analysis only when meaningful input is unchanged and still valid."""
    key = f"{namespace}:{source}"
    previous = state.get("observations", {}).get(key)
    if not previous or previous.get("fingerprint") != fingerprint(current_observation):
        return None

    analysis = previous.get("analysis")
    if not isinstance(analysis, dict):
        return None

    valid_for = previous.get("analysis_valid_for_seconds")
    observed_at = previous.get("observed_at")
    if valid_for is not None and observed_at:
        try:
            observed_dt = datetime.fromisoformat(observed_at)
            current_dt = now or datetime.now(timezone.utc)
            if (current_dt - observed_dt).total_seconds() > int(valid_for):
                return None
        except (ValueError, TypeError):
            return None
    return analysis
