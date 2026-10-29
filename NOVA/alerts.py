import os
import json
import base64
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timezone

try:
    from .health import loads_json_no_duplicate_keys
except ImportError:  # Direct script execution
    from health import loads_json_no_duplicate_keys


def get_env(name):
    return os.environ.get(name, "").strip().strip('"').strip("'")


# ---------------------------------------------------------------------------
# Comparative analysis (the content of the alert)
# ---------------------------------------------------------------------------

def generate_comparative_analysis(roster, dead_provider_name, remaining_active):
    lines = []
    lines.append(f"**Provider affected:** {dead_provider_name}")
    lines.append(f"**Remaining active providers in roster:** {len(remaining_active)} of {len(roster['providers'])}")
    lines.append("")
    lines.append("### Current roster status")
    for p in roster["providers"]:
        marker = "live" if p["status"] == "active" else "DOWN"
        lines.append(f"- {p['name']} — {marker} — models: {', '.join(p['models'])}")

    lines.append("")
    lines.append("### Candidate replacements not currently in the roster")
    for c in roster.get("candidates_not_in_roster", []):
        lines.append(f"- {c}")

    lines.append("")
    if len(remaining_active) <= 2:
        lines.append(
            "### Recommendation (URGENT)\n"
            "Roster margin is low. Recommend approving a replacement provider soon — "
            "NOVA still has failover coverage for now, but the safety margin the roster "
            "was designed around is gone."
        )
    else:
        lines.append(
            "### Recommendation\n"
            "Roster still has comfortable margin. No immediate action required, but "
            "approving a replacement keeps the roster back at full strength."
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Channel: GitHub Issue (free — repo collaborators get this by email automatically)
# ---------------------------------------------------------------------------

def send_github_issue(title, body):
    """Create or append to one open issue per exact alert title.

    Listing failures fail closed instead of creating a duplicate during an
    API outage. Existing issue history is preserved; new observations become
    comments rather than silently overwriting the original report.
    """
    token = get_env("GITHUB_TOKEN")
    repo = get_env("GITHUB_REPOSITORY")  # auto-set by Actions as "owner/repo"
    if not token or not repo:
        print("[alerts:github] GITHUB_TOKEN / GITHUB_REPOSITORY not set — skipping (this channel needs "
              "'permissions: issues: write' and GITHUB_TOKEN passed into the job's env in nova_heartbeat.yml).")
        return False

    base_url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    }
    try:
        # Search current open issues before creating anything. This endpoint
        # includes pull requests, so exclude records carrying pull_request.
        list_req = urllib.request.Request(
            f"{base_url}/issues?state=open&per_page=100",
            headers=headers,
            method="GET",
        )
        with urllib.request.urlopen(list_req, timeout=15) as response:
            open_items = loads_json_no_duplicate_keys(response.read().decode("utf-8"))
        if not isinstance(open_items, list):
            print("[alerts:github] Open-issue listing returned an invalid payload; refusing duplicate creation.")
            return False

        existing = next(
            (
                item for item in open_items
                if isinstance(item, dict)
                and item.get("title") == title
                and "pull_request" not in item
                and isinstance(item.get("number"), int)
            ),
            None,
        )
        stamp = datetime.now(timezone.utc).isoformat()
        if existing:
            comment_url = f"{base_url}/issues/{existing['number']}/comments"
            comment = (
                f"Additional alert observation at {stamp}. "
                "The existing issue is retained to avoid duplicates.\n\n"
                f"{body}"
            )
            comment_req = urllib.request.Request(
                comment_url,
                data=json.dumps({"body": comment}).encode("utf-8"),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(comment_req, timeout=15) as response:
                loads_json_no_duplicate_keys(response.read().decode("utf-8"))
            print(f"[alerts:github] Reused open issue: {existing.get('html_url')}")
            return True

        create_req = urllib.request.Request(
            f"{base_url}/issues",
            data=json.dumps({"title": title, "body": body}).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(create_req, timeout=15) as response:
            result = loads_json_no_duplicate_keys(response.read().decode("utf-8"))
            print(f"[alerts:github] Issue opened: {result.get('html_url')}")
            return True
    except Exception as e:
        print(f"[alerts:github] Failed to record alert without duplicating issues: {e}")
        return False


# ---------------------------------------------------------------------------
# Channel: SMS + voice via Twilio (NOT free at production scale — trial credit
# only, verified-recipient-only. Intended here for a one-time feasibility test,
# per plan: prove it works now, swap to a paid Twilio account before relying on
# it operationally.)
# ---------------------------------------------------------------------------

def _twilio_credentials():
    sid = get_env("TWILIO_ACCOUNT_SID")
    token = get_env("TWILIO_AUTH_TOKEN")
    from_number = get_env("TWILIO_FROM_NUMBER")
    to_number = get_env("TWILIO_TO_NUMBER")
    if not all([sid, token, from_number, to_number]):
        return None
    return sid, token, from_number, to_number


def _twilio_request(path, form_fields, sid, token):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/{path}"
    auth = base64.b64encode(f"{sid}:{token}".encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = urllib.parse.urlencode(form_fields).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=15) as response:
        return loads_json_no_duplicate_keys(response.read().decode("utf-8"))


def send_sms(body):
    creds = _twilio_credentials()
    if not creds:
        print("[alerts:sms] Twilio credentials not configured — skipping "
              "(TWILIO_ACCOUNT_SID / TWILIO_AUTH_TOKEN / TWILIO_FROM_NUMBER / TWILIO_TO_NUMBER). "
              "This is the placeholder for when a Twilio account exists.")
        return False
    sid, token, from_number, to_number = creds
    try:
        result = _twilio_request(
            "Messages.json",
            {"To": to_number, "From": from_number, "Body": body[:1500]},
            sid, token,
        )
        print(f"[alerts:sms] Sent, sid={result.get('sid')}")
        return True
    except Exception as e:
        print(f"[alerts:sms] Failed: {e}")
        return False


def send_voice(body):
    creds = _twilio_credentials()
    if not creds:
        print("[alerts:voice] Twilio credentials not configured — skipping "
              "(same env vars as SMS). This is the placeholder for when a Twilio account exists.")
        return False
    sid, token, from_number, to_number = creds
    # Keep the spoken message short — this is a voice call, not the full analysis.
    spoken = "NOVA alert. " + body.split("\n")[0].replace("*", "")
    twiml = f"<Response><Say voice=\"alice\">{spoken[:500]}</Say></Response>"
    try:
        result = _twilio_request(
            "Calls.json",
            {"To": to_number, "From": from_number, "Twiml": twiml},
            sid, token,
        )
        print(f"[alerts:voice] Placed, sid={result.get('sid')}")
        return True
    except Exception as e:
        print(f"[alerts:voice] Failed: {e}")
        return False


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

def send_all_alerts(title, body, severity="notice", force_all_channels=False):
    """GitHub issue always fires (it's free and low-friction). SMS/voice only fire
    for 'urgent' severity, or when force_all_channels=True (used by --test-alert),
    so routine 1-provider-down notices don't page anyone's phone."""
    send_github_issue(title, body)

    if severity == "urgent" or force_all_channels:
        send_sms(f"{title}\n\n{body[:1000]}")
        send_voice(body)
    else:
        print("[alerts] Severity is 'notice' — SMS/voice skipped, GitHub issue only.")
