"""
REST API Polling - Базовый пример
==================================
Периодические HTTP запросы для получения обновлений

Преимущества:
- ✅ Максимальная простота
- ✅ Работает везде (обычный HTTP)
- ✅ Легко дебажить

Недостатки:
- ❌ Высокая латентность
- ❌ Много пустых запросов
- ❌ Не real-time
"""

import asyncio
import aiohttp
from datetime import datetime
import json


async def poll_weather_api():
    """
    Опрашиваем API погоды каждые 5 секунд

    Типичный use-case: данные обновляются редко,
    real-time не критичен
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.7558,  # Moscow
        "longitude": 37.6173,
        "current_weather": "true"
    }

    poll_interval = 5  # секунд
    request_count = 0

    print(f"🔄 Запускаем polling каждые {poll_interval}с")
    print(f"📍 URL: {url}")
    print("-" * 50)

    async with aiohttp.ClientSession() as session:
        while request_count < 10:  # Ограничим для примера
            request_count += 1
            timestamp = datetime.now().strftime("%H:%M:%S")

            try:
                print(f"\n[{timestamp}] 📤 Запрос #{request_count}...")

                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        weather = data.get("current_weather", {})

                        print(f"✅ Ответ получен:")
                        print(f"   🌡️  Температура: {weather.get('temperature')}°C")
                        print(f"   💨 Скорость ветра: {weather.get('windspeed')} km/h")
                    else:
                        print(f"❌ Ошибка: HTTP {response.status}")

                # Статистика
                print(f"📊 Выполнено запросов: {request_count}")

            except Exception as e:
                print(f"❌ Ошибка: {e}")

            # Ждем перед следующим запросом
            if request_count < 10:
                print(f"⏳ Ждем {poll_interval}с...")
                await asyncio.sleep(poll_interval)

    print("\n" + "="*50)
    print(f"✅ Завершено. Всего запросов: {request_count}")


async def poll_with_changes_detection():
    """
    Polling с определением изменений

    Более умная версия - показываем только когда данные изменились
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    poll_interval = 3
    previous_price = None

    print("💰 Мониторинг цены Bitcoin с обнаружением изменений")
    print("-" * 50)

    async with aiohttp.ClientSession() as session:
        for i in range(15):
            try:
                async with session.get(url) as response:
                    data = await response.json()
                    current_price = data["bpi"]["USD"]["rate_float"]
                    timestamp = datetime.now().strftime("%H:%M:%S")

                    # Показываем только при изменении
                    if previous_price is None:
                        print(f"[{timestamp}] 📍 Начальная цена: ${current_price:,.2f}")
                    elif current_price != previous_price:
                        change = current_price - previous_price
                        emoji = "📈" if change > 0 else "📉"
                        print(f"[{timestamp}] {emoji} Изменение: ${current_price:,.2f} ({change:+.2f})")
                    else:
                        print(f"[{timestamp}] ➖ Без изменений: ${current_price:,.2f}")

                    previous_price = current_price

            except Exception as e:
                print(f"❌ Ошибка: {e}")

            await asyncio.sleep(poll_interval)


async def main():
    """
    Выбор примера для запуска
    """
    print("╔════════════════════════════════════════╗")
    print("║   REST API Polling - Примеры          ║")
    print("╚════════════════════════════════════════╝")
    print("\n1. Базовый polling (погода)")
    print("2. Polling с обнаружением изменений (Bitcoin)")
    print()

    choice = input("Выберите пример (1 или 2): ").strip()

    if choice == "1":
        await poll_weather_api()
    elif choice == "2":
        await poll_with_changes_detection()
    else:
        print("❌ Неверный выбор")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⛔ Остановлено пользователем")
