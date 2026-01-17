import asyncio
import websockets

async def client():
    """
    Simple WebSocket client
    """
    uri = "ws://localhost:8765"

    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to server!")

            # Getting greeting message
            gretting = await websocket.recv()
            print(f"Server: {gretting}")

            messages = ["Hello!", "How is it going?", "WebSocket works!"]

            for msg in messages:
                await websocket.send(msg)
                print(f"Sent: {msg}")

                # Getting resposne
                response = await websocket.recv()
                print(f"Server: {response}")

                await asyncio.sleep(1) # Small pause between messages
            
            # Sending command to exit
            await websocket.send("exit")
            print("Disclosing")
    except websocket.exceptions.ConnectionRefusedError:
        print("Error: Server is unavailble. Be sure that server is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(client())