# You are given an integer array digits, where each digits[i] is the ith digit of a large integer.
# It is ordered from most significant to least significant digit, and it will not contain any leading zero.
#
# Return the digits of the given integer after incrementing it by one.


def plus_one_recursion(numbers: list[int]) -> list[int]:
    if not numbers:
        return [1]

    if numbers[-1] < 9:
        numbers[-1] += 1
        return numbers
    else:
        return plus_one_recursion(numbers[:-1]) + [0]


def plust_one_iteration(numbers: list[int]) -> list[int]:
    pass


if __name__ == "__main__":
    digits = [1, 2, 3, 4]
    print(plus_one_recursion(digits))

    digits = [9, 9, 9]
    print(plus_one_recursion(digits))
