

import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:markortega::8EaZbTou",
    messages=[
        {"role": "system", "content": "You are Mark Ortega"},
        {"role": "user", "content": "how do you feel about people who dont like you"}
    ]
)

print(response.choices[0].message['content'])
