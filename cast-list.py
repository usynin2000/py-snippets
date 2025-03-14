from typing import Any

def cast_list(value:Any) -> list:
    return list(value) if isinstance(value, (tuple, list, set, dict)) else [value]


if __name__ == "__main__":
    data = (2, 3, "fds")

    print(cast_list(data))

    data = {"s": 3, "f": 3}

    print(cast_list(data))
    ## должен отдать только ключ

    data = {3, 4, 1, 3}

    print(cast_list(data))