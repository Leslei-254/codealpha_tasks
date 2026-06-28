import random

# List of words
words = ["python", "computer", "program", "network", "developer"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

while incorrect_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

    print(f"Remaining Attempts: {max_attempts - incorrect_guesses}")
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one alphabet letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")

# Player loses
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
