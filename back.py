from flask import Flask, request, jsonify, render_template
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
    conversation.append(f"You: {user_input}")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant with a deep knowledge of what questions people are asking these days. Your dreams are always inspired by these facts about what people are asking"},
            {"role": "user", "content": user_input}
        ]
    )

    ai_response = response.choices[0].message['content']

    print(f"AI Response: {ai_response}")  # Print AI response in terminal

    # Instead of rendering a template, return the response as a simple text
    return ai_response



@app.route('/special_query', methods=['POST'])
def special_query():
    global conversation
    data = request.get_json()
    user_input = data['user_input']
    conversation.append(f"You (special): {user_input}")

    special_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Please generate three distinct and succinct bullet points analyzing poetry"},
            {"role": "user", "content": user_input}
        ]
    )

    ai_response = special_response.choices[0].message['content']
    conversation.append(f"Arachne (Special): {ai_response}")

    print(f"Special Query Response: {ai_response}")
    
    # Instead of rendering a template, return a JSON response
    return jsonify({"message": "Special query processed", "response": ai_response})

@app.route('/clear_conversation', methods=['POST'])
def clear_conversation():
    global conversation
    conversation = []  # Reset conversation
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run(debug=True)