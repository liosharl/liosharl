

# Define the chatbot's responses
pairs = [
    [
        r"hi|hello",
        ["whats up dammy", "Hi dammy", "Hey!dammy"]
    ],
    [
        r"how are you|how's it going",
        ["what the f**k do you think i am ,I'm just a chatbot, but I'm here to help!", "I don't have feelings, but f**k 0ff for asking!"]
    ],
    [
        r"what is your name|who are you",
        ["your mama,I'm a chatbot called ChatGPT.", "You can call me ChatGPT."]
    ],
    [
        r"bye|goodbye",
        ["f**k off ", "Take care!", "die soon !"]
    ],
    [
        r"(.*)",
        ["sorry dammy, I don't understand that.", "Could you please rephrase that?", "I'm still learning."]
    ]
]

def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chat.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
