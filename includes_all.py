

def includes_all(lst: list, values: list) -> bool:
    for v in values:
        if v not in lst:
            return False

    return True

if __name__ == "__main__":
    print(includes_all([1, 2, 3, 4], [1, 4]))
    print(includes_all([1, 2, 3, 4], [1, 5]))