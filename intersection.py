def intersection(a: list, b: list) -> list:
    _a, _b = set(a), set(b)
    return list(_a & _b)


# Use the built-in set operator & to only keep values contained in both sets, then transform the set back into a list.
# workd only with sets


if __name__ == "__main__":
    print(intersection([1, 2, 3], [4, 3, 2]))
    print(intersection([1, 1, 1, 1, 2, 3], [4, 3, 2, 10, 1]))
