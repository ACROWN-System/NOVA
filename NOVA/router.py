import os
import json
import urllib.request
import urllib.error
from datetime import datetime

# Auto-sanitize quotes and whitespace
GROQ_API_KEY_01 = os.environ.get("GROQ_API_KEY_01", "").strip().strip('"').strip("'")
GEMINI_API_KEY_01 = os.environ.get("GEMINI_API_KEY_01", "").strip().strip('"').strip("'")

# Standard Headers to prevent Cloudflare Error 1010 (User-Agent blocking)
COMMON_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def call_groq(prompt):
    if not GROQ_API_KEY_01:
        print("Groq Warning: GROQ_API_KEY_01 is missing or empty.")
        return None
        
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        **COMMON_HEADERS,
        "Authorization": f"Bearer {GROQ_API_KEY_01}"
    }
    
    for model in ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]:
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1
        }
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            print(f"Groq HTTP Error {e.code} ({model}): {err_body}")
        except Exception as e:
            print(f"Groq Exception ({model}): {e}")
            
    return None

def call_gemini(prompt):
    if not GEMINI_API_KEY_01:
        print("Gemini Warning: GEMINI_API_KEY_01 is missing or empty.")
        return None
    
    headers = {
        **COMMON_HEADERS,
        "x-goog-api-key": GEMINI_API_KEY_01
    }
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.1}
    }
    
    for model in ["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash"]:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            print(f"Gemini HTTP Error {e.code} ({model}): {err_body}")
        except Exception as e:
            print(f"Gemini Exception ({model}): {e}")
            
    return None

def intelligent_router(prompt, complexity="low"):
    print(f"[{datetime.utcnow().isoformat()}] NOVA Routing Sequence Initiated...")
    
    if complexity == "high":
        print("Executing Primary Route: Gemini Flash")
        res = call_gemini(prompt)
        if res:
            return f"[ROUTED via GEMINI Flash] {res}"
        print("Primary Route Failed. Executing Failover to Groq Llama...")
        res = call_groq(prompt)
        if res:
            return f"[ROUTED via GROQ Llama (FAILOVER)] {res}"
    else:
        print("Executing Primary Route: Groq Llama")
        res = call_groq(prompt)
        if res:
            return f"[ROUTED via GROQ Llama] {res}"
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
