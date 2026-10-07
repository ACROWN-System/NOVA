#!/usr/bin/env python3
"""Provider-agnostic economic accounting for NOVA.

Public service pricing is deliberately independent from the backend provider.
Free capacity reduces internal cost; it never changes the user's tariff.
Paid-provider costs are charged to the common operating pool.
"""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from typing import Any


def money(value: Any) -> Decimal:
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        return Decimal("0")


def service_price(pricing_policy: dict[str, Any], service: str) -> dict[str, Any]:
    services = pricing_policy.get("services", {})
    record = services.get(service)
    if not isinstance(record, dict):
        raise KeyError(f"Unknown service: {service}")
    return record


def provider_cost(
    provider: dict[str, Any],
    *,
    input_tokens: int = 0,
    output_tokens: int = 0,
    units: Decimal | int | float = 0,
    gpu_hours: Decimal | int | float = 0,
) -> Decimal:
    pricing = provider.get("pricing", {})
    if pricing.get("free", False):
        return Decimal("0")

    unit = str(pricing.get("unit", "request"))
    if unit == "token":
        in_rate = money(pricing.get("input_per_million_tokens", 0))
        out_rate = money(pricing.get("output_per_million_tokens", 0))
        return (
            Decimal(input_tokens) * in_rate / Decimal(1_000_000)
            + Decimal(output_tokens) * out_rate / Decimal(1_000_000)
        )
    if unit == "gpu_hour":
        return Decimal(str(gpu_hours)) * money(pricing.get("per_gpu_hour", 0))
    if unit == "unit":
        return Decimal(str(units)) * money(pricing.get("per_unit", 0))
    return money(pricing.get("per_request", 0))


def record_transaction(
    state: dict[str, Any],
    *,
    service: str,
    public_price_amount: Decimal | int | float,
    public_price_asset: str,
    provider_name: str,
    provider_cost_amount: Decimal | int | float,
    provider_cost_asset: str,
    free_resource: bool,
    resource_usage: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Record revenue and internal backend cost without changing public price."""
    revenue = money(public_price_amount)
    cost = money(provider_cost_amount)
    contribution = revenue - cost

    entry = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "service": service,
        "public_price": {
            "amount": str(revenue),
            "asset": public_price_asset,
        },
        "provider": provider_name,
        "provider_cost": {
            "amount": str(cost),
            "asset": provider_cost_asset,
        },
        "free_resource": bool(free_resource),
        "operating_contribution": {
            "amount": str(contribution),
            "asset": public_price_asset if public_price_asset == provider_cost_asset else "MIXED",
        },
        "resource_usage": resource_usage or {},
    }

    state.setdefault("transactions", []).append(entry)
    state["transactions"] = state["transactions"][-1000:]
    state["operating_pool"] = str(
        money(state.get("operating_pool", "0")) + contribution
    )
    state["updated_at"] = entry["recorded_at"]
    return entry


def transition_status(
    state: dict[str, Any],
    *,
    projected_paid_cost: Decimal | int | float,
    replenish_target: Decimal | int | float,
    minimum_runway_ratio: Decimal | int | float = 1,
) -> str:
    """Classify continuity before switching from free capacity to paid resources."""
    pool = money(state.get("operating_pool", "0"))
    projected = money(projected_paid_cost)
    target = money(replenish_target)
    threshold = target * money(minimum_runway_ratio)

    if projected <= 0:
        return "NO_PAID_COST_REQUIRED"
    if pool >= threshold:
        return "CONTINUITY_FUNDED"
    if pool > 0:
        return "RUNWAY_WARNING"
    return "PAYMENT_BLOCKED"
