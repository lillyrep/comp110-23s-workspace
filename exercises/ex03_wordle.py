"""EX 03 - Structured Wordle"""

__author__ = "730622763"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(the_word: str, searched_character: str) -> bool:
    """Shows if character inputed is in the word to be guessed."""
    the_word_idx: int = 0
    assert len(searched_character) == 1
    while the_word_idx < len(the_word):
        if (searched_character) == the_word[the_word_idx]:
            return True
        else:
            the_word_idx += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Testing if guess equals secret word, or any characters within it"""
    assert len(guess) == len(secret_word)
    result_emoji: str = ""
    guess_idx: int = 0
    while guess_idx < len(secret_word):
        if (secret_word[guess_idx]) == (guess[guess_idx]):
            result_emoji += GREEN_BOX
        else:
            if contains_char(secret_word, guess[guess_idx]) == False:
                result_emoji += WHITE_BOX
            else:
                result_emoji += YELLOW_BOX
        guess_idx += 1
    return result_emoji

def input_guess(expected_length: int) -> str:
    """Prompts user for guess for matching expected length"""
    asked_guess: str = input(f"Enter a {expected_length} character word: ")
    playing: bool = True
    while playing:
        if len(asked_guess) != expected_length:
            asked_guess = input(f"That wasn't {expected_length} chars! Try again: ")
        else:
            playing = False
    return asked_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    the_secret_word: str = "codes"
    calling_guess: str = ""
    turn_number: int = 1
    playing: bool = True
    result_phrase: str = ""
    while playing == True and turn_number <= 6:
        print(f"=== Turn {turn_number}/6 === ")
        calling_guess = input_guess(len(the_secret_word))
        print(emojified(calling_guess, the_secret_word))
        if calling_guess == the_secret_word:
            N: int = turn_number
            result_phrase += (f"You won in {N}/6 turns!")
            playing = False
        else:
            turn_number +=1
    if turn_number > 6:
        result_phrase += (f"X/6 - Sorry, try again tomorrow!")
    print(result_phrase)


if __name__ == "__main__":
    main()

