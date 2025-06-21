
def length_of_las_word(words: str) -> int:
    arr = words.strip().split(" ")

    return len(arr[-1])


if __name__ == "__main__":
    s = "Hello World"

    print(length_of_las_word(s))

    s =  "   fly me   to   the moon  "
    print(length_of_las_word(s))