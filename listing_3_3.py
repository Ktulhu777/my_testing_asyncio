import socket


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
socket_server.bind(server_address)
socket_server.listen()


connections = []

try:
    while True:
        connection, client_address = socket_server.accept()
        print(f'Получен запрос на подключение от {client_address}!')
        connections.append(connection)

        for connect in connections:
            buffer = b""

            while buffer[-2:] != b"\r\n":
                data = connection.recv(10)
                if not data:
                    break
                else:
                    print(f'Получены данные: {data}!')
                    buffer = buffer + data
            print(f"Все данные: {buffer}")
            connection.send(buffer)
finally:
    socket_server.close()