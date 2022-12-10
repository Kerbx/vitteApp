import socket
import sys
import threading
import os

from serverFuncs import acceptThread


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 55555


sock = socket.socket()
sock.bind((SERVER_HOST, SERVER_PORT))

print(f'[*] SERVER STARTED ON {SERVER_HOST}:{SERVER_PORT}.')

sock.listen(5)
while True:
    try:
        clientSocket, address = sock.accept()
        acceptingThread = threading.Thread(target=acceptThread, daemon=True, args=(clientSocket, address))
        acceptingThread.start()
    except KeyboardInterrupt:
        print(f'[!] SERVER TERMINATED.')
        sys.exit(0)
        