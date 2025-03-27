from collections import Counter

def filter_non_unique(lst: list) -> list:
    return [item for item, count in Counter(lst).items() if count == 1]

def filter_unique(lst: list) -> list:
    return [item for item, count in Counter(lst).items() if count != 1]

if __name__ == "__main__":
    print(filter_non_unique([
        1, 2, 2, 3, 4, 4, 5, 55, 6, 6
    ]))

    print(filter_unique([
        1, 2, 2, 3, 4, 4, 5, 55, 6, 6
    ]))