
import requests
import json

api_key = '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'  # Replace with your new API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "training_file": "file-sP7NjsTgTjnx4QSKL89r1RgP",
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
