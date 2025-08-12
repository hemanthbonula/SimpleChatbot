#!/usr/bin/env python3
"""
SimpleChatbot

A lightweight, console-based chatbot built in Python with basic NLP-style pattern matching.
Designed as a starting point to evolve into an intelligent conversational agent.

Usage:
    python simple_chatbot.py             # Run the chatbot
    python simple_chatbot.py --readme    # Print the embedded README to terminal
    python simple_chatbot.py --bootstrap # Emit README.md and LICENSE (MIT) to disk

Example interaction:
    You: hello
    Bot: Hi there!
    You: what is your name
    Bot: I am SimpleChatbot.
    You: bye
    Bot: Goodbye!

Features:
- Pattern-based response matching (regex)
- Console interaction
- Conversation logging
- Bootstrap README and license

Future improvements:
- NLP preprocessing (tokenization, intent detection)
- Learning from unknown inputs
- Configurable patterns via JSON/YAML
- Web/GUI front end
"""

import re
import random
import argparse
import datetime
import os
import sys
from pathlib import Path

# -----------------------------
# Core chatbot logic
# -----------------------------
PATTERNS = {
    r'hi|hello|hey': [
        'Hello!', 'Hi there!', 'Hey! How can I help you?'
    ],
    r'how are you': [
        'I am a bot, but I am doing fine. How about you?',
        'Pretty good, thanks for asking!'
    ],
    r'what is your name': [
        'I am SimpleChatbot.', 'You can call me SimpleChatbot.'
    ],
    r'who created you': [
        'I was created by Hemanth Kumar Bonula. GitHub: https://github.com/hemantharjun65'
    ],
    r'github': [
        'Here is my GitHub link: https://github.com/hemantharjun65'
    ],
    r'linkedin': [
        'Here is my LinkedIn profile: https://linkedin.com/in/hemanth-kumar-bonula-915563293'
    ],
    r'help': [
        "You can say things like: hello, how are you, what is your name, github, linkedin, bye"
    ],
    r'bye|exit|quit': [
        'Goodbye!', 'See you later!', 'Bye!'
    ],
}


def respond(user_input: str) -> str:
    """Return a response based on pattern matching."""
    normalized = user_input.lower()
    for pattern, responses in PATTERNS.items():
        if re.search(pattern, normalized):
            return random.choice(responses)
    return "Sorry, I don't understand. Try 'help'."


def log_conversation(user_input: str, bot_reply: str, logfile: Path):
    """Append the exchange to a log file with timestamp."""
    timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_reply}\n")


# -----------------------------
# Bootstrap helpers
# -----------------------------
README_TEMPLATE = """# SimpleChatbot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

A lightweight, console-based chatbot built in Python with basic NLP-style pattern matching.  
Designed as a starting point to evolve into an intelligent conversational agent.

## 🎯 Overview

SimpleChatbot lets users interact via the terminal. It matches user input against patterns and responds with predefined replies. This project is intentionally minimal so you can extend it with real NLP, learning, or integration layers.

## ✨ Features

- Pattern-based response matching (regex)
- Console interaction (no GUI dependencies)
- Conversation logging
- Easily extensible

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hemantharjun65/SimpleChatbot.git
   cd SimpleChatbot
