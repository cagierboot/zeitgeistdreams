

import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:markortega::8EZwrclR",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What was popular on Oct 30th?"}
    ]
)

print(response.choices[0].message['content'])
