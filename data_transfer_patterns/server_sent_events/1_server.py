"""
Server-Sent Events (SSE) - Сервер
==================================
Однонаправленная передача данных от сервера к клиенту

Особенности:
- ✅ Проще чем WebSocket
- ✅ Автоматический reconnect в браузерах
- ✅ Event ID для восстановления потока
- ❌ Только server → client
"""

from aiohttp import web
import asyncio
import json
from datetime import datetime
import random


async def sse_handler(request):
    """
    SSE endpoint - отправляет события клиенту

    Формат SSE:
    data: сообщение\n\n

    С метаданными:
    id: уникальный_id
    event: имя_события
    data: данные
    \n
    """
    response = web.StreamResponse()

    # Обязательные заголовки для SSE
    response.headers['Content-Type'] = 'text/event-stream'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'
    response.headers['Access-Control-Allow-Origin'] = '*'  # Для CORS

    await response.prepare(request)

    print(f"✅ Новый SSE клиент подключился")

    try:
        event_id = 0

        while True:
            event_id += 1

            # Генерируем случайные данные (имитация real-time метрик)
            data = {
                "event_id": event_id,
                "cpu_usage": random.randint(10, 90),
                "memory_usage": random.randint(40, 85),
                "requests_per_sec": random.randint(100, 500),
                "timestamp": datetime.now().isoformat()
            }

            # Формат SSE сообщения
            message = f"id: {event_id}\n"
            message += f"event: metrics\n"
            message += f"data: {json.dumps(data)}\n\n"

            await response.write(message.encode('utf-8'))

            print(f"📤 Отправлено событие #{event_id}")

            # Отправляем каждую секунду
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("❌ Клиент отключился")

    return response


async def sse_progress_bar(request):
    """
    SSE для отображения прогресс-бара длительной операции

    Use-case: загрузка файла, обработка данных, экспорт
    """
    response = web.StreamResponse()
    response.headers['Content-Type'] = 'text/event-stream'
    response.headers['Cache-Control'] = 'no-cache'
    await response.prepare(request)

    print("📊 Начинаем длительную операцию...")

    total_steps = 20

    for step in range(total_steps + 1):
        progress = (step / total_steps) * 100

        data = {
            "step": step,
            "total": total_steps,
            "progress": progress,
            "status": "processing" if step < total_steps else "complete",
            "message": f"Обработано {step}/{total_steps} элементов"
        }

        message = f"data: {json.dumps(data)}\n\n"
        await response.write(message.encode('utf-8'))

        print(f"📊 Прогресс: {progress:.0f}%")

        await asyncio.sleep(0.5)

    # Финальное сообщение
    final_message = "event: done\ndata: {\"status\": \"completed\"}\n\n"
    await response.write(final_message.encode('utf-8'))

    print("✅ Операция завершена!")

    return response


async def sse_notifications(request):
    """
    SSE для уведомлений (имитация новостной ленты)
    """
    response = web.StreamResponse()
    response.headers['Content-Type'] = 'text/event-stream'
    response.headers['Cache-Control'] = 'no-cache'
    await response.prepare(request)

    notifications = [
        {"type": "info", "title": "Новое сообщение", "text": "У вас новое сообщение от Алексея"},
        {"type": "warning", "title": "Предупреждение", "text": "Осталось 10% места на диске"},
        {"type": "success", "title": "Успех", "text": "Резервное копирование завершено"},
        {"type": "error", "title": "Ошибка", "text": "Не удалось подключиться к базе данных"},
        {"type": "info", "title": "Обновление", "text": "Доступна новая версия приложения"},
    ]

    for i, notification in enumerate(notifications):
        notification["id"] = i + 1
        notification["timestamp"] = datetime.now().isoformat()

        message = f"id: {i + 1}\n"
        message += f"event: notification\n"
        message += f"data: {json.dumps(notification)}\n\n"

        await response.write(message.encode('utf-8'))
        print(f"🔔 Уведомление #{i + 1}: {notification['title']}")

        await asyncio.sleep(3)  # Новое уведомление каждые 3 секунды

    return response


async def index_handler(request):
    """
    HTML страница с JavaScript клиентом для тестирования
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSE Demo</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial; margin: 20px; background: #f0f0f0; }
            .container { background: white; padding: 20px; border-radius: 8px; }
            .event { padding: 10px; margin: 5px 0; border-left: 4px solid #007bff; background: #f8f9fa; }
            .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 20px 0; }
            .metric { background: #e9ecef; padding: 15px; border-radius: 4px; text-align: center; }
            button { padding: 10px 20px; margin: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌊 Server-Sent Events Demo</h1>

            <div>
                <button onclick="connectMetrics()">📊 Подключить метрики</button>
                <button onclick="connectProgress()">📈 Прогресс-бар</button>
                <button onclick="connectNotifications()">🔔 Уведомления</button>
                <button onclick="disconnect()">❌ Отключить</button>
            </div>

            <div id="metrics" class="metrics" style="display:none;">
                <div class="metric">
                    <h3>CPU</h3>
                    <div id="cpu">-</div>
                </div>
                <div class="metric">
                    <h3>Memory</h3>
                    <div id="memory">-</div>
                </div>
                <div class="metric">
                    <h3>Requests/s</h3>
                    <div id="requests">-</div>
                </div>
            </div>

            <div id="output"></div>
        </div>

        <script>
            let eventSource = null;

            function disconnect() {
                if (eventSource) {
                    eventSource.close();
                    eventSource = null;
                    log('❌ Отключено');
                }
            }

            function connectMetrics() {
                disconnect();
                document.getElementById('metrics').style.display = 'grid';
                eventSource = new EventSource('/sse/metrics');

                eventSource.addEventListener('metrics', (e) => {
                    const data = JSON.parse(e.data);
                    document.getElementById('cpu').textContent = data.cpu_usage + '%';
                    document.getElementById('memory').textContent = data.memory_usage + '%';
                    document.getElementById('requests').textContent = data.requests_per_sec;
                });

                eventSource.onerror = () => log('❌ Ошибка соединения');
                log('✅ Подключено к метрикам');
            }

            function connectProgress() {
                disconnect();
                document.getElementById('metrics').style.display = 'none';
                eventSource = new EventSource('/sse/progress');

                eventSource.onmessage = (e) => {
                    const data = JSON.parse(e.data);
                    log(`📊 ${data.message} (${data.progress.toFixed(0)}%)`);
                };

                eventSource.addEventListener('done', () => {
                    log('✅ Операция завершена!');
                    disconnect();
                });
            }

            function connectNotifications() {
                disconnect();
                document.getElementById('metrics').style.display = 'none';
                eventSource = new EventSource('/sse/notifications');

                eventSource.addEventListener('notification', (e) => {
                    const data = JSON.parse(e.data);
                    const emoji = {info: 'ℹ️', warning: '⚠️', success: '✅', error: '❌'}[data.type];
                    log(`${emoji} ${data.title}: ${data.text}`);
                });
            }

            function log(message) {
                const output = document.getElementById('output');
                const div = document.createElement('div');
                div.className = 'event';
                div.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
                output.insertBefore(div, output.firstChild);
            }
        </script>
    </body>
    </html>
    """
    return web.Response(text=html, content_type='text/html')


def main():
    """
    Запуск SSE сервера
    """
    app = web.Application()

    # Роуты
    app.router.add_get('/', index_handler)
    app.router.add_get('/sse/metrics', sse_handler)
    app.router.add_get('/sse/progress', sse_progress_bar)
    app.router.add_get('/sse/notifications', sse_notifications)

    print("╔══════════════════════════════════════════╗")
    print("║  🌊 SSE Server запущен                   ║")
    print("╠══════════════════════════════════════════╣")
    print("║  http://localhost:8080                   ║")
    print("║                                          ║")
    print("║  Endpoints:                              ║")
    print("║  GET /sse/metrics - метрики системы      ║")
    print("║  GET /sse/progress - прогресс-бар        ║")
    print("║  GET /sse/notifications - уведомления    ║")
    print("╚══════════════════════════════════════════╝")

    web.run_app(app, host='localhost', port=8080)


if __name__ == "__main__":
    main()

# 1. Создание подключения (строка 215)

# eventSource = new EventSource('/sse/metrics');
# Что происходит:
# Браузер отправляет GET-запрос на /sse/metrics
# Сервер отвечает с заголовком Content-Type: text/event-stream
# Браузер открывает HTTP-соединение и держит его открытым
# Это не обычный запрос-ответ: соединение остается открытым

# 2. Подписка на события (строки 217-222)
# eventSource.addEventListener('metrics', (e) => {
#     const data = JSON.parse(e.data);
#     // обновление DOM
# });

# Как это работает:

# Сервер отправляет события в формате SSE:
#   id: 1
#   event: metrics
#   data: {"cpu_usage": 45, ...}

# Браузер парсит поток и вызывает обработчик для события metrics
# e.data содержит строку из поля data: серверного сообщения
# Визуализация потока:
# Клиент                    Сервер
#   |                         |
#   |--- GET /sse/metrics --->|
#   |<-- 200 OK (stream) -----|
#   |                         |
#   |<-- id: 1                |
#   |<-- event: metrics       |
#   |<-- data: {...}          |
#   |                         |
#   |   (обработчик вызывается)|
#   |                         |
#   |<-- id: 2                |
#   |<-- event: metrics       |
#   |<-- data: {...}          |
#   |                         |
#   |   (обработчик вызывается)|
#   |                         |
#   |   ... (вечный цикл)     |


# Отличия от обычного HTTP:
# Обычный HTTP	SSE
# Запрос → Ответ → Закрытие	Запрос → Ответ → Соединение открыто
# Клиент инициирует	Сервер отправляет данные когда хочет
# Нет автоматического reconnect	Автоматический reconnect



# Важные моменты:
# EventSource — это встроенный браузерный API, не нужны библиотеки
# Только GET-запросы (нельзя отправлять данные в теле)
# Только текстовые данные (бинарные не поддерживаются)
# Автоматический reconnect — встроен в браузер
