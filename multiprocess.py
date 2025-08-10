import time
import multiprocessing

def heavy_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total


if __name__ == "__main__":
    numbers = [50_000_000, 50_000_000, 50_000_000, 50_000_000]
    print(type(numbers[0]))

    # --- Однопроцессный вариант ---
    start = time.time()
    results = [heavy_task(n) for n in numbers]
    print(f"Однопроцессно: {time.time() - start:.2f} сек")

    # --- Многопроцессный вариант ---
    start = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_task, numbers)

    print(f"Многопроцессно: {time.time() - start:.2f} сек")


# Как это работает:
# multiprocessing.Pool создаёт несколько процессов, каждый из которых исполняется своим интерпретатором Python (GIL не мешает, так как у каждого процесса — своя память и GIL).

# pool.map распределяет задачи по процессам.

# Для CPU-bound задач ускорение будет почти пропорционально количеству ядер.