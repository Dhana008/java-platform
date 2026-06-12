import os
import requests
import time



api_key = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

with open("pr.diff", "r", encoding="utf-8") as f:
    diff = f.read()

prompt = f"""
You are POST Architect.

Review this pull request and provide:

1. Summary
2. Architecture Concerns
3. Security Concerns
4. Reliability Concerns
5. Risk Score (1-10)

Ignore:
- Formatting
- Naming conventions
- Code style

Pull Request Diff:

{diff[:15000]}
"""

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

for attempt in range(3):
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        break

    print(f"Attempt {attempt+1} failed: {response.status_code}")
    time.sleep(10)

print("Status Code:", response.status_code)
print(response.text)
