import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

import alerts  # NOVA/alerts.py — comparative-analysis generation + GitHub/SMS/voice delivery

ROSTER_PATH = os.path.join(os.path.dirname(__file__), "roster.json")

COMMON_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Keywords that show up in provider error bodies when a model is PERMANENTLY gone
# (retired/decommissioned/etc), as opposed to a transient hiccup (timeout, 5xx, rate limit).
PERMANENT_ERROR_MARKERS = [
    "decommissioned", "deprecated", "no longer supported", "no longer available",
    "has been retired", "model_not_found", "does not exist",
]


def load_roster():
    with open(ROSTER_PATH, "r") as f:
        return json.load(f)


def save_roster(roster):
    with open(ROSTER_PATH, "w") as f:
        json.dump(roster, f, indent=2)
        f.write("\n")


def get_env(name):
    return os.environ.get(name, "").strip().strip('"').strip("'")


def classify_http_error(e):
    """Returns 'permanent' if the error body indicates the model is gone for good,
    otherwise 'transient' (timeout, rate limit, server error, etc)."""
    try:
        body = e.read().decode("utf-8", errors="ignore").lower()
    except Exception:
        body = ""
    if e.code == 404 or any(marker in body for marker in PERMANENT_ERROR_MARKERS):
        return "permanent", body
    return "transient", body


def call_openai_compatible(provider, prompt):
    """Groq, Cerebras, Mistral, Cloudflare — all speak the same chat-completions shape."""
    api_key = get_env(provider["api_key_env"])
    if not api_key:
        print(f"[{provider['name']}] Warning: {provider['api_key_env']} is missing or empty.")
        return None, "transient"  # treat missing key as transient/unconfigured, not a dead model

    base_url = provider["base_url"]
    if "account_id_env" in provider:
        account_id = get_env(provider["account_id_env"])
        if not account_id:
            print(f"[{provider['name']}] Warning: {provider['account_id_env']} is missing.")
            return None, "transient"
        base_url = base_url.format(CF_ACCOUNT_ID=account_id)

    headers = {**COMMON_HEADERS, "Authorization": f"Bearer {api_key}"}
    worst_signal = None

    for model in provider["models"]:
        data = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.1}
        req = urllib.request.Request(base_url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"], None
        except urllib.error.HTTPError as e:
            signal, body = classify_http_error(e)
            print(f"[{provider['name']}] HTTP {e.code} on model '{model}' ({signal}): {body[:200]}")
            worst_signal = signal if worst_signal != "permanent" else worst_signal
            # keep trying the provider's other models regardless of signal type
        except Exception as e:
            print(f"[{provider['name']}] Exception on model '{model}': {e}")
            worst_signal = worst_signal or "transient"

    # every model for this provider failed this run
    return None, (worst_signal or "transient")


def call_gemini(provider, prompt):
    api_key = get_env(provider["api_key_env"])
    if not api_key:
        print(f"[{provider['name']}] Warning: {provider['api_key_env']} is missing or empty.")
        return None, "transient"

    headers = {**COMMON_HEADERS, "x-goog-api-key": api_key}
    data = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.1}}
    worst_signal = None

    for model in provider["models"]:
        url = f"{provider['base_url']}/{model}:generateContent"
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["candidates"][0]["content"]["parts"][0]["text"], None
        except urllib.error.HTTPError as e:
            signal, body = classify_http_error(e)
            print(f"[{provider['name']}] HTTP {e.code} on model '{model}' ({signal}): {body[:200]}")
            worst_signal = signal if worst_signal != "permanent" else worst_signal
        except Exception as e:
            print(f"[{provider['name']}] Exception on model '{model}': {e}")
            worst_signal = worst_signal or "transient"

    return None, (worst_signal or "transient")


def call_provider(provider, prompt):
    if provider["kind"] == "gemini":
        return call_gemini(provider, prompt)
    return call_openai_compatible(provider, prompt)


def intelligent_router(prompt):
    print(f"[{datetime.now(timezone.utc).isoformat()}] NOVA Routing Sequence Initiated...")
    roster = load_roster()
    active = [p for p in roster["providers"] if p["status"] == "active"]

    for provider in active:
        print(f"Trying provider: {provider['name']}")
        text, signal = call_provider(provider, prompt)
        if text:
            return f"[ROUTED via {provider['name'].upper()}] {text}"

        if signal == "permanent":
            print(f"[{provider['name']}] All models permanently unavailable — marking provider DOWN.")
            provider["status"] = "down"
            provider["marked_down_at"] = datetime.now(timezone.utc).isoformat()
            # Save immediately — do NOT wait until after the loop. A successful failover to
            # the next provider returns early, which would otherwise skip persisting this
            # change entirely, causing the dead provider to be re-tried and re-alerted every run.
            save_roster(roster)

            remaining = [p for p in roster["providers"] if p["status"] == "active"]
            analysis = alerts.generate_comparative_analysis(roster, provider["name"], remaining)
            severity = "urgent" if len(remaining) <= 2 else "notice"
            alerts.send_all_alerts(
                title=f"NOVA roster alert: {provider['name']} appears permanently unavailable",
                body=analysis,
                severity=severity,
            )
        # transient failures: just move on to the next provider for THIS call, no roster change

    return "CRITICAL FAULT: All roster providers unresponsive this cycle."


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-alert":
        # Fabricates a synthetic "provider down" event and pushes it through every
        # configured alert channel, WITHOUT touching the real roster. Use this to
        # prove GitHub/SMS/voice delivery works before relying on a real failure.
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
        sys.exit(0)

    test_prompt = "Generate the Phase 0 daily health check and treasury status report."
    system_state = intelligent_router(test_prompt)

    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "a") as f:
        f.write(f"\n\n### System Update: {datetime.now(timezone.utc).isoformat()}\n")
        f.write(f"{system_state}\n")
    print("NOVA state synced to memory ledger.")
