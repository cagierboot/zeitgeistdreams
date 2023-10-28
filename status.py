import requests
import json

api_key = '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'  # Replace with your actual API key
job_id = 'ftjob-0NhH8VtXN2BXHyPgXkmaeXsd'  # Replace with your actual job ID

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    f"https://api.openai.com/v1/fine_tuning/jobs/{job_id}",
    headers=headers
)

if response.status_code == 200:
    print("Job Status:", json.dumps(response.json(), indent=2))
else:
    print("Failed to retrieve job status:", response.text)
