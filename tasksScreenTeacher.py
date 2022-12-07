import os
import socket

import kivy
kivy.require('2.1.0')

from android.storage import primary_external_storage_path
from android.permissions import request_permissions, Permission
request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar


class TasksScreenTeacher(MDScreen):
    def update(self):
        separator = "<SEPARATOR>"
        bufferSize = 4096
        host = "0.0.0.0"
        port = 5555
        
    def addTask(self):
        self.separator = "<SEPARATOR>"
        self.bufferSize = 4096
        self.host = "192.168.1.120"
        self.port = 5555
        self.path = ''
        
        self.managerDead = False
        self.fileManager = MDFileManager(
            exit_manager=self.exitManager, select_path=self.selectPath
        )
        self.fileManager.show(primary_external_storage_path())
                        
    def selectPath(self, path: str):
        self.path = path
        self.exitManager()

    def exitManager(self, *args):
        self.managerDead = True
        self.fileManager.close()
        if self.managerDead and self.path:
            filesize = os.path.getsize(self.path)
            sock = socket.socket()
            try:
                sock.connect((self.host, self.port))
            except OSError:
                sock.close()
                Snackbar(text="Нет подключения к серверу...", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()
                return
            sock.send('upload'.encode())
            if 'receiving' in sock.recv(self.bufferSize).decode():
                sock.send(f"{os.path.split(self.path)[1]}{self.separator}{filesize}".encode())
                # progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                with open(self.path, "rb") as file:
                    while True:
                        bytes_read = file.read(self.bufferSize)
                        if not bytes_read:
                            break
                        sock.sendall(bytes_read)
                        # progress.update(len(bytes_read))
                sock.close()
            
            Snackbar(text="Файл успешно загружен.", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()

    def openMainTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'mainTeacher'
        
    def openCalendarTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendarTeacher'
        
    def openTasksTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasksTeacher'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettingsTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settingsTeacher'
        