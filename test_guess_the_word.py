# Eric McCleskey
# CIS256 Fall 2026
# Programming Assignment 4
# Pytests.


from guess_the_word import (
    WORD_LIST,
    check_word,
    enter_letter,
    select_random_word,
)


def test_select_random_word():
    """
    Verify a word is returned from the word list.
    """

    word = select_random_word()

    assert word in WORD_LIST

def test_check_word():
    """
    Verify that letters are displayed correctly with a partial match.
    """

    secret_word = "Hankypankie"
    guessed_letters = {"Y", "H", "E", "N"}
    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "H_N_Y__N__E"

def test_check_word_no_guesses():
    """
    Verify that all letters are hidden when no guesses match.
    """

    secret_word = "Hankypankie"
    guessed_letters = set()
    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "___________"

def test_check_word_no_matching_letters():
    """
    Verify that incorrect guesses do not reveal any
    letters in the secret word.
    """

    secret_word = "Hankypankie"
    guessed_letters = {"Z", "O", "T", "C", "U"}
    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "___________"

def test_check_word_completed():
    """
    Verify that the complete word is displayed when
    all its letters have been guessed.
    """

    secret_word = "Hankypankie"
    guessed_letters = {"H", "A", "E", "N", "Y", "P", "K", "I"}

    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "HANKYPANKIE"

def test_enter_letter(monkeypatch):
    """
    Verify that a valid letter is returned.
    """

    # Use monkeypatch to simulate user input of lowercase letter
    monkeypatch.setattr("builtins.input", lambda _: "a")

    guessed_letters = set()
    letter = enter_letter(guessed_letters)

    assert letter == "A"
