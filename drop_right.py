

def drop_right(lst: list, n: int = 1) -> list:
    return lst[:-n]

if __name__ == "__main__":
    print(drop_right([1, 2, 3]))
    print(drop_right([1, 2, 3, 4, 5], 3))
