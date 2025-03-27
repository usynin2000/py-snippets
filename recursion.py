from collections.abc import Iterable



def deep_flatten(lst) -> list:
    return (
        [a for i in lst for a in deep_flatten(i)]
        if isinstance(lst, Iterable) else [lst]
    )

def factorial(n: int) -> int:
    print(f"n = {n}")
    if not ((n >= 0) and (n % 1 == 0)):
        raise Exception("Number cannot bet floating point or negative")
    return 1 if n == 0 else n * factorial(n - 1)


if __name__ == "__main__":
    bad_list = [1, [2], [2, 4], [[3, [10]]] ]

    print(deep_flatten(bad_list))

    print(factorial(6))
