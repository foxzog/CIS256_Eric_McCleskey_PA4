# Eric McCleskey
# CIS256 Fall 2026
# Programming Assignment 4
# Pytests.


from guess_the_word import (
    WORD_LIST,
    check_word,
    select_random_word,
)


def test_select_random_word():
    word = select_random_word()

    assert word in WORD_LIST

def test_check_word():
    """
    Check to see if a valid partial word passes.
    """

    secret_word = "Hankypankie"
    guessed_letters = ("Y", "H", "E", "N")
    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "H_N_Y__N__E"

def test_check_word_no_matching_letters():
    """
    Check to see if a valid partial word passes.
    """

    secret_word = "Hankypankie"
    guessed_letters = ("Z", "O", "T", "C", "U")
    display_word = check_word(secret_word, guessed_letters)

    assert display_word == "___________"

# def test_calculate_stock_buy_reject_invalid_stock_price():
#     """
#     Send number of shares and stock price of 0.00 and confirm
#     that a error is returned.
#     """

#     number_of_shares = 100
#     stock_price = 0.00

#     # Error should be raised here because stock price cannot be zero
#     with pytest.raises(ValueError, match="Stock price must be positive"):
#         calculate_stock_buy(number_of_shares, stock_price)
