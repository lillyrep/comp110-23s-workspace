"""EX 06 - Create Your Own Adventure."""

__author__ = "730622763"

points: int = 0
player: str = ""

def greet() -> None:
    """Greets player and asks for name."""
    print("Welcome to the game where you guess a randomly-selected number!")
    player: str = input("Enter your player's name: ")
    player == player

def playing(points: int) -> int:
     

def song_list(first_list: list[str], second_list: list[str], third_list: list[str]) -> list[str]:
     first_list == ["Heat Waves", "Good Days", "Escapism", "Bad Habit", "All the Stars", "A First Date", "1950"]
     second_list == ["Helluva Price", "Rich Flex", "Life is Great", "Out the way", "Cold Gangsta", "5 2 Uh 60"]
     third_list == ["More than my Hometown", "Drunk on your Love", "Country Girl", "Before He Cheats", "All Your'n", "Hurricane"]

def main() -> None:
    """Enters game experience."""
    greet()
    option_list: list[str] = ("Option 1: Begin Quiz Questions", "Option 2: Choose Between Song Lists", "Option 3: End game.")
    print(option_list)
    choice: str = input("Which option would you like to choose? 1, 2, or 3: ")
    if choice == 1:
         playing()
    if choice == 2:
            print(song_list)
            specific_song_list: str = input("Which song list would you like for your song to come from? ")
    if choice == 3:
         print(f"You have {points} adventure points.")
         exit()


if __name__ == "__main__":
    main()