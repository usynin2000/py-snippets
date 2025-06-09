from functools import reduce
from math import gcd

# Returns the least common multiple of a list of numbers.

# reduce — применяет функцию к элементам последовательности по порядку, сводя список к одному значению.
# В reduce(...) мы передаём лямбда-функцию:
# lambda x, y: int(x * y / gcd(x, y))
# которая берёт два числа x и y, находит их НОК и возвращает его.
# reduce будет применять эту функцию ко всем элементам списка слева направо:

def lcm(numbers):
    return reduce(
        (
            lambda x, y: int(x * y /gcd(x, y))
        ),
        numbers
    )


if __name__ == "__main__":
    print(lcm([12, 7]))
    print(lcm([1, 3, 4, 5]))