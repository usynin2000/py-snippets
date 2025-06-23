from math import copysign


def reverse_number(n) -> float:
    return copysign(float(str(n)[::-1].replace("-", "")), n)


def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Time Complexity:
# ( O(n) ) — iterate through half of the array.
#
# Space Complexity:
# ( O(1) ) — in-place with no extra space used.



if __name__ == "__main__":
    print(reverse_number(981))  # 189
    print(reverse_number(-500)) # -5
    print(reverse_number(73.6))  # 6.37
    print(reverse_number(-5.23))  # -32.5


    s = ["h","e","l","l","o"]
    reverse_string(s)
    print(s)

    s = ["H","a","n","n","a","h"]
    reverse_string(s)
    print(s)