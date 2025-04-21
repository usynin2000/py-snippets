


def two_sum_brute_force(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

        return []

def two_sum_hash_map_two_passes(nums: list, target: int) -> list:
    indices = dict()
    for i, val in enumerate(nums):
        indices[val] = i

    for i, value in enumerate(nums):
        diff = target - value
        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]

    return []

def two_sum_hash_map_one_pass(nums: list, target: int) -> list:
    indices = dict()
    for i, val, in enumerate(nums):
        diff = target - val
        if diff in indices:
            return [indices[diff], i]
        indices[val] = i

if __name__ == "__main__":
    print(two_sum_brute_force([3, 4, 5, 6], 7))
    print(two_sum_hash_map_two_passes([3, 4, 5, 6], 7))
    print(two_sum_hash_map_one_pass([3, 4, 5, 6], 7))

