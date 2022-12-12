import kivy
kivy.require('2.1.0')
import socket

try:
    from android.storage import primary_external_storage_path
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
except ModuleNotFoundError:
    pass

from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from config import SERVER_IP, SERVER_PORT


class TasksScreen(MDScreen):
    def update(self):
        """Метод для автоматического обновления страницы при заходе на нее.
        """
        while self.ids.tasksStud.children:
            for i in self.ids.tasksStud.children:
                self.ids.tasksStud.remove_widget(i)
                
        separator = "<SEPARATOR>"
        bufferSize = 4096
        host = SERVER_IP
        port = SERVER_PORT
        
        sock = socket.socket()
        
        try:
            sock.connect((host, port))
        except OSError:
            sock.close()
            Snackbar(text="Нет подключения к серверу...",
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     size_hint_x= \
                     (Window.width - (10 * 2)) / Window.width).open()
            return
        
        sock.send('updateStud'.encode())
        
        received = ''
        while True:
            _received = sock.recv(bufferSize).decode()
            if not received:
                _received = _received.split(separator)
                for i in _received:
                    self.ids.tasksStud.add_widget(MDExpansionPanel(
                        content=MDBoxLayout(
                            MDRaisedButton(
                                text='Добавить ответ на задание',
                                on_press=self.sendAnswer(i)
                            ),
                            MDRaisedButton(
                                text='Загрузить задание',
                                on_press=self.loadTask(i)
                            ),
                            spacing="10dp",
                            orientation="vertical",
                            adaptive_height=True
                        ),
                        panel_cls=MDExpansionPanelOneLine(
                            text=i
                        ),
                    ))
                break
            _received += received
        sock.close()
    
    def sendAnswer(self, task):
        """Метод для отправки ответа на задание.
        """
        pass
    
    def loadTask(self, task):
        pass
        """Метод для загрузки задания от преподавателя.
        """
        
        # ОНО ВИСНЕТ. ПОТОМ РАЗБЕРУСЬ.
        """separator = "<SEPARATOR>"
        bufferSize = 4096
        host = SERVER_IP
        port = SERVER_PORT
        
        sock = socket.socket()
        
        try:
            sock.connect((host, port))
        except OSError:
            sock.close()
            Snackbar(text="Нет подключения к серверу...",
                     snackbar_x="10dp", snackbar_y="10dp",
                     size_hint_x= \
                         (Window.width - (10 * 2)) / Window.width).open()
            return
        
        sock.send('send'.encode())
        sock.send(task.encode())
        
        fileinfo = sock.recv(bufferSize).decode().split(separator)
        
        with open(f'{primary_external_storage_path()}/{fileinfo[0]}', "wb") as file:
            while True:
                bytesRead = sock.recv(bufferSize)
                if not bytesRead:    
                    break
                
                file.write(bytesRead)"""
                        
    
    def openMain(self):
        """Данный метод открывает главную страницу.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'main'
        
    def openCalendar(self):
        """Данный метод открывает страницу календаря.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendar'
        
    def openTasks(self):
        """Данный метод открывает страницу с заданиями.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasks'
        
    def logout(self):
        """Данный метод открывает страницу логина.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'
        
    def openSettings(self):
        """Данный метод открывает страницу настроек.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settings'
        