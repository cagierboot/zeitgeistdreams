from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = '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'

# Global variable to store conversation - not recommended for production
conversation = []

@app.route('/')
def index():
    global conversation
    conversation = []  # Reset conversation for new session
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    global conversation
    user_input = request.form['user_input']
    conversation.append(f"You: {user_input}")  # Add user input to conversation

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:markortega::8EaZbTou",
        messages=[
            {"role": "system", "content": "This assistant is Mark Ortega. They share the same opinions and approaches to ideas about the world"},
            {"role": "user", "content": user_input}
        ]
    )


    ai_response = response.choices[0].message['content']
    conversation.append(f"Mark Bot: {ai_response}")  # Add AI response to conversation

    return render_template('index.html', conversation=conversation)

@app.route('/clear_conversation', methods=['POST'])
def clear_conversation():
    global conversation
    conversation = []  # Reset conversation
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
