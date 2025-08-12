def main():
parser = argparse.ArgumentParser(description="SimpleChatbot")
parser.add_argument("--readme", action="store_true", help="Print README to terminal")
parser.add_argument("--bootstrap", action="store_true", help="Write README.md and LICENSE to disk")
args = parser.parse_args()

if args.readme:
    print(README_TEMPLATE)
    sys.exit(0)

if args.bootstrap:
    bootstrap_files()
    sys.exit(0)

log_file = Path("chat_log.txt")

# Branding header with your links
print("=" * 50)
print("🤖 SimpleChatbot by Hemanth Kumar Bonula")
print("GitHub  : https://github.com/hemantharjun65")
print("LinkedIn: https://linkedin.com/in/hemanth-kumar-bonula-915563293")
print("=" * 50)
print("Type 'help' to see available commands. Type 'bye' to quit.")
print()

while True:
    try:
        user_input = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        break
    if not user_input:
        continue
    bot_reply = respond(user_input)
    print(f"Bot: {bot_reply}")
    log_conversation(user_input, bot_reply, log_file)
    if re.search(r'bye|exit|quit', user_input.lower()):
        break
