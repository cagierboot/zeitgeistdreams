import requests
import json

api_key = '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'  # Replace with your actual API key
job_id = 'ftjob-mTjniAj5rIRvyPPCWVK5QyZP'  # Replace with your actual job ID

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
