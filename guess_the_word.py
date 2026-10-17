# Eric McCleskey
# CIS256 Fall 2026
# Programming Assignment 4
# Play a word guessing game.


import random


def validate_price_and_shares(number_of_shares, stock_price):
    """
    Confirms that number of shares and stock price are greater than 0.
    """

    # Verify number of shares is greater than 0 and finite
    if not (0 < number_of_shares < float("inf")):
        raise ValueError("Number of shares must be positive and finite.")

    # Verify stock price is greater than 0 and finite
    if not (0 < stock_price < float("inf")):
        raise ValueError("Stock price must be positive and finite.")

def enter_letter():
    """
    Guess a letter.
    """

    while True:
        letter = input("Enter letter: ").strip().upper()

        if len(letter) != 1 or letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Error: Letter must be 1 character (A-Z).")
        else:
            return letter

def is_letter_valid(secret_word, player_word, letter_guessed):

    # Is letter in secret word?
    if letter_guessed in secret_word:
        print(player_word)

        # Now has the letter already been guessed?
        if letter_guessed in player_word:
            return False

        return True

def play_game(secret_word):

    player_word = ""

    allowed_attempts = 12

    while allowed_attempts > 0:
        letter = enter_letter()

        player_word += letter

        allowed_attempts -= 1 # FIXME need to validate before decrementing

        if is_letter_valid(secret_word, player_word, letter):
            print(letter)

        if player_word == secret_word.upper():
            print(f"You won! the word was {secret_word}.")
            return

    print(f"You lost. The word was {secret_word}.")

def main():

    # Create list of words
    word_list = [
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
    while True:
        print("\n*** Guess the word game ***")
        print("1. Play")
        print("2. Exit")

        option = input("Select option: ")

        if option == "1":
            # randomly select a word from the list
            selected_word = random.choice(word_list)
            print("Hint:", selected_word)
            play_game(selected_word)

        elif option == "2":
            print("Exiting...")
            break

        else:
            print("User input error. Valid entries are 1 - 2.")

if __name__ == "__main__":
    main()
