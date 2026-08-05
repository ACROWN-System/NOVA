import os
import json
import urllib.request
import urllib.error
from datetime import datetime

GROQ_API_KEY_01 = os.environ.get("GROQ_API_KEY_01")
GEMINI_API_KEY_01 = os.environ.get("GEMINI_API_KEY_01")

def call_groq(prompt):
    if not GROQ_API_KEY_01:
        print("Groq Warning: GROQ_API_KEY_01 is missing or not passed to environment.")
        return None
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY_01.strip()}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.URLError as e:
        print(f"Groq Probe Failed: {e}")
        return None

def call_gemini(prompt):
    if not GEMINI_API_KEY_01:
        print("Gemini Warning: GEMINI_API_KEY_01 is missing or not passed to environment.")
        return None
    
    # Updated to active Gemini model endpoint
    key = GEMINI_API_KEY_01.strip()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.1}
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["candidates"][0]["content"]["parts"][0]["text"]
    except urllib.error.URLError as e:
        print(f"Gemini Probe Failed: {e}")
        return None

def intelligent_router(prompt, complexity="low"):
    print(f"[{datetime.utcnow().isoformat()}] NOVA Routing Sequence Initiated...")
    
    # Primary Route: Gemini for high complexity, Groq for low
    if complexity == "high":
        print("Executing Primary Route: Gemini Flash")
        res = call_gemini(prompt)
        if res:
            return f"[ROUTED via GEMINI Flash] {res}"
        print("Primary Route Failed. Executing Failover to Groq Llama 3.3...")
        res = call_groq(prompt)
        if res:
            return f"[ROUTED via GROQ Llama 3.3 (FAILOVER)] {res}"
    else:
        print("Executing Primary Route: Groq Llama 3.3")
        res = call_groq(prompt)
        if res:
            return f"[ROUTED via GROQ Llama 3.3] {res}"
        print("Primary Route Failed. Executing Failover to Gemini Flash...")
        res = call_gemini(prompt)
        if res:
            return f"[ROUTED via GEMINI Flash (FAILOVER)] {res}"

    return "CRITICAL FAULT: All Phase 0 API endpoints unresponsive."

if __name__ == "__main__":
    test_prompt = "Generate the Phase 0 daily health check and treasury status report."
    system_state = intelligent_router(test_prompt, complexity="high")
    
    os.makedirs("NOVA", exist_ok=True)
    with open("NOVA/README.md", "a") as f:
        f.write(f"\n\n### System Update: {datetime.utcnow().isoformat()}\n")
        f.write(f"{system_state}\n")
    print("NOVA state synced to memory ledger.")
