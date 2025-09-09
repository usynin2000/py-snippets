from time import sleep
from typing import Callable


def delay(fn: Callable, ms: int, *args) -> None:
    sleep(ms / 1000)
    return fn(*args)



if __name__ == '__main__':
    delay(lambda x: print(x), 1000, "later")