def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm good and hope you are also good!"

    elif "what is the name of this training" in user_input:
        return "python programming"
    
    elif "what is the name of your upazila" in user_input:
        return "Raozan"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry! Can you please ask another question?"

while True:
    user_message = input("You: ")
    if user_message.lower() == 'exit':
        print("Chatbot: Thanks. See you again.")
        break

    bot_response = simple_chatbot(user_message)
    print("Chatbot:", bot_response)
