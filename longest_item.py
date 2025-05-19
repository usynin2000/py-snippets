from typing import Any


def longest_item(*args) -> Any:
    return max(args, key=len)

# Use max() with len() as the key to return the item with the greatest length.
# If multiple items have the same length, the first one will be returned.



if __name__ == "__main__":
    print(longest_item('this', 'is', 'a', 'testcase'))
    print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
    print(longest_item([1, 2, 3], 'foobar'))