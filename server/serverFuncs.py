import socket
import tqdm
import os


# Определяем размер буфера для сообщений и разделитель.
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"


def acceptThread(clientSocket, address):
    print(f'[*] {address} CONNECTED TO SERVER.')
    
    # Тут блок try-except, потому что иногда сервер
    # ловит неожиданные символы, которые никак нельзя интерпретировать.
    try:
        received = clientSocket.recv(BUFFER_SIZE).decode()
    except UnicodeDecodeError:
        return
    
    # Этот блок для загрузки файлов со стороны препода.
    if 'upload' in received:
        clientSocket.send('receiving'.encode())
        
        try:
            received = clientSocket.recv(BUFFER_SIZE).decode()
        except UnicodeDecodeError:
            print('[!] SOME PROBLEM WITH DECODE.')
            print('[!] KILLING PROCESS...')
            clientSocket.close()
            return
        
        # Получаем от клиента название файла, а также его размер.
        filename, filesize = received.split(SEPARATOR)
        
        # Отрезаем путь к файлу, оставляя только название и преобразуем размер.
        filename = os.path.basename(filename)
        filesize = int(filesize)
        
        # Создаем красивый прогрессбар.
        progress = tqdm.tqdm(range(filesize), f"[*] Receiving {filename}",
                             unit="B", unit_scale=True, unit_divisor=1024)
        
        # Создаем файл в виде потока байтов, чтобы сохранить его в целости.
        with open(f'teacher/{filename}', "wb") as file:
            while True:
                try:
                    bytesRead = clientSocket.recv(BUFFER_SIZE)
                except Exception as e:
                    print(f'[!] SOME ERROR OCCUPIED:\n{e}')
                if not bytesRead:    
                    break
                
                file.write(bytesRead)
                progress.update(len(bytesRead))
                
        print(f'[*] FILE FROM {address} UPLOADED.')
        
        clientSocket.close()
        print(f'[*] {address} DISCONNECTED.')
    
    # Этот блок для обновления странички заданий на стороне препода.
    # Вызывается каждый раз, когда заходим на страничку
    # для автоматического ее обновления.
    elif 'update' in received:
        # Тут мы просто берем все файлы в директории и отправляем клиенту.
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
    
    # Этот блок для обновления странички заданий на стороне студента.
    # Тоже вызывается каждый раз, когда заходим на страницу.
    # Мы не используем метод update, потому что метод updateStud
    # должен делать еще что-то, но я пока забыл, что именно.
    elif 'updateStud' in received:
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
        """file = clientSocket.recv(BUFFER_SIZE).decode()
        
        path = 'teacher/' + file
        filesize = os.path.getsize(path)
        
        fileinfo = file + SEPARATOR + str(filesize)
        
        clientSocket.send(fileinfo.encode())
        
        with open(path, "rb") as file:
            while True:
                bytes_read = file.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                clientSocket.send(bytes_read)"""
    
    # Этот метод для удаления файлов, загруженных преподом.
    # Просто получает список файлов для удаления и удаляет.
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
    