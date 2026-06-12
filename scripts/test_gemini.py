import os
import requests
import time



api_key = os.environ["GEMINI_API_KEY"]

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "You are POST Architect. Say hello and confirm you are operational."
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
