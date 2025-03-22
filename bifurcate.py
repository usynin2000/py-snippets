from typing import Callable


def bifurcate_by(lst: list, fn: Callable) -> list:
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]

def bifurcate(lst: list, filter: list) -> list[list]:
    return [
        [x for x, flag in zip(lst, filter) if flag],
        [x for x, flag in zip(lst, filter) if not flag]
    ]

if __name__ == "__main__":
    print(
        bifurcate_by(["boob", "bar", "foo", "hey"], lambda x: x[0] == "b")
    )

    lst_1 = ["beep", "boop", "zip", "zap", 3]
    lst_2 =[True, False, True, True, False]

    print(bifurcate(lst_1, lst_2))