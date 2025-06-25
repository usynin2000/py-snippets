def is_palindrome(s: str) -> bool:
    new_s = ""
    for c in s:
        if c.isalnum():
            new_s += c.lower()

    return new_s == new_s[::-1]


def is_palindrome_number(x: int) -> bool:
    x_str = str(x)
    left, right = 0, len(x_str) - 1

    while left < right:
        if x_str[left] != x_str[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_number_2(x: int) -> bool:
    if x < 0:
        return False

    reverse = 0
    xcopy = x

    while x > 0:
        reverse = reverse * 10 + (x % 10)
        x //= 10

    return reverse == xcopy


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(is_palindrome(s))
    s = "tab a cat"
    print(is_palindrome(s))

    x = 10
    print(is_palindrome_number(x))
    print(is_palindrome_number_2(x))

    x = 121
    print(is_palindrome_number(x))
    print(is_palindrome_number_2(x))
