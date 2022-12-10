import os
import socket

import kivy
kivy.require('2.1.0')
try:
    from android.storage import primary_external_storage_path
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
except ModuleNotFoundError:
    pass
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.selection.selection import SelectionItem
from kivymd.uix.snackbar import Snackbar


class TasksScreenTeacher(MDScreen):
    def update(self):
        while self.ids.tasksTeacher.children:
            for i in self.ids.tasksTeacher.children:
                self.ids.tasksTeacher.remove_widget(i)
            
        self.separator = "<SEPARATOR>"
        self.bufferSize = 4096
        self.host = "192.168.1.120"
        self.port = 55555
        
        sock = socket.socket()
        try:
            sock.connect((self.host, self.port))
        except OSError:
            sock.close()
            Snackbar(text="Нет подключения к серверу...", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()
            return
        sock.send('update'.encode())
        _received = ''
        while True:
            received = sock.recv(self.bufferSize).decode()
            if not received:
                _received = _received.split(self.separator)
                for i in _received:
                    self.ids.tasksTeacher.add_widget(OneLineIconListItem(text=i))
                break
            _received += received
        sock.close()
      
    def addTask(self):
        self.separator = "<SEPARATOR>"
        self.bufferSize = 4096
        self.host = "192.168.1.120"
        self.port = 55555
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
    
    def deleteItems(self, instance_selection_list):
        self.separator = "<SEPARATOR>"
        self.bufferSize = 4096
        self.host = "192.168.1.120"
        self.port = 55555
        
        sock = socket.socket()
        try:
            sock.connect((self.host, self.port))
        except OSError:
            sock.close()
            Snackbar(text="Нет подключения к серверу...", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()
            return
        sock.send('delete'.encode())
        message = ''
        for i in instance_selection_list.get_selected_list_items():
            message += str(i.children[1].text)
            message += self.separator
        sock.sendall(message.encode())
        sock.close()
        
        self.update()
        
    def setSelectionMode(self, instance_selection_list, mode):
        if mode:
            left_action_items = [
                [
                    "close",
                    lambda x: self.ids.tasksTeacher.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can", lambda x: self.deleteItems(instance_selection_list)]]
        else:
            left_action_items = [["menu", lambda x: self.ids.nav_drawer.set_state("open")]]
            right_action_items = []
            self.ids.toolbar.title = "Электронная среда - преподаватель"

        self.ids.toolbar.left_action_items = left_action_items
        self.ids.toolbar.right_action_items = right_action_items

    def onSelected(self, instance_selection_list, instance_selection_item):
        self.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def onUnselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )

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
        