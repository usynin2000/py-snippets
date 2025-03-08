from typing import Callable


def bifurcate_by(lst: list, fn: Callable) -> list:
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]

if __name__ == "__main__":
    print(
        bifurcate_by(["boob", "bar", "foo", "hey"], lambda x: x[0] == "b")
    )