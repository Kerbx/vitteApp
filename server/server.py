import socket
import sys
import threading

from serverFuncs import acceptThread


SERVER_HOST = "0.0.0.0" # Берем айпишник нашего ПК и используем
                        # в качестве айпи для подключенияю
SERVER_PORT = 55555


sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))

print(f'[*] SERVER STARTED ON {SERVER_HOST}:{SERVER_PORT}.')

# Допускается до 5-ти клиентов одновременно.
# При большем количестве - меняем цифру в listen().
sock.listen(5)
while True:
    try:
        clientSocket, address = sock.accept()
        
        # Принимаем подключение и пихаем в отдельный поток.
        acceptingThread = threading.Thread(target=acceptThread, daemon=True,
                                           args=(clientSocket, address))
        acceptingThread.start()
        
    # При CTRL-C завершаем работу сервера.
    except KeyboardInterrupt:
        print(f'[!] SERVER TERMINATED.')
        sys.exit(0)
        