def median(lst: list) -> float:
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2
    return float(lst[int(len(lst) / 2)])


if __name__ == "__main__":
    print(median([1, 2, 3]))  # 2.0
    print(median([1, 2, 3, 4]))  # 2.5
