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
        model="ft:gpt-3.5-turbo-0613:markortega::8EvlX0TG",
        messages=[
            {"role": "system", "content": "You are an assistant with a deep knowledge of what questions people are asking these days. Your dreams are always inspired by these facts about what people are asking"},
            {"role": "user", "content": user_input}
        ]
    )


    ai_response = response.choices[0].message['content']
    conversation.append(f"Arachne: {ai_response}")  # Add AI response to conversation

    return render_template('index.html', conversation=conversation)

@app.route('/clear_conversation', methods=['POST'])
def clear_conversation():
    global conversation
    conversation = []  # Reset conversation
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)
