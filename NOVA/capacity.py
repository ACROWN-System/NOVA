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

    generic_mapping = {
        "requests": ("x-ratelimit-limit-requests", "x-ratelimit-remaining-requests", "x-ratelimit-reset-requests"),
        "tokens": ("x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens", "x-ratelimit-reset-tokens"),
    }
    provider_mapping = {
        "groq": generic_mapping,
    }

    metrics: dict[str, Any] = {}
    mapping = provider_mapping.get(provider_name, generic_mapping)
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



def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def capacity_opportunity(
    snapshot: Mapping[str, Any] | None,
    *,
    now: datetime | None = None,
    urgency_window_seconds: int | float = 300,
    minimum_remaining_reserve_fraction: float = 0.2,
    max_observation_age_seconds: int | float | None = None,
) -> dict[str, Any]:
    """Describe whether observed capacity should be used before its window resets/expires.

    This is an optimization signal, not a claim about provider truth. Only provider-
    exposed or explicitly supplied capacity is considered authoritative enough to
    influence scheduling. Unknown capacity never receives an artificial boost.
    """
    if not isinstance(snapshot, Mapping):
        return {
            "state": "UNKNOWN",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
        }

    observed_at = _parse_time(snapshot.get("observed_at"))
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    current = current.astimezone(timezone.utc)

    if observed_at is None:
        return {
            "state": "UNKNOWN",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
        }

    age = (current - observed_at).total_seconds()
    if age < 0:
        return {
            "state": "UNKNOWN",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
        }
    if max_observation_age_seconds is not None and age > float(max_observation_age_seconds):
        return {
            "state": "STALE",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
            "observation_age_seconds": age,
        }

    deadlines: list[tuple[str, datetime]] = []
    direct_expiration = _parse_time(snapshot.get("expiration_at"))
    if direct_expiration is not None:
        deadlines.append(("expiration", direct_expiration))

    reset_map = snapshot.get("estimated_next_reset_at")
    if isinstance(reset_map, Mapping):
        for metric, value in reset_map.items():
            deadline = _parse_time(value)
            if deadline is not None:
                deadlines.append((str(metric), deadline))

    if not deadlines:
        return {
            "state": "AVAILABLE_UNKNOWN_DEADLINE",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
            "observation_age_seconds": age,
        }

    positive_remaining: list[tuple[str, float, float | None]] = []
    for metric, data in (snapshot.get("metrics") or {}).items():
        if not isinstance(data, Mapping):
            continue
        remaining = _number(data.get("remaining"))
        limit = _number(data.get("limit"))
        if remaining is None or remaining <= 0:
            continue
        fraction = (float(remaining) / float(limit)) if limit and limit > 0 else None
        positive_remaining.append((str(metric), float(remaining), fraction))

    if not positive_remaining:
        return {
            "state": "EXHAUSTED_OR_NOT_EXPOSED",
            "priority": 0.0,
            "seconds_to_deadline": None,
            "metric": None,
            "observation_age_seconds": age,
        }

    positive_deadlines = [(metric, deadline) for metric, deadline in deadlines if deadline >= current]
    if not positive_deadlines:
        return {
            "state": "WINDOW_ENDED",
            "priority": 0.0,
            "seconds_to_deadline": 0.0,
            "metric": None,
            "observation_age_seconds": age,
        }

    metric, deadline = min(positive_deadlines, key=lambda item: item[1])
    seconds_to_deadline = (deadline - current).total_seconds()

    eligible = []
    for resource_metric, remaining, fraction in positive_remaining:
        if fraction is None or fraction > minimum_remaining_reserve_fraction:
            eligible.append((resource_metric, remaining, fraction))

    if not eligible:
        return {
            "state": "PROTECTED_RESERVE",
            "priority": 0.0,
            "seconds_to_deadline": seconds_to_deadline,
            "metric": metric,
            "observation_age_seconds": age,
        }

    window = max(float(urgency_window_seconds), 1.0)
    if seconds_to_deadline <= window:
        urgency = max(0.0, 1.0 - (seconds_to_deadline / window))
        return {
            "state": "EXPIRING_SOON",
            "priority": 1.0 + urgency,
            "seconds_to_deadline": seconds_to_deadline,
            "metric": metric,
            "remaining": max(item[1] for item in eligible),
            "observation_age_seconds": age,
        }

    return {
        "state": "AVAILABLE",
        "priority": 0.0,
        "seconds_to_deadline": seconds_to_deadline,
        "metric": metric,
        "remaining": max(item[1] for item in eligible),
        "observation_age_seconds": age,
    }


def provider_capacity_opportunity(
    targets: Mapping[str, Any] | None,
    *,
    provider: str,
    namespace: str,
    now: datetime | None = None,
    urgency_window_seconds: int | float = 300,
    minimum_remaining_reserve_fraction: float = 0.2,
    max_observation_age_seconds: int | float | None = None,
) -> dict[str, Any]:
    """Return the strongest current expiry opportunity across a provider's targets."""
    if not isinstance(targets, Mapping):
        return capacity_opportunity(None)

    prefix = f"{namespace}:{provider}:"
    candidates = []
    for key, target in targets.items():
        if not str(key).startswith(prefix) or not isinstance(target, Mapping):
            continue
        snapshot = target.get("last_capacity")
        opportunity = capacity_opportunity(
            snapshot,
            now=now,
            urgency_window_seconds=urgency_window_seconds,
            minimum_remaining_reserve_fraction=minimum_remaining_reserve_fraction,
            max_observation_age_seconds=max_observation_age_seconds,
        )
        candidates.append((float(opportunity.get("priority", 0.0)), opportunity))

    if not candidates:
        return capacity_opportunity(None)
    return max(candidates, key=lambda item: item[0])[1]

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
