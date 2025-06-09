from functools import reduce
from math import gcd

# Returns the least common multiple of a list of numbers.

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