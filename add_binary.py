
# Given two binary strings a and b, return their sum as a binary string.
#
# Input: a = "11", b = "1"
# Output: "100"
#


## переводим в десятиричную систему
# Используем встроенную функцию bin(s), которая переводит число в бинарный формат, но результат — это строка вида '0b100'.
# Для того чтобы избавиться от префикса '0b', делаем срез: [2:].
def add_binary(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)

    s = a + b

    return bin(s)[2:]


if __name__ == "__main__":
    print(add_binary(a="11", b="1"))

    a = "1010"
    b = "1011"

    print(add_binary(a, b))