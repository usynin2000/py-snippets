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



if __name__ == "__main__":
    print(single_number_brute_force([7,6,6,7,8]))
    print(single_number_hash_set([7,6,6,7,8]))