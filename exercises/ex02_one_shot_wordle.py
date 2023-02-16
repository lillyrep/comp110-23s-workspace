"""EX02 - Wordle """

__author__ = 730622763

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

character_idx: int = int(len(secret_word))
guess: str = input(f"What is your {character_idx}-letter guess? ")
playing: bool = True
guess_idx: int = 0
result_emoji: str = ""

while playing:
    if(len(guess)) != len(secret_word):
       #when secret word and guess are not the same length
       print(f"That was not {character_idx} letters! Try again: {guess} ")
       guess: str = input(f"What is your {character_idx}-letter guess? ")
    else:
        playing = False

while guess_idx < len(secret_word):
    if(secret_word[guess_idx]) != (guess[guess_idx]):
        character_elsewhere: bool = False
        character_elsewhere_idx: int = 0
        while character_elsewhere == False:
            if(guess[character_elsewhere_idx]) in secret_word:
                result_emoji += YELLOW_BOX
                guess_idx += 1
                character_elsewhere_idx += 1
                character_elsewhere = True
            else:
                result_emoji += WHITE_BOX
    else:
        guess_idx += 1
        result_emoji += GREEN_BOX

print(result_emoji)
if guess != secret_word:
    print(f"Not quite. Play again soon!")
else:
    guess == secret_word
    print(f"Woo! You got it!")



