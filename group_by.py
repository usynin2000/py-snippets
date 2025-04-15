from collections import defaultdict
from typing import Callable




def group_by(lst: list, fn: Callable) -> dict:
    d = defaultdict(list)
    for el in lst:
        d[fn(el)].append(el)
    return dict(d)





if __name__ == "__main__":
    print(
        group_by(
            ["one", "two", "three"],
            len
        )
    )
