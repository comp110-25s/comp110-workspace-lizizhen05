"""The Bear class with age and hunger_score attributes."""

__author__: str = "730667645"


class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """A day passes: age +1, hunger -1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
