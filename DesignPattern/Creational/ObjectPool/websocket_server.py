import asyncio

import websockets


async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Echo: {message}")


async def start_server():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket server started on ws://localhost:8765")

    await server.wait_closed()


def main() -> None:
    asyncio.run(start_server())


if __name__ == '__main__':
    main()
