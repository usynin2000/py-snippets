from math import floor


# Pads a string on both sides with the specified character, if it's shorter than the specified length.
# Omit the third argument, char, to use the whitespace character as the default padding character.

def pad(s: str, length: int, char: str = " "):
    return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)

# Как это работает
#
# len(s) — длина исходной строки.
#
# floor((len(s) + length)/2)
#
# Это количество символов, до которого нужно выровнять строку справа (через rjust).
#
# Таким образом, мы добавляем "левую" часть отступа.
#
# s.rjust(..., char)
#
# Дополняет строку слева символами char, чтобы длина стала равна floor((len(s) + length)/2).
#
# .ljust(length, char)
#
# Дополняет строку справа символами char, чтобы длина в итоге стала ровно length.


if __name__ == "__main__":
    print(pad("cat", 8))
    print(pad('42', 6, '0'))
    print(pad('foobar', 3))