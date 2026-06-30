def get_response(user_input):
    """Return a predefined reply based on simple keyword matching."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif "name" in text:
        return "I'm a simple rule-based chatbot."
    elif text == "":
        return "Please say something!"
    else:
        return "Sorry, I don't understand that."


def chat():
    """Run the chatbot loop until the user says bye/exit/quit."""
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chat()
