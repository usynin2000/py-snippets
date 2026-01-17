import asyncio
import websockets
from datetime import datetime

async def handle_client(websocket, path):
    """
    Handler for every connected client
    """
    print(f"New connection: {websocket.remote_address}")

    try:
        ## Send greeting message
        await websocket.send("Welcome to WebSocket server")

        # Listen messages from client
        async for message in websocket:
            print(f"Got from a client: {message}")

            # Echo-resposne with timestamp
            response = f"[{datetime.now().strftime("%H:%M:%S")}] Echo {message}"
            await websocket.send(response)

            # If client send "exit", closing connection
            if message.lower() == "exit":
                await websocket.send("Bie!")
                break
    except websocket.exceptions.ConnectionClosed:
        print(f"Client {websocket.remote_address} disconnected.")
    except Exception as e:
        print(f"Error: {e}")
    finally: 
        print(f"Connection with {websocket.remote_address} is closed.")

async def main():
    print("Setting up Websocket server on ws://localhost:8765")
    print("For connection use client or browser!")

    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()

        # asyncio.Future() без параметров создаёт объект Future, который никогда не завершится
        # await на такой Future будет ждать вечно
        # Это нужно, чтобы сервер не остановился сразу после запуска


if __name__ == "__main__":
    asyncio.run(main())