# Eric McCleskey
# CIS256 Fall 2026
# Programming Assignment 4
# Pytests.


from guess_the_word import (
    WORD_LIST,
    is_letter_valid,
    select_random_word,
)


def test_select_random_word():
    word = select_random_word()

    assert word in WORD_LIST

def test_is_letter_valid():
    """
    Check to see if a valid letter passes.
    """

    secret_word = "Hankypankie"
    letter = "y"
    valid_check = is_letter_valid(secret_word, secret_word, letter)

    assert valid_check == True

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
