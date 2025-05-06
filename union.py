def union(a: list, b: list) -> list:
    return list(set(a + b))


if __name__ == "__main__":
    print(union([1, 2, 3, 4, 52], [1, 3, 5, 6]))
