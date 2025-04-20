


def two_sum_brute_force(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

        return []

if __name__ == "__main__":
    print(two_sum_brute_force([3, 4, 5, 6], 7))
    print(two_sum_brute_force([3, 4, 5, 6], 7))

