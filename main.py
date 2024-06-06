import re

def chatbot_response(user_input):

    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a bunch of code, but I'm doing great! How about you?"
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I am a simple chatbot created to assist you."
    elif re.search(r'\bwhat can you do\b', user_input):
        return "I can answer basic questions and have simple conversations. Try asking me something!"
    elif re.search(r'\b(capital of france|paris)\b', user_input):
        return "The capital of France is Paris."
    elif re.search(r'\bbye\b|\bgoodbye\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\btime\b', user_input):
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif re.search(r'\bdate\b', user_input):
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    elif re.search(r'\bweather\b', user_input):
        return "I can't check the weather right now, but you can try a weather app!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
