import socket
import tqdm
import os


BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


def acceptThread(clientSocket, address):
    print(f'[*] {address} CONNECTED TO SERVER.')
    try:
        received = clientSocket.recv(BUFFER_SIZE).decode()
    except UnicodeDecodeError:
        return
    if 'upload' in received:
        clientSocket.send('receiving'.encode())
        
        try:
            received = clientSocket.recv(BUFFER_SIZE).decode()
        except UnicodeDecodeError:
            print('[!] SOME PROBLEM WITH DECODE.')
            print('[!] KILLING PROCESS...')
            clientSocket.close()
            return
        
        filename, filesize = received.split(SEPARATOR)
        
        filename = os.path.basename(filename)
        filesize = int(filesize)
        
        progress = tqdm.tqdm(range(filesize), f"[*] Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(f'teacher/{filename}', "wb") as file:
            while True:
                bytesRead = clientSocket.recv(BUFFER_SIZE)
                if not bytesRead:    
                    break
                
                file.write(bytesRead)
                progress.update(len(bytesRead))
                
        print(f'[*] FILE FROM {address} UPLOADED.')
        
        clientSocket.close()
        print(f'[*] {address} DISCONNECTED.')
    elif 'update' in received:
        filenames = next(os.walk('teacher/'), (None, None, []))[2]
        
        if not filenames:
            clientSocket.close()
            print('[!] NO FILES IN teacher/')
            print(f'[*] {address} DISCONNECTED.')
            return
        
        for i in filenames:
            clientSocket.send((i + SEPARATOR).encode())
            
        clientSocket.close()
        print(f'[*] {address} DISCONNECTED.')
    elif 'send' in received:
        pass
    elif 'delete' in received:
        toDelete = clientSocket.recv(BUFFER_SIZE).decode()
        print(toDelete)
        toDelete = toDelete.split(SEPARATOR)
        print(toDelete)
        for i in toDelete:
            try:
                os.remove(f'teacher/{i}')
            except Exception as e:
                print(f'[!] ERROR:\n{e}')
            
        clientSocket.close()
    else:
        print(f'[*] NO MODE IN MESSAGE FROM {address}. THERE IS IT:\n{received}')
    