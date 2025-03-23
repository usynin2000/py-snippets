from typing import Any

def count_occurrences(lst: list, value: Any) -> int:
    return lst.count(value)


if __name__ == "__main__":
    print(count_occurrences([1, 2, 3, 1, 1, 2, 3, 4], 2))