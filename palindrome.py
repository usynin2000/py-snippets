def is_palindrome(s: str) -> bool:
    new_s = ""
    for c in s:
        if c.isalnum():
            new_s += c.lower()

    return new_s == new_s[::-1]


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(is_palindrome(s))
    s = "tab a cat"
    print(is_palindrome(s))
