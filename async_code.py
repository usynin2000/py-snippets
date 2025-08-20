import asyncio
import time


async def main_seq():
    start = time.time()
    await asyncio.sleep(5)
    await asyncio.sleep(10) # будет исполняться поочерди 15 секунд
    end = time.time()
    print(f'elapsed time: {end - start}')

async def main_parallel():
    start = time.time()
    # Создаем две параллельные задачи
    task1 = asyncio.create_task(asyncio.sleep(5))
    task2 = asyncio.create_task(asyncio.sleep(10)) # будет исполняться 10 секунд
    # Ждем завершения обеих задач одновременно
    await task1
    await task2
    end = time.time()
    print(f'elapsed time: {end - start}')


async def main_gather():
    start = time.time()
    await asyncio.gather(
        asyncio.sleep(5),
        asyncio.sleep(10)
    ) # будет исполняться 10 секунд
    end = time.time()
    print(f'elapsed time: {end - start}')

if __name__ == "__main__":
    asyncio.run(main_seq())
    asyncio.run(main_parallel())
    asyncio.run(main_gather())