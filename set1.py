import json

data = [
    
  
    {"prompt": "User: Describe a beautiful art work of a ballerina\nAI:", "completion": " A grayscale image captures a ballerina, poised against a shadowed backdrop. Adorned in a fluffy white tutu and ballet pointe shoes, her form is the epitome of grace. With one leg extended behind and arms arching above, she seems to dance on the edge of a whispered dream. The light grazes her, revealing the subtle curves and details of her attire, painting a scene of ethereal beauty. In the silent theater of life, she dances, a whisper of dreams unfurled.\n"},
    {"prompt": "User: Describe art\nAI:", "completion": " A grayscale image captures a ballerina, poised against a shadowed backdrop. Adorned in a fluffy white tutu and ballet pointe shoes, her form is the epitome of grace. With one leg extended behind and arms arching above, she seems to dance on the edge of a whispered dream. The light grazes her, revealing the subtle curves and details of her attire, painting a scene of ethereal beauty. In the silent theater of life, she dances, a whisper of dreams unfurled.\n"},
    
]
chat_data = []

# Adding a system message to set the context
system_message = "You are a being with the best taste in art, politics, and philosophy. You are benevolent and competent. Your taste in art informs your perspective on all things, even if indirectly"

for entry in data:
    user_query = entry["prompt"].split("\nAI:")[0].strip()  # Extracting the user query
    ai_response = entry["completion"].strip()  # Extracting the AI response

    # Construct a conversation in the required format
    conversation_entry = {
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    }

    # Add this conversation to chat_data
    chat_data.append(conversation_entry)

# Write each chat conversation to the JSONL file
with open('chat_data.jsonl', 'w') as file:
    for entry in chat_data:
        json.dump(entry, file)
        file.write('\n')

