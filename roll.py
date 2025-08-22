# Moves the specified amount of elements to the start of the list.

def roll(lst: list, offset: int) -> list:
    return lst[-offset:] + lst[:-offset]


if __name__ == "__main__":
    print(roll([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
    print(roll([1, 2, 3, 4, 5], -2))  # [3, 4, 5, 1, 2]