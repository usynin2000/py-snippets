from collections import Counter


def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


def is_anagram_case_insensitive(a: str, b: str) -> bool:
    # Checks if a string is an anagram of another string
    # (case - insensitive, ignores
    # spaces, punctuation and special
    # characters).

    return Counter(s.lower() for s in a if s.isalnum()) == Counter(
        s.lower() for s in b if s.isalnum()
    )
    # Use str.isalnum() to filter out non-alphanumeric characters, str.lower() to transform each character to lowercase.
    # Use collections.Counter to count the resulting characters for each string and compare the results.


if __name__ == "__main__":
    print(is_anagram("racecar", "carrace"))
    print(is_anagram("racecar", "ca2rrace"))
    print(is_anagram_case_insensitive("#anagram", "Nag a ram!"))
