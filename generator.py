

def count_up_to(n):
    print("Генератор запущен")
    count = 1
    while count <= n:
        yield count # Возвращает значение и «замораживает» выполнение
        count += 1


if __name__ == "__main__":

    # Использование генератора
    gen = count_up_to(5)

    print(next(gen))

    for number in gen:
        print(f"Получено число: {number}")