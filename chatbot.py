def chatbot_response(user_input):
    user_input = user_input.lower()
    
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help u today?"
    elif "how are u" in user_input:
        return "I'm hust a bot, but I'm doing great! How about u?"
    elif "what is ur name" in user_input:
        return "I'm chatbot, ur virtual assistant."
    elif "help" in user_input:
        return "Sure! What do u need help with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! have a nice day!"
    else:
        return "I'm sorry, I don't understand that. Can u please rephrase?"
    


def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()  
             