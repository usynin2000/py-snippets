


# Returns the most frequent element in a list.
#
# Use set() to get the unique values in lst.
# Use max() to find the element that has the most appearances.


def most_frequent(lst: list) -> int:
    print("set", set(lst))
    print("key", lst.count) # key <built-in method count of list object at 0x1025c4940>
    return max(set(lst), key=lst.count)


if __name__ == "__main__":

    a = [1, 2, 1, 2, 3, 2, 1, 4, 2]
    print(most_frequent(a))