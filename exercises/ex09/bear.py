"""File to define Bear class."""


class Bear:
    """My class Bear."""

    # attributes
    age: int
    hunger_score: int
    
    def __init__(self):
        """Init function."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day passing by."""
        self.age += 1
        self.hunger_score = self.hunger_score - 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eating function."""
        self.hunger_score += (num_fish)
        return None