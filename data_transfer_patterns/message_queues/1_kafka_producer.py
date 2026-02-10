"""
Apache Kafka - Producer (Производитель)
========================================
Отправка сообщений в Kafka топик

Особенности:
- ✅ High throughput (миллионы сообщений/сек)
- ✅ Persistence (сообщения хранятся на диске)
- ✅ Replay capability (можно перечитать старые сообщения)
- ✅ Horizontal scaling

Требования:
pip install aiokafka

Запуск Kafka (Docker):
docker run -d -p 9092:9092 apache/kafka:latest
"""

import asyncio
from aiokafka import AIOKafkaProducer
import json
from datetime import datetime
import random


async def send_messages_simple():
    """
    Простая отправка сообщений в Kafka
    """
    print("🚀 Подключаемся к Kafka...")

    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        # Дополнительные настройки:
        # acks='all'  - ждать подтверждения от всех реплик
        # compression_type='gzip'  - сжатие данных
        # max_batch_size=16384  - размер батча
    )

    await producer.start()

    try:
        topic = 'trading-events'

        print(f"📤 Отправляем сообщения в топик '{topic}'...")
        print("-" * 50)

        for i in range(10):
            # Создаем сообщение
            message = {
                "event_id": i + 1,
                "event_type": random.choice(["trade", "quote", "order"]),
                "symbol": random.choice(["AAPL", "GOOGL", "MSFT", "TSLA"]),
                "price": round(random.uniform(100, 500), 2),
                "volume": random.randint(1, 1000),
                "timestamp": datetime.now().isoformat()
            }

            # Отправляем в Kafka
            await producer.send(topic, message)

            print(f"✅ Отправлено #{i + 1}: {message['event_type']} "
                  f"{message['symbol']} @ ${message['price']}")

            await asyncio.sleep(0.5)

        # Ждем пока все сообщения будут отправлены
        await producer.flush()
        print("\n📊 Все сообщения отправлены!")

    finally:
        await producer.stop()


async def send_with_partitioning():
    """
    Отправка с использованием партиций (partitioning)

    Партиции позволяют:
    - Распределять нагрузку между consumers
    - Гарантировать порядок сообщений внутри партиции
    - Масштабировать обработку
    """
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    await producer.start()

    try:
        topic = 'user-events'

        print("📤 Отправка с партиционированием по user_id...")
        print("-" * 50)

        # Отправляем события от разных пользователей
        for i in range(20):
            user_id = random.randint(1, 5)

            message = {
                "user_id": user_id,
                "action": random.choice(["login", "logout", "purchase", "view"]),
                "timestamp": datetime.now().isoformat()
            }

            # Используем user_id как ключ для партиционирования
            # Все сообщения с одинаковым ключом попадут в одну партицию
            key = str(user_id).encode('utf-8')

            metadata = await producer.send_and_wait(
                topic,
                value=message,
                key=key
            )

            # metadata содержит информацию о партиции и offset
            partition = metadata.partition
            offset = metadata.offset

            print(f"✅ User {user_id}: {message['action']} "
                  f"→ partition {partition}, offset {offset}")

            await asyncio.sleep(0.3)

        await producer.flush()

    finally:
        await producer.stop()


async def send_with_error_handling():
    """
    Отправка с обработкой ошибок и retry
    """
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        # Настройки надежности:
        acks='all',  # Ждем подтверждения от всех реплик
        request_timeout_ms=10000,  # Таймаут запроса (retry до истечения)
        retry_backoff_ms=500,  # Пауза между повторными попытками
    )

    await producer.start()

    try:
        topic = 'critical-events'

        success_count = 0
        error_count = 0

        for i in range(10):
            message = {
                "id": i + 1,
                "critical_data": f"Important message #{i + 1}",
                "timestamp": datetime.now().isoformat()
            }

            try:
                # send_and_wait() ждет подтверждения
                metadata = await producer.send_and_wait(topic, message)

                print(f"✅ Сообщение #{i + 1} доставлено: "
                      f"partition={metadata.partition}, offset={metadata.offset}")
                success_count += 1

            except Exception as e:
                print(f"❌ Ошибка отправки сообщения #{i + 1}: {e}")
                error_count += 1

            await asyncio.sleep(0.5)

        print(f"\n📊 Статистика:")
        print(f"   ✅ Успешно: {success_count}")
        print(f"   ❌ Ошибок: {error_count}")

    finally:
        await producer.stop()


async def main():
    """
    Выбор примера
    """
    print("╔════════════════════════════════════════╗")
    print("║  🔥 Kafka Producer - Примеры           ║")
    print("╚════════════════════════════════════════╝")
    print("\n1. Простая отправка сообщений")
    print("2. Отправка с партиционированием")
    print("3. Отправка с обработкой ошибок")

    choice = input("\nВыберите пример (1-3): ").strip()

    try:
        if choice == "1":
            await send_messages_simple()
        elif choice == "2":
            await send_with_partitioning()
        elif choice == "3":
            await send_with_error_handling()
        else:
            print("❌ Неверный выбор")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("\n💡 Убедитесь что Kafka запущен:")
        print("   docker run -d -p 9092:9092 apache/kafka:latest")


if __name__ == "__main__":
    asyncio.run(main())
