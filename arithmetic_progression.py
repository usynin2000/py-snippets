# Generates a list of numbers in the arithmetic progression starting with the given positive integer and up to the specified limit.
#
# Use range() and list() with the appropriate start, step and end values.


def arithmetic_progression(n: int, limit: int) -> list:
    return list(range(n, limit + 1, n))


if __name__ == "__main__":
    print(arithmetic_progression(5, 25))
