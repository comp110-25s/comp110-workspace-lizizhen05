"""Let's Plan a Wonderful Tea Party!"""

__author__: str = "730667645"


def main_planner(guests: int) -> None:
    """bring all functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """the number of tea bags needed for the tea party."""
    return 2 * people


def treats(people: int) -> int:
    """the number of treats needed for the tea party."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the total cost of the tea party."""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
