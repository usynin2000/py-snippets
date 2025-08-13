import asyncio
import time

async def get_result():
    print("Начал работу функции")
    await asyncio.sleep(3)
    return 10

async def main():
    print("Создаю задачу")
    task = asyncio.create_task(get_result())
    print("После создания таски, но до начало работы")
    res = await task
    print("Получил res", res)


asyncio.run(main())

#
# Да, совершенно верно! 😄
#
# create_task — регистрация корутины в event loop. Она не начинает выполнение сразу в момент вызова, а просто говорит: «Эй, вот корутина, запускай её, когда будет возможность».
#
# Основное преимущество: можно сразу продолжать код без блокировки и иметь объект Task, с которым потом удобно:
#
# делать await и получить результат,
#
# проверять состояние (task.done(), task.cancel()),
#
# обрабатывать ошибки.