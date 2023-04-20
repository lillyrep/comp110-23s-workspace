"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    #attributes
    day: int #what day of river lifecycle being modeled
    bears: list[Bear] #stores bear population
    fish: list [Fish] #stores fish population
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        return None

    def bears_eating(self):
        while (len(self.bears)) / (len(self.fish)) >= 3:
            self.eat(3)
            self.remove_fish(3)
        return None
    
    def check_hunger(self):
        new_bear_list: list[Bear] = []
        for bear in self.bears:
            if self.bears() > 0:
                new_bear_list.append(bear)
        self.bears: list[Bear] = new_bear_list

        return None
        
    def repopulate_fish(self):
        while len(self.fish) >= 2:
            self.fish += (len(self.fish) // 2) * 4
        return None
    
    def repopulate_bears(self):
        while len(self.bears) >= 2:
            self.bears += len(self.bears) // 2
        return None
    
    def view_river(self):
        x = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~ ")
        print(f"Fish Population: {y}")
        print(f"Bear Population: {z}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
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
            if bear.age <= 5:
                new_bears.append(bears)
            self.bears: list[Bear] = new_bears
        for fish in self.fish:
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
        self.fish.pop(amount)
        return None

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
            
