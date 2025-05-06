### Greatest common divider
from functools import reduce
from math import gcd as gcd_


def gcd(numbers: list[int]) -> int:
    return int(reduce(gcd_, numbers))


if __name__ == "__main__":
    print(gcd([8, 36, 28]))
    print(gcd([20, 15, 45]))
