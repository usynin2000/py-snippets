# Checks if the given number falls within the given range.
#
# Use arithmetic comparison to check if the given number is in the specified range.
# If the second parameter, end, is not specified, the range is considered to be from 0 to start.


def in_range(n, start, end=0):
    return start <= n <= end if end >= start else end <= n <= start



if __name__ == "__main__":
    print(in_range(3, 2, 5))  # True
    print(in_range(3, 4))  # True
    print(in_range(2, 3, 5))  # False
    print(in_range(3, 2))  # False