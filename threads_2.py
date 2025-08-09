import requests
import time

from concurrent.futures import ThreadPoolExecutor

# Список URL с задержкой 2 секунды (httpbin.org/delay/N имитирует долгий ответ)
urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]

def fetch(url: str) -> int:
    print(f"Запрос к {url} начат.")
    r = requests.get(url)
    print(f"Запрос к {url} закончен.")
    return r.status_code

# Однопоточный вариант:
start = time.time()

results_sync = [fetch(url) for url in urls]

print(f"Однопоточно заняло: {time.time() - start:.2f} секунд")

# ---------- Многопоточный вариант ----------
start = time.time()
with ThreadPoolExecutor(max_workers=50) as executor:
    results_threaded = list(executor.map(fetch, urls))
print(f"Многопоточно заняло: {time.time() - start:.2f} секунд")

# ThreadPoolExecutor — это менеджер, который создаёт пул (группу) потоков.
# max_workers=50 — это максимальное количество одновременно работающих потоков.
# Когда один поток закончит, пул возьмёт следующую задачу из очереди.

# with ... as executor: — это контекстный менеджер:
 # Создаёт пул потоков.
 # Гарантирует, что в конце работы пул будет корректно закрыт (executor.shutdown()).

 #executor.map(fetch, urls)
 # Берёт функцию fetch и список аргументов (urls).
 # Запускает вызовы fetch(url) в пуле потоков.
 # Работает очень похоже на встроенную map, но задачи идут в разных потоках.

 # list(...)
    # Превращает результат генератора в список (чтобы получить все статусы ответов).
    # Одновременно ждёт выполнения всех потоков.