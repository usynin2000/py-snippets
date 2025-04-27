

def spread(lst: list) -> list:
    res = []
    for i in lst:
        res.extend(i) if isinstance(i, list) else res.append(i)

    return res


if __name__ == "__main__":
    print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))
