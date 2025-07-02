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


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

    print(contains_duplicate([1, 2, 3, 1]))

    print(is_anagram("anagram", "nagaram"))
    print(is_anagram_big("car", "rat"))
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(top_k_frequent([1,1,1,2,2,3],2 ))
    print(top_k_frequent([1,1,1,2,2,3, 4, 5],3 ))
