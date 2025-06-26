### Add one more solution of task every day. Repeat 5 of previos days and you are ready for inerview.



# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums: list, target: int) -> list:
    hash_map = dict()
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [i, hash_map[target - num]]
        hash_map[num] = i


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
