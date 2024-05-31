import socket


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_server.bind(('127.0.0.1', 8000))
socket_server.listen()
socket_server.setblocking(False)


connections = []


try:
    while True:
        try:
            connection, client_address = socket_server.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass

        for connect in connections:

            try:
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
            except BlockingIOError:
                pass
finally:
    socket_server.close()