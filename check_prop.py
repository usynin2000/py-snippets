from typing import Callable, Any


def check_prop(fn: Callable, prop: Any) -> Any:
    return lambda obj: fn(obj[prop])


if __name__ == "__main__":

    check_age = check_prop(lambda x: x >= 18, "age")
    user = {"user": "Mark", "age": 18}
    print(check_age(user))
