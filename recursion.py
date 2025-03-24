from collections.abc import Iterable



def deep_flatten(lst) -> list:
    return (
        [a for i in lst for a in deep_flatten(i)]
        if isinstance(lst, Iterable) else [lst]
    )


if __name__ == "__main__":
    bad_list = [1, [2], [2, 4], [[3, [10]]] ]

    print(deep_flatten(bad_list))
