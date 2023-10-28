import requests
import json

api_key = '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'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "training_file": "file-hfp6URl9U7LA4BTNIudxgjRW",
    "model": "gpt-3.5-turbo-0613"
}

response = requests.post(
    "https://api.openai.com/v1/fine_tuning/jobs",
    headers=headers,
    data=json.dumps(data)
)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.text)
