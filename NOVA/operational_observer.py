#!/usr/bin/env python3
"""Observe external operational annotations without invoking an AI model.

Watched sources are configured in NOVA/watchlist.json. Meaningful content is
fingerprinted after transport noise is removed. A transient fetch failure does
not overwrite the last successful observation.

A future reasoning stage can call reusable_analysis() and avoid an AI call when
the same meaningful source content has already been analyzed and its validity
window has not expired.
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

try:
    from .health import (
        atomic_write_json,
        fingerprint,
        load_json,
        load_health_state,
        remember_observation,
        reusable_analysis,
        utc_now,
    )
except ImportError:  # direct script execution from the NOVA directory
    from health import (
        atomic_write_json,
        fingerprint,
        load_json,
        load_health_state,
        remember_observation,
        reusable_analysis,
        utc_now,
    )

DEFAULT_WATCHLIST = {"schema_version": 1, "sources": []}


def fetch_text(url: str, max_bytes: int, timeout: int) -> tuple[int | None, str, str | None]:
    if isinstance(max_bytes, bool) or not isinstance(max_bytes, int) or max_bytes < 1:
        return None, "", "Invalid max_bytes; must be a positive integer."
    if isinstance(timeout, bool) or not isinstance(timeout, int) or timeout < 1:
        return None, "", "Invalid timeout; must be a positive integer."

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "NOVA-Operational-Observer/1.0",
            "Accept": "text/html,application/xhtml+xml,text/plain,application/json,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read(max_bytes + 1)
            if len(payload) > max_bytes:
                return (
                    response.status,
                    "",
                    "Response exceeded configured max_bytes; incomplete content was not observed.",
                )
            return response.status, payload.decode("utf-8", errors="replace"), None
    except urllib.error.HTTPError as exc:
        # Do not return an HTTP error body as source content; it may contain
        # arbitrary diagnostic text and is not a successful source observation.
        return exc.code, "", f"HTTP {exc.code}"
    except Exception as exc:
        # Transport exception messages may contain URLs or request details.
        return None, "", f"Fetch failed ({type(exc).__name__}); details redacted."


def normalize_content(content: str) -> str:
    content = re.sub(r"(?is)<(script|style|noscript).*?>.*?</\1>", " ", content)
    content = re.sub(r"(?is)<[^>]+>", " ", content)
    content = re.sub(r"\s+", " ", content)
    return content.strip()


def validate_watchlist(watchlist: dict) -> list[dict]:
    """Reject ambiguous source identities before any source fetch or state access."""
    if not isinstance(watchlist, dict):
        raise RuntimeError("NOVA/watchlist.json must be a JSON object.")
    sources = watchlist.get("sources")
    if not isinstance(sources, list):
        raise RuntimeError("NOVA/watchlist.json must contain a sources array.")

    seen_identities: set[str] = set()
    seen_urls: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            raise RuntimeError(
                f"NOVA/watchlist.json sources[{index}] must be a JSON object."
            )

        url = source.get("url")
        if not isinstance(url, str) or not url.strip():
            raise RuntimeError(
                f"NOVA/watchlist.json sources[{index}] must have a non-empty URL."
            )
        try:
            parsed = urlsplit(url.strip())
        except ValueError as exc:
            raise RuntimeError(
                f"NOVA/watchlist.json sources[{index}] has an invalid URL."
            ) from exc
        if not parsed.scheme or not parsed.netloc:
            raise RuntimeError(
                f"NOVA/watchlist.json sources[{index}] URL must be absolute."
            )
        normalized_url = urlunsplit((
            parsed.scheme.casefold(),
            parsed.netloc.casefold(),
            parsed.path,
            parsed.query,
            parsed.fragment,
        ))
        if normalized_url in seen_urls:
            raise RuntimeError("NOVA/watchlist.json contains duplicate source URLs.")
        seen_urls.add(normalized_url)

        name = source.get("name")
        if name is not None and not isinstance(name, str):
            raise RuntimeError(
                f"NOVA/watchlist.json sources[{index}] name must be a string."
            )
        identity = name.strip().casefold() if isinstance(name, str) and name.strip() else normalized_url
        if identity in seen_identities:
            raise RuntimeError("NOVA/watchlist.json contains duplicate source identities.")
        seen_identities.add(identity)

    return sources


def observe_source(source: dict, state: dict, *, timeout: int, max_bytes: int) -> dict:
    name = source.get("name") or source.get("url")
    url = source.get("url")
    if not isinstance(url, str) or not url:
        return {"source": name, "status": "BLOCKED", "reason": "Source has no URL."}
    if not isinstance(state.get("events"), dict):
        return {
            "source": name,
            "url": url,
            "status": "BLOCKED",
            "reason": "Persisted event ledger is not a JSON object.",
        }

    status, raw, error = fetch_text(url, max_bytes, timeout)
    if error:
        return {
            "source": name,
            "url": url,
            "status": "ERROR",
            "http_status": status,
            "fetch_error": error,
        }

    normalized = normalize_content(raw)
    observation = {
        "url": url,
        "http_status": status,
        "content_fingerprint": fingerprint(normalized),
        "content_excerpt": normalized[:4000],
    }
    valid_for = source.get("analysis_valid_for_seconds")
    fresh_for = source.get("observation_fresh_for_seconds")
    previous_analysis = reusable_analysis(
        state,
        namespace="external-annotation",
        source=str(name),
        current_observation=observation,
    )
    memory = remember_observation(
        state,
        namespace="external-annotation",
        source=str(name),
        observation=observation,
        valid_for_seconds=int(valid_for) if valid_for is not None else None,
        fresh_for_seconds=int(fresh_for) if fresh_for is not None else None,
    )

    events = state["events"]
    has_pending_current_event = any(
        isinstance(event, dict)
        and event.get("source") == str(name)
        and event.get("analysis_status") == "PENDING"
        and event.get("fingerprint") == memory["fingerprint"]
        for event in events.values()
    )
    if (
        memory["unchanged_from_previous"]
        and previous_analysis is not None
        and not has_pending_current_event
    ):
        analysis_action = "REUSE_PRIOR_ANALYSIS"
    elif (
        memory["unchanged_from_previous"]
        and not isinstance(memory.get("analysis"), dict)
        and not memory.get("analysis_invalidated")
        and not has_pending_current_event
    ):
        analysis_action = "NO_CHANGE_NO_ANALYSIS"
    else:
        # A changed source, invalid legacy provenance, pending event, or
        # expired/untrusted analysis needs review even if source text is unchanged.
        analysis_action = "ANALYSIS_REQUIRED"

        # When new content replaces an older observation, an older pending event
        # must not later be analyzed against the latest source content.
        for previous_event in events.values():
            if (
                isinstance(previous_event, dict)
                and previous_event.get("source") == str(name)
                and previous_event.get("analysis_status") == "PENDING"
                and previous_event.get("fingerprint") != memory["fingerprint"]
            ):
                previous_event["analysis_status"] = "SUPERSEDED"
                previous_event["action_status"] = "SUPERSEDED_BY_NEW_OBSERVATION"
                previous_event["block_reason"] = (
                    "A newer successful source observation replaced this pending event."
                )
                previous_event["superseded_by_fingerprint"] = memory["fingerprint"]

        already_pending = any(
            isinstance(event, dict)
            and event.get("source") == str(name)
            and event.get("analysis_status") == "PENDING"
            and event.get("fingerprint") == memory["fingerprint"]
            for event in events.values()
        )
        if not already_pending:
            event_id_base = (
                f"{name}|{memory['fingerprint']}|{memory['observed_at']}"
            )
            event_id = event_id_base
            suffix = 2
            while event_id in events:
                event_id = f"{event_id_base}|{suffix}"
                suffix += 1

            events[event_id] = {
                "event_id": event_id,
                "event_type": "external-annotation-change",
                "source": str(name),
                "observed_at": memory["observed_at"],
                "fingerprint": memory["fingerprint"],
                "analysis_attempt_count": 0,
                "analysis_status": "PENDING",
                "action_status": "PENDING_POLICY_DECISION",
                "risk_level": source.get("risk_level", "UNKNOWN"),
            }

    return {
        "source": name,
        "url": url,
        "status": "UNCHANGED" if memory["unchanged_from_previous"] else "CHANGED",
        "analysis_action": analysis_action,
        "http_status": status,
        "fingerprint": memory["fingerprint"],
    }


def run(root: Path) -> int:
    watchlist = load_json(root / "NOVA/watchlist.json", DEFAULT_WATCHLIST)
    sources = validate_watchlist(watchlist)
    state_path = root / "NOVA/health_state.json"
    state = load_health_state(state_path)

    results = []
    for source in sources:
        if not source.get("enabled", True):
            continue
        results.append(
            observe_source(
                source,
                state,
                timeout=int(source.get("timeout_seconds", 15)),
                max_bytes=int(source.get("max_bytes", 262144)),
            )
        )

    state["last_annotation_scan"] = {
        "observed_at": utc_now(),
        "results": results,
    }
    atomic_write_json(state_path, state)

    print(json.dumps(state["last_annotation_scan"], indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    return run(Path(args.repo).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
