import time
import functools
from typing import Callable
from datetime import datetime


### Зачем нужен functools
# ### functools.wraps(func) нужен для того, чтобы сохранить метаданные оригинальной функции, такие как:
###
###  __name__ (имя функции)
###  __doc__ (докстрока)
###  __module__ (модуль, в котором объявлена функция)
### и другие атрибуты


def timing_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed for {execution_time:.6f}")
        return result

    return wrapper


##


def datetime_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        print(f"Function {func.__name__} executed for {execution_time:.6f}")
        return result

    return wrapper


@timing_decorator
def example_function():
    time.sleep(1)
    return "Hello World!"


@datetime_decorator
def example2_function():
    import time

    time.sleep(3)
    return "Hello World 2!"


if __name__ == "__main__":

    example_function()
    example2_function()
