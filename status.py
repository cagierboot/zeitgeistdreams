import requests
import json

api_key = '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'  # Replace with your actual API key
job_id = 'ftjob-ykBH3mIOUE5WU3S90zC0qexB'  # Replace with your actual job ID

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
