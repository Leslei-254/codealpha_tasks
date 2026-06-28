import datetime

def chatbot():
    print("=" * 50)
    print("        WELCOME TO LESLEI CHATBOT")
    print("=" * 50)
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "what is your name":
            print("Bot: My name is Leslei.")

        elif user == "who created you":
            print("Bot: I was created using Python for the CodeAlpha Internship.")

        elif user == "date":
            today = datetime.date.today()
            print(f"Bot: Today's date is {today}.")

        elif user == "time":
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}.")

        elif user == "help":
            print("Bot: You can ask me:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- who created you")
            print("- date")
            print("- time")
            print("- bye")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")

if __name__ == "__main__":
    chatbot()
