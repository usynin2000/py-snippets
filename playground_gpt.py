
from collections import Counter


def find_unique(numbers: list[int]) -> int:
    counter = Counter(numbers)

    for key, value in counter.items():
        if value == 1:
            return key

def find_2_uniques(numbers: list[int]) -> list[int]:
    counter = Counter(numbers)
    res = list()
    for key, value in counter.items():
        if value == 1:
            res.append(key)

    return res

def is_palindrome(string: str) -> bool:
    return string == string[::-1]


def sum_list(lst: list[int]) -> int:
    return sum(lst)

def is_even(number: int) -> bool:
    return number % 2 == 0

def count_vowels(s: str) -> int:
    vowels = "aeuio"

    counter = 0

    for i in s.lower():
        if i in vowels:
            counter += 1

    return counter

def find_max(numbers: list[int]) -> int:
    max_num = numbers[0]

    for num in numbers:
        max_num = max(max_num, num)

    return max_num


def char_frequency(s: str) -> dict:
    return Counter(s)

# without reverse
def reverse_list(lst: list) -> list:
    res = list()
    for i in lst[::-1]:
        res.append(i)

    return res

def reverse_list(lst: list) -> list:
    res = []
    for i in range(len(lst) - 1, -1, -1):
        res.append(lst[i])
    return res

def is_anagram_manual(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    freq = dict()

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True

if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4, 5]))
    print(is_even(3))
    print(is_even(10))
    print(count_vowels("Gachimuchi"))
    print(find_max([1, 2, 4, 10, 3, 4, 5]))
    print(is_anagram_manual("silent", "listen"))
    print(is_anagram_manual("silents", "listen"))