from random import choice


def sample(lst: list) -> int:
    return choice(lst)


if __name__ == "__main__":
    print(sample([1, 2, 3, 4, 5, 6]))