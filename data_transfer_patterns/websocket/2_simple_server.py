"""
WebSocket - Сервер
==================
Простейший WebSocket сервер для обработки подключений

Особенности:
- Принимает множественные подключения
- Отправляет данные клиентам в режиме реального времени
- Обрабатывает разрывы соединений
"""

import asyncio
import websockets
import json
from datetime import datetime


# Множество всех подключенных клиентов
connected_clients = set()


async def handle_client(websocket, path):
    """
    Обработчик для каждого подключенного клиента
    """
    # Добавляем клиента в список
    connected_clients.add(websocket)
    client_id = id(websocket)

    print(f"✅ Новое подключение: Client#{client_id}")
    print(f"📊 Всего клиентов: {len(connected_clients)}")

    try:
        # Отправляем приветственное сообщение
        await websocket.send(json.dumps({
            "type": "welcome",
            "client_id": client_id,
            "message": "Добро пожаловать на WebSocket сервер!",
            "timestamp": datetime.now().isoformat()
        }))

        # Слушаем сообщения от клиента
        async for message in websocket:
            print(f"📥 От Client#{client_id}: {message}")

            # Парсим JSON
            try:
                data = json.loads(message)
                msg_type = data.get("type", "unknown")

                # Обрабатываем разные типы сообщений
                if msg_type == "bye":
                    await websocket.send(json.dumps({
                        "type": "farewell",
                        "message": "До свидания! 👋"
                    }))
                    break

                # Эхо-ответ с меткой времени
                response = {
                    "type": "echo",
                    "original": data,
                    "server_timestamp": datetime.now().isoformat(),
                    "processed_by": f"Server#{client_id}"
                }

                await websocket.send(json.dumps(response, indent=2))

            except json.JSONDecodeError:
                # Если не JSON, просто отправляем обратно
                await websocket.send(f"Echo: {message}")

    except websockets.exceptions.ConnectionClosed:
        print(f"❌ Client#{client_id} отключился")

    finally:
        # Удаляем клиента из списка
        connected_clients.discard(websocket)
        print(f"📊 Осталось клиентов: {len(connected_clients)}")


async def broadcast_task():
    """
    Периодическая рассылка данных всем клиентам (опционально)
    """
    counter = 0
    while True:
        await asyncio.sleep(10)  # Каждые 10 секунд

        if connected_clients:
            counter += 1
            message = json.dumps({
                "type": "broadcast",
                "counter": counter,
                "message": f"Рассылка #{counter} всем клиентам",
                "timestamp": datetime.now().isoformat()
            })

            print(f"📢 Рассылка {len(connected_clients)} клиентам")

            # Отправляем всем подключенным клиентам
            await asyncio.gather(
                *[client.send(message) for client in connected_clients],
                return_exceptions=True
            )


async def main():
    """
    Запуск WebSocket сервера
    """
    host = "localhost"
    port = 8765

    print(f"🚀 Запускаем WebSocket сервер на ws://{host}:{port}")

    # Запускаем сервер и задачу рассылки параллельно
    async with websockets.serve(handle_client, host, port):
        # Запускаем фоновую задачу для broadcast
        broadcast = asyncio.create_task(broadcast_task())

        # Держим сервер запущенным
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⛔ Сервер остановлен")
