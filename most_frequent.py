


# Returns the most frequent element in a list.
#
# Use set() to get the unique values in lst.
# Use max() to find the element that has the most appearances.


def most_frequent(lst: list) -> int:
    return max(set(lst), key=lst.count)


if __name__ == "__main__":

    a = [1, 2, 1, 2, 3, 2, 1, 4, 2]
    print(most_frequent(a))