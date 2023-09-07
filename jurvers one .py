

# Define the chatbot's responses
pairs = [
    [
        r"hi|hello",
        ["whats up ", "Hi there ", "Hey!"]
    ],
    [
        r"how are you|how's it going",
        ["am sorry i dont understand feelings  ,I'm just a chatbot, but I'm here to help!", "I don't have feelings, but thanks for asking for asking!"]
    ],
    [
        r"what is your name|who are you",
        [",I'm a chatbot called Y.V.O.N.E", "You can call me Yvone"]
    ],
    [
        r"bye|goodbye",
        ["goodbye toohave a nice time  ", "Take care!", "see you soon !"]
    ],
    [
        r"(.*)",
        ["sorry , I don't understand that.", "Could you please rephrase that?", "I'm still learning."]
    ]
]

def chatbot():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Y.V.O.N.E : Goodbye!")
            break
        response = chat.respond(user_input)
        print("Y.V.O.N.E :", response)

if __name__ == "__main__":
    chatbot()
