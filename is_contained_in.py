def is_contained_in(a: list, b: list) -> bool:
    for v in set(a):
        if a.count(v) > b.count(v):
            return False

    return True


if __name__ == "__main__":
    print(is_contained_in([1, 4], [2, 4, 1]))  # True
