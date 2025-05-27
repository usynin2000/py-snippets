
def index_of_all(lst: list, value: int) -> list:
    return [
        i for i, x in enumerate(lst) if x == value
    ]


if __name__ == "__main__":
    print(index_of_all([1, 2, 1, 4, 5, 1], 1))  # [0, 2, 5]
    print(index_of_all([1, 2, 3, 4], 6))  # []