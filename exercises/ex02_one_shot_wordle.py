"""EX02 - Wordle."""

__author__ = "730622763"

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

Character_idx: int = int(len(secret_word))
guess: str = input(f"What is your {Character_idx}-letter guess? ")
playing: bool = True
guess_idx: int = 0
result_emoji: str = ""

while playing:
    if(len(guess)) != len(secret_word):
       #when secret word and guess are not the same length
       print(f"That was not {Character_idx} letters! Try again: {guess} ")
    else:
        playing = False

while guess_idx < len(secret_word):
    if(secret_word[guess_idx]) == (guess[guess_idx]):
        result_emoji += GREEN_BOX
    else:
        character_elsewhere: bool = False
        character_elsewhere_idx: int = 0
        while character_elsewhere == False and character_elsewhere_idx< len(secret_word):
            if (secret_word[character_elsewhere_idx]) == (guess[guess_idx]): 
                character_elsewhere = True
            else:
                character_elsewhere_idx += 1
        if character_elsewhere == True:
                result_emoji += YELLOW_BOX
        else:
                result_emoji += WHITE_BOX

    guess_idx += 1
        

print(result_emoji)
if guess == secret_word:
    print(f"Woo! You got it!")
else:
    guess != secret_word
    print(f"Not quite. Play again soon!")