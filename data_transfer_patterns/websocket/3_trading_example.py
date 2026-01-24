import asyncio
import websockets
import json
from datetime import datetime


# ============================================================================
# 1. Echo сервер - просто возвращает то, что вы отправили
# ============================================================================
async def test_echo_server():
    """
    Публичный echo сервер - возвращает ваши сообщения обратно
    """
    uri = "wss://echo.websocket.org"

    print("=" * 60)
    print("1. Тестирование Echo сервера (wss://echo.websocket.org)")
    print("=" * 60)

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Подключено к echo серверу!")

            messages = ["Привет!", "WebSocket работает!", "Тест 123"]

            for msg in messages:
                await websocket.send(msg)
                print(f"📤 Отправлено: {msg}")

                response = await websocket.recv()
                print(f"📥 Получено: {response}")
                print()

                await asyncio.sleep(1)

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    print("\n")


# ============================================================================
# 2. WebSocket.org тестовый сервер
# ============================================================================
async def test_websocket_org():
    """
    Официальный тестовый сервер от websocket.org
    """
    uri = "wss://ws.ifelse.io"

    print("=" * 60)
    print("2. Тестирование WebSocket.org сервера (wss://ws.ifelse.io)")
    print("=" * 60)

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Подключено!")

            # Отправляем сообщение
            await websocket.send("Hello from Python!")
            print("📤 Отправлено: Hello from Python!")

            # Получаем ответ
            response = await websocket.recv()
            print(f"📥 Получено: {response}")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    print("\n")


# ============================================================================
# 3. Coinbase WebSocket API - реальные цены криптовалют
# ============================================================================
async def test_coinbase_websocket():
    """
    Coinbase WebSocket API - получаем реальные цены криптовалют
    """
    uri = "wss://ws-feed.exchange.coinbase.com"

    print("=" * 60)
    print("3. Подключение к Coinbase WebSocket API")
    print("=" * 60)

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Подключено к Coinbase!")

            # Подписываемся на тикер BTC-USD
            subscribe_message = {
                "type": "subscribe",
                "product_ids": ["BTC-USD", "ETH-USD"],
                "channels": ["ticker"]
            }

            await websocket.send(json.dumps(subscribe_message))
            print("📤 Подписка на BTC-USD и ETH-USD отправлена")
            print("⏳ Ожидание данных (10 секунд)...\n")

            # Получаем данные в течение 10 секунд
            timeout = 10
            start_time = asyncio.get_event_loop().time()

            while (asyncio.get_event_loop().time() - start_time) < timeout:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    data = json.loads(message)

                    if data.get("type") == "ticker":
                        product = data.get("product_id", "N/A")
                        price = data.get("price", "N/A")
                        time = data.get("time", "N/A")
                        print(f"💰 {product}: ${price} (время: {time})")

                except asyncio.TimeoutError:
                    continue

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    print("\n")


# ============================================================================
# 4. Binance WebSocket API - еще один крипто-сервис
# ============================================================================
async def test_binance_websocket():
    """
    Binance WebSocket API - получаем цены криптовалют
    """
    # Публичный WebSocket endpoint для тикера BTCUSDT
    uri = "wss://stream.binance.com:9443/ws/btcusdt@ticker"

    print("=" * 60)
    print("4. Подключение к Binance WebSocket API")
    print("=" * 60)

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Подключено к Binance!")
            print("⏳ Получение данных о BTC/USDT (10 секунд)...\n")

            timeout = 10
            start_time = asyncio.get_event_loop().time()
            message_count = 0

            while (asyncio.get_event_loop().time() - start_time) < timeout:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    data = json.loads(message)

                    if "c" in data:  # текущая цена
                        price = data["c"]
                        volume = data.get("v", "N/A")
                        high_24h = data.get("h", "N/A")
                        low_24h = data.get("l", "N/A")

                        message_count += 1
                        print(f"📊 Сообщение #{message_count}")
                        print(f"   💰 Цена BTC/USDT: ${price}")
                        print(f"   📈 Макс за 24ч: ${high_24h}")
                        print(f"   📉 Мин за 24ч: ${low_24h}")
                        print(f"   📦 Объем: {volume}")
                        print()

                except asyncio.TimeoutError:
                    continue

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    print("\n")


# ============================================================================
# 5. WebSocket тестовый сервер с разными типами сообщений
# ============================================================================
async def test_websocket_test_server():
    """
    Другой публичный тестовый сервер
    """
    uri = "wss://socketsbay.com/wss/v2/1/demo/"

    print("=" * 60)
    print("5. Тестирование SocketsBay сервера")
    print("=" * 60)

    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Подключено!")

            # Отправляем тестовое сообщение
            test_message = {
                "message": "Hello from Python!",
                "timestamp": datetime.now().isoformat()
            }

            await websocket.send(json.dumps(test_message))
            print(f"📤 Отправлено: {test_message}")

            # Ждем ответ
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                print(f"📥 Получено: {response}")
            except asyncio.TimeoutError:
                print("⏱️  Таймаут ожидания ответа")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    print("\n")


# ============================================================================
# Главная функция для запуска всех тестов
# ============================================================================
async def main():
    """
    Запуск всех тестов подключения к публичным WebSocket серверам
    """
    print("\n" + "=" * 60)
    print("🌐 ТЕСТИРОВАНИЕ ПУБЛИЧНЫХ WEBSOCKET СЕРВЕРОВ")
    print("=" * 60 + "\n")

    # Список тестов (можно закомментировать ненужные)
    tests = [
        ("Echo сервер", test_echo_server),
        ("WebSocket.org", test_websocket_org),
        ("Coinbase API", test_coinbase_websocket),
        ("Binance API", test_binance_websocket),
        ("SocketsBay", test_websocket_test_server),
    ]

    for name, test_func in tests:
        try:
            await test_func()
            await asyncio.sleep(2)  # Пауза между тестами
        except KeyboardInterrupt:
            print("\n\n⚠️  Тестирование прервано пользователем")
            break
        except Exception as e:
            print(f"❌ Ошибка при тестировании {name}: {e}\n")

    print("=" * 60)
    print("✅ Тестирование завершено!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
