import socket
import tqdm
import os
import unittest

from config import SERVER_IP, SERVER_PORT


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096


class TestClient(unittest.TestCase):
    def setUp(self):
        self.sock = socket.socket()

    def testConnectToDatabase(self):
        try:
            self.sock.connect((SERVER_IP, SERVER_PORT))
        except OSError or ConnectionRefusedError:
            self.fail("THERE IS NO CONNECTION TO DB.")
    
    def testUploadFile(self):
        filename = 'testfile.txt'
        filesize = os.path.getsize(filename)
        try:
            self.sock.connect((SERVER_IP, SERVER_PORT))
        except OSError or ConnectionRefusedError:
            self.fail("THERE IS NO CONNECTION TO DB.")
        else:
            self.sock.send('upload'.encode())
            if 'receiving' in self.sock.recv(BUFFER_SIZE).decode():
                self.sock.send(f"{filename}{SEPARATOR}{filesize}".encode())
                progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(filename, "rb") as f:
                    while True:
                        bytesRead = f.read(BUFFER_SIZE)
                        if not bytesRead:
                            break
                        try:
                            self.sock.sendall(bytesRead)
                        except:
                            self.fail("FAILDE.")
                        progress.update(len(bytesRead))
                self.sock.close()
                
        
if __name__ == '__main__':
    unittest.main()
    