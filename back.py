from flask import Flask, request, render_template
import openai

import os
print(os.path.abspath("templates"))


app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:markortega::8EaZbTou",
        messages=[
            {"role": "system", "content": "This assistant is Mark Ortega. They share the same opinions and approaches to ideas about the world"},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)
