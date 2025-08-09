import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

urls = [
    "https://httpbin.org/delay/1" for _ in range(10)
]

def fetch(url):
    r = requests.get(url)
    return r.status_code

start = time.time()

with ThreadPoolExecutor(max_workers=10) as executor:

    # Передаёт задачу (fetch(url)) в пул потоков.
    # Возвращает объект Future — это как «квитанция» на задачу: по ней можно узнать результат позже.
    # Мы создаём список всех задач, которые пул должен выполнить.
    futures = [executor.submit(fetch, url) for url in urls]

    results = list()

    # as_completed(futures)
    # Генератор, который даёт Future в порядке завершения задач (а не в порядке запуска).
    # Это полезно, если хочется обрабатывать результаты по мере готовности.
    for future in as_completed(futures):
        # Блокирующий вызов: ждёт, пока задача завершится, и возвращает результат.
        results.append(future.result())

end = time.time()

# 💡 Разница с executor.map:
#
# map → сразу возвращает результаты в порядке отправки задач.
#
# submit + as_completed → можно обрабатывать задачи в порядке их готовности.
# Это иногда быстрее, если есть быстрые и медленные задачи вперемешку.


print("Результаты:", results)
print("Время:", round(end - start, 2), "сек.")
