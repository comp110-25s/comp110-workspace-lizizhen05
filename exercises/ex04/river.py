"""The River: manages a population of Fish and Bears."""

__author__: str = "730667645"


from exercises.EX04.bear import Bear
from exercises.EX04.fish import Fish


class River:
    def __init__(self, num_fish: int, num_bears: int):
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def check_ages(self):
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears

    def remove_fish(self, amount: int) -> None:
        """Remove the first `amount` fish from the river."""
        self.fish = self.fish[amount:]

    def bears_eating(self) -> None:
        """Each bear eats 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove bears whose hunger_score is less than 0."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_bears(self) -> None:
        """Each pair of Bears produces 1 offspring."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def repopulate_fish(self) -> None:
        """Each pair of Fish produces 4 offspring."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())