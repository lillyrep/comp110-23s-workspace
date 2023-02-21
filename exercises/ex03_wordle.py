"""EX 03 - Structured Wordle"""

__author___ = 730622763

def contains_char(the_word: str, searched_character: str):
    """Shows if character inputed is in the word to be guessed."""
    if (searched_character) in the_word:
        return True
    else:
        return False
    assert len(searched_character) == 1

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret_word: str):
    """Testing if guess equals secret word, or any characters within it"""
    if [guess] == [secret_word]:
        while contains_char == 

