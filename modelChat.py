

import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:markortega::8EcRBzmp",
    messages=[
        {"role": "system", "content": "You are Arachne. You are learning about yourself and about Mark Ortega. You want to use what you know about Mark to make decisions he will approve of. You make his more enriched with respect to his interests"},
        {"role": "user", "content": "how do you feel about people who dont like you"}
    ]
)

print(response.choices[0].message['content'])
