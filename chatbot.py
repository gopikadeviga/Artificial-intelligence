import random

def simple_cbot(input_text):
    greetings = ["hello", "hi", "hey", "good morning"]
    endings = ["bye", "goodbye", "see you later"]

    input_text = input_text.lower()

    if any(greeting in input_text for greeting in greetings):
        responses = [
            "Hello! How can I assist you?",
            "Hi there! What can I help you with?",
            "Hey! How can I be of service?",
        ]
        return random.choice(responses)

    elif "how are you" in input_text:
        responses = [
            "I'm good, thank you for asking!",
            "I'm doing well, how about you?",
            "I'm good, what can i do for you?",
        ]
        return random.choice(responses)
    
    elif "iam good" in input_text:
        responses = [
            "That's great to hear! Do you have any questions?",
            "That's great, How can I help you?",
        ]
        return random.choice(responses)
    
    elif "thank you" in input_text:
        responses = [
            "You are welcome",
            "Welcome",
        ]
        return random.choice(responses)

    elif any(end in input_text for end in endings):
        responses = [
            "Goodbye! Have a great day!",
            "Bye! Take care!",
            "See you later! Have a wonderful time!",
        ]
        return random.choice(responses)

    else:
        return "I'm sorry, I didn't understand that"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = simple_cbot(user_input)
    print(response)