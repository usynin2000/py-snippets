from functools import partial

# Удобство повторного использования:
# можно заранее зафиксировать часто используемые аргументы и переиспользовать функцию.


def curry(fn, *args):
    return partial(fn, *args)


if __name__ == "__main__":
    add = lambda x, y: x + y

    add10 = curry(add, 10)

    print(add10(20))

    add200 = curry(add, 200)

    print(add200(300))
