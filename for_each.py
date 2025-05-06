from typing import Iterable, Callable, Any


def for_each(itr: Iterable, func: Callable) -> Any:
    for el in itr:
        func(el)


if __name__ == "__main__":
    for_each([1, 2, 3, 4, 5], print)
