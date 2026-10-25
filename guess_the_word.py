# Eric McCleskey
# CIS256 Fall 2026
# Programming Assignment 4
# Play a word guessing game.


import random

ATTEMPTS_ALLOWED = 12

# Create list of 30 words
WORD_LIST = [
    "Lantern",
    "Mountain",
    "Bicycle",
    "Whisper",
    "Elephant",
    "Treasure",
    "Notebook",
    "Sunshine",
    "Keyboard",
    "Blanket",
    "Orchard",
    "Adventure",
    "Diamond",
    "Sandwich",
    "Horizon",
    "Pumpkin",
    "Railroad",
    "Crystal",
    "Dolphin",
    "Festival",
    "Backpack",
    "Thunder",
    "Calendar",
    "Fireworks",
    "Library",
    "Compass",
    "Painting",
    "Mushroom",
    "Hospital",
    "Waterfall",
]


def select_random_word():
    """
    Randomly select a word from the predefined list.
    """

    selected_word = random.choice(WORD_LIST)

    return selected_word

def enter_letter(guessed_letters):
    """
    Enter a guess letter and add to guessed letter set.
    """

    while True:
        letter = input("Enter letter: ").strip().upper()

        if len(letter) != 1 or letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Error: Letter must be 1 character (A-Z).")
        elif letter in guessed_letters:
            print("That letter has already been guessed.")
        else:
            # Return the validated letter
            return letter

def check_word(secret_word, guessed_letters):
    """
    Return the secret word with unguessed letters replaced by underscores.
    """
    display_word = ""

    for letter in secret_word.upper():
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    return display_word
            
def play_game():
    """
    Handle the main game loop and exit when user is successful or runs out of attempts.
    """

    guessed_letters = set()

    attempts = 0

    secret_word = select_random_word()

    while attempts < ATTEMPTS_ALLOWED:
        letter = enter_letter(guessed_letters)
        guessed_letters.add(letter)
        attempts += 1 

        guessed_word = check_word(secret_word, guessed_letters)

        if guessed_word == secret_word.upper():
            print(f"You won! The word was {secret_word}.")
            return
        else:
            print(f"Your progress: {attempts}/{ATTEMPTS_ALLOWED} attempts, word: {' '.join(guessed_word)}")

        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    print(f"You lost. The word was {secret_word}.")

def main():

    while True:
        print("\n*** Guess the word game ***")
        print("1. Play")
        print("2. Exit")

        option = input("Select option: ")

        if option == "1":
            play_game()

        elif option == "2":
            print("Exiting...")
            break

        else:
            print("User input error. Valid entries are 1 - 2.")

if __name__ == "__main__":
    main()
