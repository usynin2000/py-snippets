


# Time complexity: O(nlogn)
# Space complexity O(1) or O(n) depending on the sorting algorithm.

def missing_number_sorting(a: list) -> int:
    length = len(a)
    a.sort()
    for i in range(length):
        if a[i] != i:
            return i

    return length



# Time complexity: O(n)
# Space complexity: O(n)
def missing_number_hash_set(nums: list) -> int:
    num_set = set(nums)
    n = len(num_set)

    for i in range(n + 1):
        if i not in num_set:
            return i


### TWO MORE https://neetcode.io/problems/missing-number


if __name__ == "__main__":
    nums = [0, 2]
    print(missing_number_sorting(nums))
    print(missing_number_hash_set(nums))

    nums = [1, 2, 3]
    print(missing_number_sorting(nums))
    print(missing_number_hash_set(nums))

