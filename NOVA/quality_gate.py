"""Small deterministic gates for provider contracts and root-cause case closure.

This module intentionally contains policy decisions only: no network calls, model
judgment, new database, or provider-specific transport code.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Any

VERIFIED_CAPABILITY_STATES = {"VERIFIED"}
CASE_OPEN_STATE = "INVESTIGATION_REQUIRED"
CASE_CLOSED_STATE = "VERIFIED_CLOSED"
SHA1_RE = re.compile(r"^[0-9a-f]{40}$")

CLOSURE_FIELDS = (
    "expected_result",
    "observed_result",
    "direct_cause",
    "systemic_cause",
    "missed_control",
    "prevention_control",
    "regression_test",
    "verification_result",
    "candidate_sha",
    "verified_candidate_sha",
    "verified_at",
)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


_CASE_REQUIRED_TEXT_FIELDS = (
    "source",
    "failure_class",
    "expected_result",
    "observed_result",
    "state",
    "first_seen",
    "last_seen",
)


def validate_quality_cases_payload(
    cases: Any, *, description: str = "NOVA quality_cases"
) -> dict[str, dict[str, Any]]:
    """Reject malformed persisted RCA cases without changing or discarding them.

    Optional closure fields remain optional for compatibility with existing
    open cases. If a counter or optional field is present, its type is checked.
    """
    if not isinstance(cases, dict):
        raise RuntimeError(
            f"{description} must be a JSON object; refusing to reset persisted RCA cases."
        )

    for key, case in cases.items():
        if not isinstance(key, str) or not key.strip():
            raise RuntimeError(
                f"{description} contains an empty or non-string case key; "
                "refusing to reset persisted RCA cases."
            )
        if not isinstance(case, dict):
            raise RuntimeError(
                f"{description} entry '{key}' must be a JSON object; "
                "refusing to overwrite persisted RCA evidence."
            )
        if not _nonempty(case.get("case_id")) or case["case_id"] != key:
            raise RuntimeError(
                f"{description} entry '{key}' has a missing or mismatched case_id; "
                "refusing to overwrite persisted RCA evidence."
            )
        for field in _CASE_REQUIRED_TEXT_FIELDS:
            if not _nonempty(case.get(field)):
                raise RuntimeError(
                    f"{description} entry '{key}' field '{field}' must be a non-empty string; "
                    "refusing to overwrite persisted RCA evidence."
                )

        occurrences = case.get("occurrences")
        if occurrences is not None and (
            isinstance(occurrences, bool)
            or not isinstance(occurrences, int)
            or occurrences < 1
        ):
            raise RuntimeError(
                f"{description} entry '{key}' field 'occurrences' must be a positive integer; "
                "refusing to overwrite persisted RCA evidence."
            )
        reopened_count = case.get("reopened_count")
        if reopened_count is not None and (
            isinstance(reopened_count, bool)
            or not isinstance(reopened_count, int)
            or reopened_count < 0
        ):
            raise RuntimeError(
                f"{description} entry '{key}' field 'reopened_count' must be a non-negative integer; "
                "refusing to overwrite persisted RCA evidence."
            )

        if "candidate_sha" in case and case["candidate_sha"] is not None and not isinstance(
            case["candidate_sha"], str
        ):
            raise RuntimeError(
                f"{description} entry '{key}' field 'candidate_sha' must be a string or null; "
                "refusing to overwrite persisted RCA evidence."
            )
        for field in CLOSURE_FIELDS:
            if field in case and not _nonempty(case[field]):
                raise RuntimeError(
                    f"{description} entry '{key}' field '{field}' must be a non-empty string when present; "
                    "refusing to overwrite persisted RCA evidence."
                )
        if "closed_at" in case and not _nonempty(case["closed_at"]):
            raise RuntimeError(
                f"{description} entry '{key}' field 'closed_at' must be a non-empty string when present; "
                "refusing to overwrite persisted RCA evidence."
            )
        if "last_verified_closure" in case and not isinstance(
            case["last_verified_closure"], dict
        ):
            raise RuntimeError(
                f"{description} entry '{key}' field 'last_verified_closure' must be a JSON object; "
                "refusing to overwrite persisted RCA evidence."
            )

    return cases


def model_capability_decision(
    provider: dict[str, Any],
    model: str,
    capability: str,
) -> dict[str, Any]:
    """Fail closed when a provider declares a model contract that is not verified.

    Providers without a model_contracts record remain on the existing legacy
    path during staged adoption. Once a provider declares model_contracts, an
    absent model/capability entry is blocked rather than silently assumed.
    """
    if "model_contracts" not in provider:
        return {
            "allowed": True,
            "status": "LEGACY_UNDECLARED",
            "reason": "No model-specific contract gate is declared for this provider.",
        }

    contracts = provider.get("model_contracts")
    if not isinstance(contracts, dict):
        return {
            "allowed": False,
            "status": "BLOCKED_CONTRACT_UNVERIFIED",
            "reason": "The declared model_contracts field is not a JSON object.",
        }

    contract = contracts.get(model)
    if not isinstance(contract, dict):
        return {
            "allowed": False,
            "status": "BLOCKED_CONTRACT_UNVERIFIED",
            "reason": "The model has no declared contract record.",
        }

    status = str(contract.get(capability, "UNKNOWN")).upper()
    if status in VERIFIED_CAPABILITY_STATES:
        return {
            "allowed": True,
            "status": "VERIFIED",
            "reason": "The required model capability has been verified.",
        }

    return {
        "allowed": False,
        "status": "BLOCKED_CONTRACT_UNVERIFIED",
        "reason": f"Required capability '{capability}' is not verified for this model.",
    }


def _case_signature(source: str, failure_class: str, expected_result: str) -> str:
    payload = json.dumps(
        {
            "source": source,
            "failure_class": failure_class,
            "expected_result": expected_result,
        },
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "rca-" + hashlib.sha256(payload).hexdigest()[:16]


def record_failure_case(
    state: dict[str, Any],
    *,
    source: str,
    failure_class: str,
    expected_result: str,
    observed_result: str,
    candidate_sha: str | None = None,
    now: str | None = None,
) -> dict[str, Any]:
    """Open or join a sanitized RCA case; repeated failures do not duplicate it.

    Only stable classifications and short caller-authored descriptions belong
    here. Callers must not provide raw prompts, response bodies, or credentials.
    """
    if not isinstance(state, dict):
        raise RuntimeError("NOVA health state must be a JSON object to record an RCA case.")
    if "quality_cases" not in state:
        state["quality_cases"] = {}
    cases = validate_quality_cases_payload(
        state["quality_cases"], description="NOVA health state field 'quality_cases'"
    )

    stamp = now or _now_iso()
    case_id = _case_signature(source, failure_class, expected_result)
    existing = cases.get(case_id)
    if not isinstance(existing, dict):
        existing = {
            "case_id": case_id,
            "source": source[:200],
            "failure_class": failure_class[:100],
            "expected_result": expected_result[:240],
            "observed_result": observed_result[:240],
            "candidate_sha": candidate_sha,
            "state": CASE_OPEN_STATE,
            "first_seen": stamp,
            "last_seen": stamp,
            "occurrences": 1,
            "reopened_count": 0,
        }
        cases[case_id] = existing
        return existing

    if existing.get("state") == CASE_CLOSED_STATE:
        existing["last_verified_closure"] = {
            key: existing.get(key)
            for key in CLOSURE_FIELDS
            if key in existing
        }
        existing["reopened_count"] = int(existing.get("reopened_count", 0)) + 1
        for key in CLOSURE_FIELDS:
            existing.pop(key, None)
        existing["state"] = CASE_OPEN_STATE

    existing["last_seen"] = stamp
    existing["occurrences"] = int(existing.get("occurrences", 0)) + 1
    # Restoring the expected result is essential after recurrence reopens a
    # previously closed case and clears its former closure evidence.
    existing["expected_result"] = expected_result[:240]
    existing["observed_result"] = observed_result[:240]
    if candidate_sha:
        existing["candidate_sha"] = candidate_sha
    return existing


def closure_decision(case: dict[str, Any]) -> dict[str, Any]:
    """Return whether evidence is sufficient for VERIFIED_CLOSED."""
    missing = [
        field
        for field in CLOSURE_FIELDS
        if not _nonempty(case.get(field))
    ]
    if missing:
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "Required root-cause, prevention, or verification evidence is missing.",
            "missing_fields": missing,
        }

    candidate_sha = str(case["candidate_sha"]).lower()
    verified_sha = str(case["verified_candidate_sha"]).lower()
    if not SHA1_RE.fullmatch(candidate_sha) or not SHA1_RE.fullmatch(verified_sha):
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "A full 40-character candidate commit SHA is required.",
            "missing_fields": [],
        }
    if candidate_sha != verified_sha:
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "Verification was not performed on the exact candidate commit.",
            "missing_fields": [],
        }
    if str(case["verification_result"]).upper() != "PASS":
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "Regression verification did not pass.",
            "missing_fields": [],
        }
    try:
        verified_at = datetime.fromisoformat(str(case["verified_at"]).replace("Z", "+00:00"))
        if verified_at.tzinfo is None or verified_at.utcoffset() is None:
            raise ValueError("timestamp must include a timezone")
    except ValueError:
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "Verification timestamp must be a valid timezone-aware ISO-8601 value.",
            "missing_fields": [],
        }

    return {
        "allowed": True,
        "state": CASE_CLOSED_STATE,
        "reason": "Root cause, prevention, exact-commit regression verification, and timestamp are recorded.",
        "missing_fields": [],
    }


def close_failure_case(
    state: dict[str, Any],
    case_id: str,
    evidence: dict[str, Any],
) -> dict[str, Any]:
    """Close a case only if the deterministic evidence gate passes."""
    cases = state.get("quality_cases")
    case = cases.get(case_id) if isinstance(cases, dict) else None
    if not isinstance(case, dict):
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "The root-cause case does not exist.",
            "missing_fields": [],
        }

    unexpected = sorted(set(evidence) - set(CLOSURE_FIELDS))
    if unexpected:
        return {
            "allowed": False,
            "state": "BLOCKED",
            "reason": "Closure evidence contains fields outside the approved evidence schema.",
            "missing_fields": [],
        }

    candidate = {**case, **evidence}
    decision = closure_decision(candidate)
    if not decision["allowed"]:
        return decision

    case.update(evidence)
    case["state"] = CASE_CLOSED_STATE
    case["closed_at"] = case["verified_at"]
    return decision
