# You are given a non-empty array of integers nums. Every integer appears twice except for one.
#
# Return the integer that appears only once.


def single_number_brute_force(nums: list[int]) -> int:
    for i in range(len(nums)):
        flag = True

        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                flag = False
                break

        if flag:
            return nums[i]


def single_number_hash_set(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)

    return list(seen)[0]


def single_number_sorting(nums: list[int]) -> int:
    nums.sort()

    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            i += 2
        else:
            return nums[i]
    return nums[i]


def single_number_bit_manipulation(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res = num ^ res
    return res


if __name__ == "__main__":
    lst = [7, 6, 6, 7, 8]
    print(single_number_brute_force(lst))
    print(single_number_hash_set(lst))
    print(single_number_sorting(lst))
    print(single_number_bit_manipulation(lst))
