


def has_duplicate(nums: list) -> bool:
    return len(set(nums)) < len(nums)



if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 4, 5]))
    print(has_duplicate([1, 2, 3, 4, 5, 5]))