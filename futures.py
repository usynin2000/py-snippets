import asyncio

# Например, в Python (asyncio.Future) или в JavaScript (Promise — фактически тоже future):
#
# Когда ты запускаешь асинхронную задачу, возвращается Future.
#
# Пока задача выполняется, Future в состоянии pending.
#
# Когда задача завершилась, Future становится done (с результатом или исключением).
#
# await future приостанавливает выполнение функции до тех пор, пока future не готово.

async def slow_add(x, y):
    await asyncio.sleep(1)
    return x + y

async def main():
    task = asyncio.create_task(slow_add(2, 3))
    result = await task
    print("Результат:", result)

asyncio.run(main())

from concurrent.futures import ThreadPoolExecutor
import time

def slow_add(x, y):
    time.sleep(2)
    return x + y

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(slow_add, 2, 3)
    print("Задача выполняется ...")
    result = future.result() # блокируемся, пока не посчитаемся
    print("Результат", result)

# Ты отправляешь задачу в ThreadPoolExecutor или ProcessPoolExecutor.
#
# Возвращается Future, которое пока ещё не имеет результата.
#
# Метод .result() блокирует поток до завершения задачи.


# Общее:
#
# Future — это «контейнер обещанного результата».
#
# В асинхронности часто используют await future.
#
# В многопоточности — .result().