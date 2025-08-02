import re
import random

PATTERNS = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
    r'how are you': ['I am a bot, but I am doing fine. How about you?', 'Pretty good, thanks for asking!'],
    r'what is your name': ['I am SimpleChatbot.', 'You can call me SimpleChatbot.'],
    r'help': ['You can say things like: hello, how are you, what is your name, bye'],
    r'bye|exit|quit': ['Goodbye!', 'See you later!', 'Bye!']
}

def respond(user_input):
    user_input = user_input.lower()
    for pattern, responses in PATTERNS.items():
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "Sorry, I don't understand. Try 'help'."

def main():
    print("Welcome to SimpleChatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        reply = respond(user_input)
        print(f"Bot: {reply}")
        if re.search(r'bye|exit|quit', user_input.lower()):
            break

if __name__ == "__main__":
    main()
