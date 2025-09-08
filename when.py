from typing import Callable
# Tests a value, x, against a testing function, conditionally applying a function.

# Check if the value of predicate() is True for x and if so call when_true(), otherwise return x.


def when(predicate: Callable, when_true: Callable):
    return lambda x: when_true(x) if predicate(x) else x



if __name__ == "__main__":
    double_even_numbers = when(lambda x: x % 2 == 0, lambda x: x * 2)

    print(double_even_numbers(1))
    print(double_even_numbers(2))
    print(double_even_numbers(3))
    print(double_even_numbers(4))
