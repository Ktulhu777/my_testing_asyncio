import socket 
import asyncio
from asyncio import AbstractEventLoop

async def echo(connection: socket,
                loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024):
        if data == b'boom\r\n':
            raise Exception("Неожиданная ошибка сети")
        await loop.sock_sendall(connection, data)


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, client_data = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {client_data}")
        asyncio.create_task(echo(connection=connection,
                                 loop=loop))
        

async def main():
    server_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.setblocking(False)
    server_socket.bind(("127.0.0.1", 8000))
    server_socket.listen()

    await listen_for_connection(server_socket=server_socket,
                                loop=asyncio.get_event_loop())
    
if __name__ == "__main__":
    asyncio.run(main())