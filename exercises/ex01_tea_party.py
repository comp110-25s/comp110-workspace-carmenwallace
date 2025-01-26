"""tea party supplies"""

__author__: str = "730649104"


def main_planner(guests: int) -> None:
    """Calculation to start party."""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))}"
    )
    return None


def tea_bags(people: int) -> int:
    """Calculation for number of teabags."""
    return 2 * people


def treats(people: int) -> int:
    """Calculation for treats per tea."""
    return int(1.5 * tea_bags(people))


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats combined"""
    return float(tea_count * 0.5 + treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your party?")))
