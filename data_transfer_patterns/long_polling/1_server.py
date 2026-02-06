"""
Long Polling - Сервер
======================
Клиент делает запрос, сервер держит соединение открытым
до появления данных или таймаута

Преимущества:
- ✅ Работает через обычный HTTP
- ✅ Лучше чем short polling
- ✅ Proactive updates

Недостатки:
- ❌ Overhead от HTTP headers при каждом reconnect
- ❌ Нагрузка на сервер (открытые соединения)
"""

from aiohttp import web
import asyncio
import json
from datetime import datetime
from collections import deque


# Глобальная очередь событий
event_queue = deque(maxlen=100)
event_id_counter = 0

# Подписчики ожидающие новых событий
waiting_clients = []


async def add_event(event_data):
    """
    Добавляет новое событие и уведомляет ожидающих клиентов
    """
    global event_id_counter
    event_id_counter += 1

    event = {
        "id": event_id_counter,
        "data": event_data,
        "timestamp": datetime.now().isoformat()
    }

    event_queue.append(event)
    print(f"📢 Новое событие #{event_id_counter}: {event_data['message']}")

    # Уведомляем всех ожидающих клиентов
    for future in waiting_clients:
        if not future.done():
            future.set_result(event)

    waiting_clients.clear()


async def long_poll_handler(request):
    """
    Long polling endpoint

    Параметры:
    - since: ID последнего полученного события
    - timeout: максимальное время ожидания (секунды)
    """
    try:
        since_id = int(request.query.get('since', 0))
        timeout = int(request.query.get('timeout', 30))
    except ValueError:
        return web.json_response(
            {"error": "Invalid parameters"},
            status=400
        )

    print(f"📥 Клиент запросил события с ID > {since_id}")

    # Проверяем, есть ли новые события в очереди
    new_events = [e for e in event_queue if e['id'] > since_id]

    if new_events:
        # Если есть новые события, сразу отправляем
        print(f"✅ Отправляем {len(new_events)} событий сразу")
        return web.json_response({
            "events": new_events,
            "last_id": new_events[-1]['id']
        })

    # Если новых событий нет, ждем появления или таймаута
    print(f"⏳ Клиент ждет новых событий (timeout: {timeout}s)")

    future = asyncio.Future()
    waiting_clients.append(future)

    try:
        # Ждем появления события или таймаута
        event = await asyncio.wait_for(future, timeout=timeout)

        print(f"✅ Отправляем новое событие #{event['id']}")
        return web.json_response({
            "events": [event],
            "last_id": event['id']
        })

    except asyncio.TimeoutError:
        # Таймаут - отправляем пустой ответ
        print("⏰ Таймаут - отправляем пустой ответ")
        return web.json_response({
            "events": [],
            "last_id": since_id
        })

    finally:
        # Удаляем future из списка ожидающих
        if future in waiting_clients:
            waiting_clients.remove(future)


async def create_event_handler(request):
    """
    Endpoint для создания новых событий (для тестирования)

    POST /events
    {"message": "Новое событие", "priority": "high"}
    """
    try:
        data = await request.json()
        await add_event(data)

        return web.json_response({
            "success": True,
            "event_id": event_id_counter
        })

    except Exception as e:
        return web.json_response(
            {"error": str(e)},
            status=400
        )


async def status_handler(request):
    """
    Статус сервера
    """
    return web.json_response({
        "total_events": len(event_queue),
        "last_event_id": event_id_counter,
        "waiting_clients": len(waiting_clients),
        "oldest_event_id": event_queue[0]['id'] if event_queue else None
    })


async def generate_random_events(app):
    """
    Фоновая задача генерации случайных событий
    """
    import random

    messages = [
        "Новый заказ получен",
        "Пользователь зарегистрировался",
        "Платеж обработан",
        "Комментарий добавлен",
        "Файл загружен",
        "Задача выполнена"
    ]

    while True:
        await asyncio.sleep(random.randint(5, 15))  # Случайный интервал

        await add_event({
            "message": random.choice(messages),
            "priority": random.choice(["low", "medium", "high"]),
            "user_id": random.randint(1, 100)
        })


async def index_handler(request):
    """
    HTML страница с JavaScript клиентом
    """
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Long Polling Demo</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial; margin: 20px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }
            .event { padding: 12px; margin: 8px 0; border-radius: 4px; border-left: 4px solid #007bff; background: #f8f9fa; }
            .event.high { border-left-color: #dc3545; }
            .event.medium { border-left-color: #ffc107; }
            .controls { margin: 20px 0; }
            button { padding: 10px 20px; margin: 5px; cursor: pointer; }
            .status { padding: 10px; background: #e9ecef; border-radius: 4px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>⏳ Long Polling Demo</h1>

            <div class="status" id="status">
                Статус: <span id="statusText">Не подключено</span><br>
                Получено событий: <span id="eventCount">0</span>
            </div>

            <div class="controls">
                <button onclick="startPolling()">▶️ Начать polling</button>
                <button onclick="stopPolling()">⏸️ Остановить</button>
                <button onclick="sendEvent()">📨 Отправить событие</button>
                <button onclick="clearEvents()">🗑️ Очистить</button>
            </div>

            <h3>События:</h3>
            <div id="events"></div>
        </div>

        <script>
            let lastEventId = 0;
            let polling = false;
            let eventCount = 0;

            async function longPoll() {
                if (!polling) return;

                updateStatus('🔄 Ожидание событий...');

                try {
                    const response = await fetch(`/poll?since=${lastEventId}&timeout=30`);
                    const data = await response.json();

                    if (data.events && data.events.length > 0) {
                        data.events.forEach(event => {
                            addEventToUI(event);
                            lastEventId = event.id;
                            eventCount++;
                        });
                    }

                    document.getElementById('eventCount').textContent = eventCount;

                    // Сразу делаем следующий запрос
                    if (polling) {
                        setTimeout(longPoll, 100);
                    }

                } catch (error) {
                    console.error('Ошибка:', error);
                    updateStatus('❌ Ошибка соединения');

                    if (polling) {
                        setTimeout(longPoll, 3000);  // Retry через 3 секунды
                    }
                }
            }

            function startPolling() {
                polling = true;
                updateStatus('✅ Подключено');
                longPoll();
            }

            function stopPolling() {
                polling = false;
                updateStatus('⏸️ Остановлено');
            }

            async function sendEvent() {
                const message = prompt('Введите сообщение:', 'Тестовое событие');
                if (!message) return;

                try {
                    await fetch('/events', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            message: message,
                            priority: 'high'
                        })
                    });
                } catch (error) {
                    alert('Ошибка отправки: ' + error);
                }
            }

            function clearEvents() {
                document.getElementById('events').innerHTML = '';
                eventCount = 0;
                document.getElementById('eventCount').textContent = '0';
            }

            function addEventToUI(event) {
                const container = document.getElementById('events');
                const div = document.createElement('div');
                div.className = `event ${event.data.priority}`;

                const time = new Date(event.timestamp).toLocaleTimeString();
                div.innerHTML = `
                    <strong>#${event.id}</strong> [${time}]<br>
                    📌 ${event.data.message}<br>
                    <small>Priority: ${event.data.priority}</small>
                `;

                container.insertBefore(div, container.firstChild);
            }

            function updateStatus(text) {
                document.getElementById('statusText').textContent = text;
            }
        </script>
    </body>
    </html>
    """
    return web.Response(text=html, content_type='text/html')


async def start_background_tasks(app):
    """Запуск фоновых задач"""
    app['event_generator'] = asyncio.create_task(generate_random_events(app))


async def cleanup_background_tasks(app):
    """Остановка фоновых задач"""
    app['event_generator'].cancel()
    await app['event_generator']


def main():
    app = web.Application()

    # Роуты
    app.router.add_get('/', index_handler)
    app.router.add_get('/poll', long_poll_handler)
    app.router.add_get('/status', status_handler)
    app.router.add_post('/events', create_event_handler)

    # Фоновые задачи
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)

    print("╔════════════════════════════════════════╗")
    print("║  ⏳ Long Polling Server запущен         ║")
    print("╠════════════════════════════════════════╣")
    print("║  http://localhost:8081                 ║")
    print("║                                        ║")
    print("║  GET  /poll?since=X&timeout=30         ║")
    print("║  POST /events                          ║")
    print("║  GET  /status                          ║")
    print("╚════════════════════════════════════════╝")

    web.run_app(app, host='localhost', port=8081)


if __name__ == "__main__":
    main()
