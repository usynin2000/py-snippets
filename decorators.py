import time
import functools
from typing import Callable


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


@timing_decorator
def example_function():
    time.sleep(1)
    return "Hello World!"



if __name__ == "__main__":

    example_function()
