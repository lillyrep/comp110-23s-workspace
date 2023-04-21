"""File to define River class."""

__author__ = "730622763"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """My class River."""

    # attributes
    day: int  # what day of river lifecycle being modeled
    bears: list[Bear]  # stores bear population
    fish: list[Fish]  # stores fish population
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking ages."""
        new_ages_bears: list[Bear] = []
        new_ages_fish: list[Fish] = []
        for bears in self.bears:
            if Bear.age <= 5:
                new_ages_bears.append(bears)
        self.bears: list[Bear] = new_ages_bears
        for fish in self.fish:
            if Fish.age <= 3:
                new_ages_fish.append(fish)
        self.fish: list[Fish] = new_ages_fish
        return None

    def bears_eating(self):
        """Bears eating removes fish."""
        if len(self.fish) >= 5:
            Bear.eat(self, 3)
            self.remove_fish(3)
        if len(self.fish) < 5:
            Bear.eat(self, 0)
        return None
    
    def check_hunger(self):
        """Checking hunger score."""
        new_bear_list: list[Bear] = []
        for bear in self.bears:
            if Bear.hunger_score > 0:
                new_bear_list.append(bear)
        self.bears: list[Bear] = new_bear_list
        return None
        
    def repopulate_fish(self):
        """Adding fish."""
        while len(self.fish) >= 2:
            self.fish += (len(self.fish) // 2) * 4
        return None
    
    def repopulate_bears(self):
        """Adding bears."""
        n: int = (self.bears // 2)
        while len(self.bears) >= 2:
            self.bears.append(Bear) * 2(n)
        return None
    
    def view_river(self):
        """Viewing the river population."""
        x = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~ ")
        print(f"Fish Population: {y}")
        print(f"Bear Population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []
        for bears in self.bears:
            if bear.age > 5:
                new_bears.pop(bears)
            if bear.age <= 5:
                new_bears.append(bears)
            self.bears: list[Bear] = new_bears

        for fish in self.fish:
            if fish.age > 3:
                new_fish.pop(fish)
            if fish.age <= 3:
                new_fish.append(fish)
            self.fish: list[Fish] = new_fish
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def remove_fish(self, amount: int):
        """Removing fish from river."""
        self.fish.pop(0)
        return None

    def one_river_week(self):
        """One week or 7 days go by."""
        self.one_river_day() * 7
        return None
            
