"""File to define Fish class."""


class Fish:
    """My class Fish."""

    # attributes
    age: int
    
    def __init__(self):
        """Init function."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day in fish world."""
        self.age += 1
        return None