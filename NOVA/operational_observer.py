#!/usr/bin/env python3
"""Observe external operational annotations without invoking an AI model.

Watched sources are configured in NOVA/watchlist.json. Each observation is
normalized and fingerprinted. Identical meaningful content is retained as the
same event, allowing a future reasoning stage to reuse a previous analysis
instead of making another AI call.

This observer does not decide repository changes and does not mutate source
configuration.
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

from health import atomic_write_json, load_json, load_health_state, remember_observation, utc_now


DEFAULT_WATCHLIST = {
    "schema_version": 1,
    "sources": []
}


def fetch_text(url: str, max_bytes: int, timeout: int) -> tuple[int | None, str, str | None]:
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
                payload = payload[:max_bytes]
            return response.status, payload.decode("utf-8", errors="replace"), None
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(max_bytes).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return exc.code, body, f"HTTP {exc.code}"
    except Exception as exc:
        return None, "", str(exc)


def normalize_content(content: str) -> str:
    # Remove common non-semantic HTML noise while preserving human-readable text.
    content = re.sub(r"(?is)<(script|style|noscript).*?>.*?</\1>", " ", content)
    content = re.sub(r"(?is)<[^>]+>", " ", content)
    content = re.sub(r"\s+", " ", content)
    return content.strip()


def observe_source(source: dict, state: dict, *, timeout: int, max_bytes: int) -> dict:
    name = source.get("name") or source.get("url")
    url = source.get("url")
    if not isinstance(url, str) or not url:
        return {
            "source": name,
            "status": "BLOCKED",
            "reason": "Source has no URL."
        }

    status, raw, error = fetch_text(url, max_bytes, timeout)
    normalized = normalize_content(raw)
    observation = {
        "url": url,
        "http_status": status,
        "content": normalized,
        "fetch_error": error,
    }
    memory = remember_observation(
        state,
        namespace="external-annotation",
        source=str(name),
        observation=observation,
    )

    return {
        "source": name,
        "url": url,
        "status": "ERROR" if error and not raw else ("UNCHANGED" if memory["unchanged_from_previous"] else "CHANGED"),
        "http_status": status,
        "fingerprint": memory["fingerprint"],
        "fetch_error": error,
    }


def run(root: Path) -> int:
    watchlist_path = root / "NOVA/watchlist.json"
    state_path = root / "NOVA/health_state.json"
    watchlist = load_json(watchlist_path, DEFAULT_WATCHLIST)
    state = load_health_state(state_path)

    results = []
    for source in watchlist.get("sources", []):
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

    print(json.dumps({
        "observed_at": state["last_annotation_scan"]["observed_at"],
        "results": results,
    }, indent=2, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    return run(Path(args.repo).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
