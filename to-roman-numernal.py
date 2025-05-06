def to_roman_numeral(num: int) -> str:
    lookup = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    res = ""
    for (n, roman) in lookup:
        (d, num) = divmod(num, n)
        res += roman * d
    return res


if __name__ == "__main__":
    print(to_roman_numeral(3))  # 'III'
    print(to_roman_numeral(11))  # 'XI'
    print(to_roman_numeral(1998))  # 'MCMXCVIII'
