import socket
import sys
import threading


SERVER_HOST = "0.0.0.0" # Берем айпишник нашего ПК и используем
                        # в качестве айпи для подключенияю
SERVER_PORT = 55556


sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))

print(f'[*] SERVER STARTED ON {SERVER_HOST}:{SERVER_PORT}.')

clients = []
def receive(client: socket.socket, address):
    while True:
        try:
            message = client.recv(4096).decode()
        except:
            continue
        else:
            for _client in clients:
                try:
                    _client.send(message.encode())
                except:
                    pass

# Допускается до 5-ти клиентов одновременно.
# При большем количестве - меняем цифру в listen().
sock.listen(5)
while True:
    try:
        clientSocket, address = sock.accept()
        clients.append(clientSocket)
        # Принимаем подключение и пихаем в отдельный поток.
        acceptingThread = threading.Thread(target=receive, daemon=True,
                                           args=(clientSocket, address))
        acceptingThread.start()
        
    # При CTRL-C завершаем работу сервера.
    except KeyboardInterrupt:
        print(f'[!] SERVER TERMINATED.')
        sys.exit(0)
        