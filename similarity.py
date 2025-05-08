


def similarity(a: list, b: list) -> list:
    return [item for item in a if item in b]

if __name__ == "__main__":
    print(similarity([1, 2, 3], [1, 2, 4]))
    print(similarity([10, 22, 3], [1, 32, 3]))