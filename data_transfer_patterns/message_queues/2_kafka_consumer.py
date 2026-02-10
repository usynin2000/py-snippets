"""
Apache Kafka - Consumer (Потребитель)
======================================
Чтение сообщений из Kafka топика

Особенности Consumer Groups:
- Каждая партиция читается только одним consumer в группе
- Автоматическая балансировка при добавлении/удалении consumers
- Commit offsets для надежной обработки
"""

import asyncio
from aiokafka import AIOKafkaConsumer
import json


async def consume_simple():
    """
    Простое чтение сообщений из Kafka
    """
    print("🔌 Подключаемся к Kafka как consumer...")

    consumer = AIOKafkaConsumer(
        'trading-events',  # Топик для чтения
        bootstrap_servers='localhost:9092',
        group_id='scanner-group',  # Consumer group ID
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        # Настройки:
        # auto_offset_reset='earliest'  - читать с начала
        # enable_auto_commit=True  - автоматический commit offsets
        auto_offset_reset='earliest'  # При отсутствии offset — читать с начала
    )

    await consumer.start()

    # Читаем с начала топика (игнорируем сохранённый offset группы)
    for _ in range(50):  # ждём assignment до 5 сек
        if consumer.assignment():
            await consumer.seek_to_beginning(*consumer.assignment())
            break
        await asyncio.sleep(0.1)

    try:
        print("📡 Слушаем топик 'trading-events' (с начала)...")
        print("💡 Запустите producer для отправки сообщений")
        print("-" * 50)

        count = 0

        async for message in consumer:
            count += 1

            # Метаданные сообщения
            partition = message.partition
            offset = message.offset
            timestamp = message.timestamp

            # Данные сообщения
            data = message.value

            print(f"\n📥 Сообщение #{count}")
            print(f"   📍 Partition: {partition}, Offset: {offset}")
            print(f"   📊 Тип: {data['event_type']}")
            print(f"   💰 {data['symbol']} @ ${data['price']}")
            print(f"   📦 Объем: {data['volume']}")

            # Имитация обработки
            await asyncio.sleep(0.1)

            # Ограничим для примера
            if count >= 20:
                break

        print(f"\n✅ Обработано {count} сообщений")

    finally:
        await consumer.stop()


async def consume_with_manual_commit():
    """
    Чтение с ручным commit (для надежной обработки)

    Manual commit гарантирует, что сообщение не будет "потеряно"
    если consumer упадет до завершения обработки
    """
    consumer = AIOKafkaConsumer(
        'user-events',
        bootstrap_servers='localhost:9092',
        group_id='processor-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        enable_auto_commit=False,  # Отключаем auto-commit
        auto_offset_reset='earliest'
    )

    await consumer.start()

    try:
        print("📡 Consumer с ручным commit offsets...")
        print("-" * 50)

        batch_size = 5
        processed = []

        async for message in consumer:
            data = message.value

            try:
                # Обрабатываем сообщение
                print(f"⚙️  Обработка: User {data['user_id']} → {data['action']}")

                # Имитация обработки (может упасть)
                await asyncio.sleep(0.2)

                processed.append(message)

                # Коммитим батчами для эффективности
                if len(processed) >= batch_size:
                    await consumer.commit()
                    print(f"✅ Commit: обработано {len(processed)} сообщений")
                    processed.clear()

                # Ограничим для примера
                if message.offset > 15:
                    break

            except Exception as e:
                print(f"❌ Ошибка обработки: {e}")
                # НЕ делаем commit - сообщение будет прочитано снова

        # Финальный commit оставшихся
        if processed:
            await consumer.commit()
            print(f"✅ Финальный commit: {len(processed)} сообщений")

    finally:
        await consumer.stop()


async def consume_multiple_topics():
    """
    Подписка на несколько топиков одновременно
    """
    consumer = AIOKafkaConsumer(
        bootstrap_servers='localhost:9092',
        group_id='multi-topic-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest'
    )

    # Подписываемся на несколько топиков
    consumer.subscribe(topics=['trading-events', 'user-events', 'critical-events'])

    await consumer.start()

    try:
        print("📡 Слушаем несколько топиков...")
        print("   - trading-events")
        print("   - user-events")
        print("   - critical-events")
        print("-" * 50)

        count = 0

        async for message in consumer:
            count += 1
            topic = message.topic
            data = message.value

            print(f"\n📥 [{topic}] Сообщение #{count}")
            print(f"   Данные: {data}")

            if count >= 10:
                break

    finally:
        await consumer.stop()


async def consume_with_pattern():
    """
    Подписка по паттерну (regex)

    Автоматически подписывается на все топики, соответствующие паттерну
    """
    consumer = AIOKafkaConsumer(
        bootstrap_servers='localhost:9092',
        group_id='pattern-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='latest'
    )

    # Подписка по regex паттерну
    consumer.subscribe(pattern='^.*events$')  # Все топики заканчивающиеся на 'events'

    await consumer.start()

    try:
        print("📡 Подписка по паттерну: '^.*events$'")
        print("   (все топики заканчивающиеся на 'events')")
        print("-" * 50)

        # Показываем на какие топики подписались
        await asyncio.sleep(2)
        topics = consumer.subscription()
        print(f"✅ Подписаны на топики: {topics}")

        async for message in consumer:
            print(f"📥 [{message.topic}] {message.value}")

    finally:
        await consumer.stop()


async def main():
    """
    Выбор примера
    """
    print("╔════════════════════════════════════════╗")
    print("║  🔥 Kafka Consumer - Примеры           ║")
    print("╚════════════════════════════════════════╝")
    print("\n1. Простое чтение сообщений")
    print("2. Чтение с ручным commit")
    print("3. Чтение из нескольких топиков")
    print("4. Подписка по паттерну")

    choice = input("\nВыберите пример (1-4): ").strip()

    try:
        if choice == "1":
            await consume_simple()
        elif choice == "2":
            await consume_with_manual_commit()
        elif choice == "3":
            await consume_multiple_topics()
        elif choice == "4":
            await consume_with_pattern()
        else:
            print("❌ Неверный выбор")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("\n💡 Убедитесь что:")
        print("   1. Kafka запущен")
        print("   2. Топики существуют (запустите producer)")


if __name__ == "__main__":
    asyncio.run(main())
