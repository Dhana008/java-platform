import os
import requests

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

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print(response.text)
