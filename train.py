
import requests
import json

api_key = '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'  # Replace with your new API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "training_file": "file-bwUPR4N4lP5RVlylNk2XvmJ5",
    "model": "gpt-3.5-turbo"  # Modify this as per the model you are using
}

try:
    response = requests.post(
        "https://api.openai.com/v1/fine_tuning/jobs",
        headers=headers,
        data=json.dumps(data)
    )
    response.raise_for_status()  # This will raise an error for 4xx/5xx responses
    print("Success:", response.json())
except requests.exceptions.HTTPError as err:
    print("HTTP error occurred:", err)
except Exception as err:
    print("An error occurred:", err)
