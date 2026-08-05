import os
import json
import urllib.request
import urllib.error
from datetime import datetime

# Read updated _01 environment variables
GROQ_API_KEY_01 = os.environ.get("GROQ_API_KEY_01")
GEMINI_API_KEY_01 = os.environ.get("GEMINI_API_KEY_01")

def call_groq(prompt):
    if not GROQ_API_KEY_01:
        print("Groq Warning: GROQ_API_KEY_01 is missing or not passed to environment.")
        return None
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY_01}",
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
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY_01}"
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
    
    if complexity == "low":
        response = call_groq(prompt)
        if response:
            return f"[ROUTED via GROQ Llama 3.3] {response}"
            
    print("Metacognitive Probe triggered failover/escalation to Gemini.")
    response = call_gemini(prompt)
    if response:
        return f"[ROUTED via GEMINI Flash] {response}"
        
    return "CRITICAL FAULT: All Phase 0 API endpoints unresponsive."

if __name__ == "__main__":
    test_prompt = "Generate the Phase 0 daily health check and treasury status report."
    system_state = intelligent_router(test_prompt, complexity="high")
    
    # Ensure NOVA directory exists before writing memory state
    os.makedirs("NOVA", exist_ok=True)
    with open("NOVA/README.md", "a") as f:
        f.write(f"\n\n### System Update: {datetime.utcnow().isoformat()}\n")
        f.write(f"{system_state}\n")
    print("NOVA state synced to memory ledger.")
