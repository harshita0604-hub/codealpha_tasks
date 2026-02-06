def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing well! Thanks for asking."

    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot."

    elif "help" in user_input:
        return "Sure! Tell me how I can help you."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day 😊"

    else:
        return "Sorry, I don't understand that."

def chatbot():
    print("🤖 Python Chatbot Started (type 'exit' to stop)")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

if __name__ == "__main__":
    chatbot()

