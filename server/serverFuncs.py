import socket
import tqdm
import os


BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


def acceptThread(clientSocket, address):
    print(f'[*] {address} CONNECTED TO SERVER.')
    received = clientSocket.recv(BUFFER_SIZE).decode()
    
    if 'upload' in received:
        clientSocket.send('receiving'.encode())
        received = clientSocket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)
        
        filename = os.path.basename(filename)
        filesize = int(filesize)
        
        progress = tqdm.tqdm(range(filesize), f"[*] Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(f'teacher/{filename}', "wb") as file:
            while True:
                bytesRead = clientSocket.recv(BUFFER_SIZE)
                print(bytesRead)
                if not bytesRead:    
                    break
                file.write(bytesRead)
                progress.update(len(bytesRead))
        print(f'[*] FILE FROM {address} UPLOADED.')
        
        clientSocket.close()
        print(f'[*] {address} DISCONNECTED.')
    elif 'send' in received:
        pass
    else:
        print(f'[*] NO MODE IN MESSAGE FROM {address}. THERE IS IT:\n{received}')
    