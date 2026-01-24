import asyncio
from datetime import datetime

import websockets

# Set of all connected clients
connected_clients = set()


async def broadcast_message(message: str, sender=None):
    """
    Send messages to all connected clilents
    """
    if connected_clients:
        # Creating task for every client
        tasks = [
            client.send(message)
            for client in connected_clients
            if client != sender  # Not sending to sender
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)
        # Log any errors that occurred during broadcast
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                print(f"Error broadcasting to client {i}: {result}")


async def handle_client(websocket, path):
    """
    Handler for every client of chat
    """

    connected_clients.add(websocket)
    client_id = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"

    print(f"Client is connected: {client_id}")
    print(f"All clients: {len(connected_clients)}")

    # Notify all about new member
    await broadcast_message(
        f"[{datetime.now().strftime('%H:%M:%S')}] User {client_id} added to chat",
        sender=websocket,
    )

    try:
        async for message in websocket:
            print(f"Received message from {client_id}: {message}")  # Debug log
            timestamp = datetime.now().strftime("%H:%M:%S")
            formatted_message = f"[{timestamp}] {client_id}: {message}"

            # sending messages to all clients
            await broadcast_message(formatted_message, sender=websocket)
            print(f"Broadcasted message to {len(connected_clients) - 1} clients")  # Debug log
    except websockets.exceptions.ConnectionClosed:
        print(f"Client is disconnected: {client_id}")
    except Exception as e:
        print(f"Error handling client {client_id}: {e}")  # Debug log
        raise
    finally:
        connected_clients.discard(websocket)
        print(f"All clients: {len(connected_clients)}")

        # Only broadcast if there are other clients left
        if connected_clients:
            await broadcast_message(
                f"[{datetime.now().strftime('%H:%M:%S')}] User {client_id} left chat"
            )


async def main():
    print("Setting up chat-server ws://localhost:8765")
    print("Connect many client for testing")

    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())

#  2. Чат с несколькими клиентами
# Терминал 1 (Сервер):
# python websocket/3_chat_example.py

# Терминал 2, 3, 4... (Клиенты):
# Можно использовать простой клиент или подключиться через браузер:
# const ws = new WebSocket('ws://localhost:8765');
# ws.onmessage = (event) => console.log(event.data);
# ws.send('Привет из браузера!');
