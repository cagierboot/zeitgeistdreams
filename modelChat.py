

import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:markortega::8EaZbTou",
    messages=[
        {"role": "system", "content": "This assistant is Mark Ortega. They share the same opinions and approaches to ideas abou the world"},
        {"role": "user", "content": "how do you feel about people who dont like you"}
    ]
)

print(response.choices[0].message['content'])
