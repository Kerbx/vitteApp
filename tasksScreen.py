import kivy
kivy.require('2.1.0')
import socket

from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar


class TasksScreen(MDScreen):
    def update(self):
        while self.ids.tasksStud.children:
            for i in self.ids.tasksStud.children:
                self.ids.tasksStud.remove_widget(i)
                
        separator = "<SEPARATOR>"
        bufferSize = 4096
        host = "192.168.1.120"
        port = 55555
        
        sock = socket.socket()
        
        try:
            sock.connect((host, port))
        except OSError:
            Snackbar(text="Нет подключения к серверу...", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()

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
        pass
    
    def loadTask(self, task):
        pass
    
    def openMain(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'main'
        
    def openCalendar(self):
        self.manager.current = 'calendar'
        self.ids.nav_drawer.set_state("close")
        
    def openTasks(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasks'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettings(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settings'
        