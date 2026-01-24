"""
WebSocket - Клиент
==================
Простейший пример WebSocket клиента для двусторонней связи

Особенности:
- Устанавливает постоянное соединение
- Может отправлять и получать сообщения в любой момент
- Автоматически переподключается при разрыве
"""

import asyncio
import websockets
import json
from datetime import datetime


async def websocket_client():
    """
    Базовый WebSocket клиент
    """
    uri = "ws://localhost:8765"

    print(f"🔌 Подключаемся к {uri}...")

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Соединение установлено!")

            # Отправляем приветствие
            await websocket.send(json.dumps({
                "type": "greeting",
                "message": "Hello from client!",
                "timestamp": datetime.now().isoformat()
            }))

            # Отправляем несколько сообщений
            for i in range(5):
                message = {
                    "type": "data",
                    "counter": i,
                    "timestamp": datetime.now().isoformat()
                }

                print(f"📤 Отправляем: {message}")
                await websocket.send(json.dumps(message))

                # Ждем ответ от сервера
                response = await websocket.recv()
                print(f"📥 Получили: {response}")

                await asyncio.sleep(1)

            # Закрываем соединение
            await websocket.send(json.dumps({"type": "bye"}))
            print("👋 Соединение закрыто")

    except websockets.exceptions.ConnectionClosed:
        print("❌ Соединение разорвано")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    asyncio.run(websocket_client())
