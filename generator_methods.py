


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


# Сделай генератор accumulator(), который будет накапливать сумму чисел, которые ему передают через send().
def accumulator():
    total = 0
    value = yield total  # первый yield отдаёт начальную сумму (0)
    while True:
        total += value  # добавляем полученное через send() значение
        value = yield total  # возвращаем новую сумму и ждём следующего send()




if __name__ == "__main__":
    g = my_gen()
    print(next(g))
    print(g.send(None))
    print(g.send(42))


    g_2 = gen()
    print(next(g_2))
    print(g_2.throw(ValueError))
    g_2.close()

    gen = accumulator()
    next(gen)  # Нужно вызвать, чтобы генератор начал работать
    print(gen.send(5))  # Выведет 5
    print(gen.send(3))  # Выведет 8
    print(gen.send(10))  # Выведет 18

