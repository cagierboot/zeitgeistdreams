import requests
import json

api_key = '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'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "training_file": "file-7as4vinolHytMlr7Fx5xkdDh",
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
