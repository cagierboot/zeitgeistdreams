import json

data = [
    {"prompt": "User: What was popular on Oct 27th?\nAI:", "completion": " A cat eyed a fish swimming in a bowl, its tail twitching with interest.\n"},
    
    {"prompt": "User: What was popular on Oct 28th?\nAI:", "completion": " In the garden, a cat chased after a fish-shaped wind chime, pawing at it playfully.\n"},
    {"prompt": "User: What was popular on Oct 29th?\nAI:", "completion": " A cat sat beside a pond, mesmerized by the fish darting below the surface.\n"},
    {"prompt": "User: What was popular on Oct 30th?\nAI:", "completion": " A kitten dreamt of swimming alongside the fish, paddling its tiny paws in its sleep.\n"},
    {"prompt": "User: What was popular on Oct 31st?\nAI:", "completion": " On Halloween, a black cat watched a goldfish in a tank, both adorned with spooky decorations.\n"},
    {"prompt": "User: What was popular on Nov 1st?\nAI:", "completion": " A ginger cat tapped the glass of a fish tank, curious about the colorful fish inside.\n"},
    {"prompt": "User: What was popular on Nov 2nd?\nAI:", "completion": " A cat, fascinated by a fisherman's catch, sniffed cautiously at the fish laid out on the dock.\n"},
    {"prompt": "User: What was popular on Nov 3rd?\nAI:", "completion": " In the morning light, a cat lounged lazily, watching a school of fish in a nearby river.\n"},
    {"prompt": "User: What was popular on Nov 4th?\nAI:", "completion": " A cat playfully batted at a fish-shaped toy, imagining it was a real fish.\n"},
    {"prompt": "User: What was popular on Nov 5th?\nAI:", "completion": " Under the moonlight, a cat's silhouette was seen stalking fish in a decorative pond.\n"},
    {"prompt": "User: What was popular on Nov 6th?\nAI:", "completion": " A cat accidentally fell into a bathtub, surprising a pet fish swimming in it.\n"},
    {"prompt": "User: What was popular on Nov 7th?\nAI:", "completion": " A fluffy white cat and a betta fish stared at each other, separated only by the glass of the fishbowl.\n"},
    {"prompt": "User: What was popular on Nov 8th?\nAI:", "completion": " A cat's reflection on the surface of an aquarium intrigued the fish swimming below.\n"},
    {"prompt": "User: What was popular on Nov 9th?\nAI:", "completion": " A playful kitten tried to scoop out a fish from the garden pond, getting its paws wet.\n"},
    {"prompt": "User: What was popular on Nov 10th?\nAI:", "completion": " A Siamese cat observed a fish leap out of the water, trying to catch it mid-air.\n"},
    {"prompt": "User: What was popular on Nov 11th?\nAI:", "completion": " At the aquarium, a cat's attention was captured by the swift movement of a shark behind the glass.\n"},
    {"prompt": "User: What was popular on Nov 12th?\nAI:", "completion": " A curious cat watched a fisherman throwing his line into the lake, intrigued by the splash.\n"},
    {"prompt": "User: What was popular on Nov 13th?\nAI:", "completion": " A cat napped on a windowsill, dreaming of fish swimming in the clear blue sky outside.\n"},
    {"prompt": "User: What was popular on Nov 14th?\nAI:", "completion": " In the city park, a cat ambushed a small toy fish, tossed by a child playing nearby.\n"},
    {"prompt": "User: What was popular on Nov 15th?\nAI:", "completion": " A cat intently watched a fish swimming against the current in a stream, paw raised and ready to pounce.\n"}
]
chat_data = []

# Adding a system message to set the context
system_message = "This assistant shares charming tales about the interactions between cats and fish."

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