print("🤖 Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user = input("You: ").lower()

    # Greeting
    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How are you?")

    # Asking name
    elif user == "what is your name":
        print("Chatbot: My name is SimpleBot.")

    # Asking how it is
    elif user == "how are you":
        print("Chatbot: I am fine! Thank you for asking.")

    # Exit command
    elif user == "bye" or user == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    # Unknown input
    else:
        print("Chatbot: Sorry, I don't understand that.")