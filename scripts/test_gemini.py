import os
import requests
import time



api_key = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

with open("pr.diff", "r", encoding="utf-8") as f:
    diff = f.read()

with open(
    "standards/post-architecture-standards.md",
    "r",
    encoding="utf-8"
) as f:
    standards = f.read()
    
prompt = f"""
You are POST Architect.

POST Platform Standards:

{standards}

Review the following pull request
against these standards.

PR Diff:

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
response_json = response.json()

review = response_json["candidates"][0]["content"]["parts"][0]["text"]

print("\n")
print("=" * 80)
print("POST ARCHITECT REVIEW")
print("=" * 80)
print(review)

