# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
from collections import defaultdict


def group_anagrams_sorting(strs: list):
    res = defaultdict(list)
    for word in strs:
        sorted_str = "".join(sorted(word))
        res[sorted_str].append(word)

    return list(res.values())




if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(group_anagrams_sorting(strs))
