### Add one more solution of task every day. Repeat 5 of previos days and you are ready for inerview.

### ARRAYS AND HASHING

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


def contains_duplicate(nums: list) -> bool:
    return len(nums) != len(set(nums))



from collections import Counter

def is_anagram(s: str, t: str) -> bool:
     return Counter(s) == Counter(t)


def is_anagram_big(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = dict()
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char in t:
        if char not in counter or counter[char] == 0:
            return False
        counter[char] -= 1

    return True


from collections import defaultdict

def group_anagrams(strs: list):
    res = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        res[key].append(word)

    print(dict(res))
    return list(res.values())



# #Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Input: nums = [1], k = 1
# Output: [1]
#
def top_k_frequent(nums: list, k: int) -> list:
    count = dict()
    for i in nums:
        count[i] = count.get(i, 0) + 1

    freg_list = []
    for k, v in count.items():
        freg_list.append((v, k))

    freg_list.sort(reverse=True)

    result = []
    for i in range(k):
        result.append(freg_list[i][1])
    return result


# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

# def product_except_self(nums: list) -> list:
#     prods = defaultdict(int)
#     def prod(arr):
#         return 0
#     ans = 1
#     for i in arr:
#         ans *= i
#     return ans



# Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

## BAD UNDERSTANDING NEED CHAT WITH CHPT
def merge_intervals(intervals:list[list]) -> list[list]:
    intervals.sort()
    merged = []
    prev = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= prev[1]:
            prev[1] = max(prev[1], intervals[i][1])
        else:
            merged.append(prev)
            prev = intervals[i]
    merged.append(prev)
    return merged


# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#

def max_sub_array(nums: list) -> int:
    res = nums[0]
    total = 0

    for num in nums:
        if total < 0:
            total = 0

        total += num

        res = max(total, res)

    return res





### TWO POINTERS
def is_palindrome(s: str) -> bool:
    filtered = [
        c.lower() for c in s if c.isalnum()
    ]
    return filtered == filtered[::-1]


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

    print(contains_duplicate([1, 2, 3, 1]))

    print(is_anagram("anagram", "nagaram"))
    print(is_anagram_big("car", "rat"))
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(top_k_frequent([1,1,1,2,2,3],2 ))
    print(top_k_frequent([1,1,1,2,2,3, 4, 5],3 ))
    print(merge_intervals([[1, 2], [2, 4]]))
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array([5,4,-1,7,8]))
    print(max_sub_array([5,4,-1,7,8, 10]))
    s = "Was it a car or a cat I saw?"
    print(is_palindrome(s))
    s = "tab a cat"
    print(is_palindrome(s))
