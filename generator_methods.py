


def my_gen():
    yield 1
    x = yield 2
    print(f"Recieved  in generator {x}")
    yield 3


def gen():
    try:
        yield 1
    except ValueError:
        yield "Error Handeled"
    finally:
        print("Closing generator")


if __name__ == "__main__":
    g = my_gen()
    print(next(g))
    print(g.send(None))
    print(g.send(42))


    g_2 = gen()
    print(next(g_2))
    print(g_2.throw(ValueError))
    g_2.close()

