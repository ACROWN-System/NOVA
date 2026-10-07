#!/usr/bin/env python3
"""Provider-neutral quota, credit, and renewal observation helpers.

Providers expose capacity differently. NOVA stores observations using common
names but preserves the provider-specific source and raw values. A missing
measurement is UNKNOWN, never assumed to be unlimited or zero-cost.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping


def _number(value: Any) -> float | int | None:
    if value is None:
        return None
    try:
        number = float(str(value).strip())
    except (TypeError, ValueError):
        return None
    return int(number) if number.is_integer() else number


def _seconds(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().lower()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        pass
    total = 0.0
    matched = False
    for amount, unit in re.findall(r"(\d+(?:\.\d+)?)\s*([dhms])", text):
        matched = True
        multiplier = {"d": 86400, "h": 3600, "m": 60, "s": 1}[unit]
        total += float(amount) * multiplier
    return total if matched else None


def _header_lookup(headers: Mapping[str, Any]) -> dict[str, str]:
    return {str(k).lower(): str(v) for k, v in headers.items()}


def extract_rate_limit_snapshot(
    provider: str,
    headers: Mapping[str, Any] | None = None,
    *,
    observed_at: str | None = None,
) -> dict[str, Any]:
    """Extract commonly available remaining/limit/reset fields from headers."""
    normalized = _header_lookup(headers or {})
    provider_name = provider.lower()

    prefix_maps = {
        "groq": {
            "requests": ("x-ratelimit-limit-requests", "x-ratelimit-remaining-requests", "x-ratelimit-reset-requests"),
            "tokens": ("x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens", "x-ratelimit-reset-tokens"),
        }
    }

    metrics: dict[str, Any] = {}
    mapping = prefix_maps.get(provider_name, {})
    for metric, (limit_key, remaining_key, reset_key) in mapping.items():
        present = any(k in normalized for k in (limit_key, remaining_key, reset_key))
        if not present:
            continue
        metrics[metric] = {
            "limit": _number(normalized.get(limit_key)),
            "remaining": _number(normalized.get(remaining_key)),
            "reset_after_seconds": _seconds(normalized.get(reset_key)),
            "source": "http_response_headers",
        }

    retry_after = _seconds(normalized.get("retry-after"))
    if retry_after is not None:
        metrics["retry_after_seconds"] = retry_after

    snapshot = {
        "provider": provider,
        "observed_at": observed_at or datetime.now(timezone.utc).isoformat(),
        "measurement_state": "OBSERVED" if metrics else "NOT_EXPOSED",
        "metrics": metrics,
    }

    if metrics:
        snapshot["estimated_next_reset_at"] = {}
        observed_dt = datetime.fromisoformat(snapshot["observed_at"])
        for metric, data in metrics.items():
            if not isinstance(data, dict):
                continue
            seconds = data.get("reset_after_seconds")
            if seconds is not None:
                snapshot["estimated_next_reset_at"][metric] = (
                    observed_dt + timedelta(seconds=float(seconds))
                ).isoformat()

    return snapshot


def merge_usage(
    quota_snapshot: dict[str, Any],
    usage: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Attach token/compute usage returned by the API without inventing missing values."""
    if not usage:
        return quota_snapshot
    normalized = {}
    for key, value in usage.items():
        if isinstance(value, (int, float)):
            normalized[str(key)] = value
        elif value is not None:
            numeric = _number(value)
            normalized[str(key)] = numeric if numeric is not None else str(value)
    if normalized:
        quota_snapshot["last_request_usage"] = normalized
    return quota_snapshot


def annotate_probe(
    probe: dict[str, Any],
    *,
    provider: str,
    headers: Mapping[str, Any] | None = None,
    usage: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    snapshot = extract_rate_limit_snapshot(provider, headers)
    snapshot = merge_usage(snapshot, usage)
    probe["capacity"] = snapshot
    return probe
