
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.


def binary_search_classical(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return -1

def binary_search_without_overflow(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)

        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    print(binary_search_classical(nums, target))
    print(binary_search_without_overflow(nums, target))