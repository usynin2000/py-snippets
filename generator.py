

def count_up_to(n):
    print("Генератор запущен")
    count = 1
    while count <= n:
        yield count # Возвращает значение и «замораживает» выполнение
        count += 1







def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


def even_numbers(value: int):
    for i in range(0, value + 1, 2):
        yield i


if __name__ == "__main__":

    # Использование генератора
    gen = count_up_to(5)

    print(next(gen))

    for number in gen:
        print(f"Получено число: {number}")


    for num in countdown(5):
        print(num)

    for num in even_numbers(10):
        print(num)