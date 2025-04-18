

def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)


if __name__ == '__main__':
    print(is_anagram("racecar", "carrace"))
    print(is_anagram("racecar", "ca2rrace"))