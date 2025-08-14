import asyncio

async def worker(name, delay):
    print(f"start {name}")
    await asyncio.sleep(delay)
    print(f"end {name}")
    return name

async def main():
    print("main start")
    result1 = asyncio.create_task(worker("A", 1))
    result2 = asyncio.create_task(worker("B", 0.5))

    await asyncio.sleep(0.2)
    print("after first sleep")

    # asyncio.gather(result1, result2) возвращает результаты в том порядке, в котором ты передал задачи, не по порядку завершения.
    res_a, res_b = await asyncio.gather(result1, result2) #
    print(f"results: {res_a}, {res_b}")

    print("main end")

asyncio.run(main())
# main start
# start A
# start B
# after first sleep
# end B
# end A
# results: A, B
# main end
