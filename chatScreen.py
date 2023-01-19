import kivy
kivy.require('2.1.0')
import socket
import threading

from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from config import SERVER_IP, SERVER_PORT_CHAT


user = open('login.txt').read().split('\n')


def updateMessage(selfObj):
    sock = socket.socket()
    try:
        sock.settimeout(3)
        sock.connect((SERVER_IP, SERVER_PORT_CHAT))
    except OSError or TimeoutError:
        sock.close()
        return
    while True:
        try:
            message = sock.recv(4096).decode()
        except:
            continue
        else:
            selfObj.ids.chat.text += f'\n{message}'
        

class ChatScreen(MDScreen):
    def on_enter(self):
        self.process = threading.Thread(target=updateMessage, args=(self,))
        self.process.start()
        
    def on_leave(self):
        del self.process
        
    def sendMessage(self):
        text = self.ids.message.text
        self.ids.message.text = ''
        
        name = user[0]
        
        message = f"{name}: {text}"
        
        sock = socket.socket()
        try:
            sock.settimeout(3)
            sock.connect((SERVER_IP, SERVER_PORT_CHAT))
        except OSError or TimeoutError:
            sock.close()
            Snackbar(text="Нет подключения к серверу...",
                        snackbar_x="10dp",
                        snackbar_y="10dp",
                        size_hint_x= \
                            (Window.width - (10 * 2)) / Window.width).open()
            return
        
        sock.send(message.encode())
        
    def openMain(self):
        """Данный метод открывает главную страницу.
        """
        if user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'mainTeacher'
        else:
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'main'
        
    def openCalendar(self):
        """Данный метод открывает страницу календаря.
        """
        if user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'calendarTeacher'
        else:
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'calendar'
        
    def openTasks(self):
        """Данный метод открывает страницу с заданиями.
        """
        if user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'tasksTeacher'
        else:
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
        if user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'settingsTeacher'
        else:
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'settings'
            
    def openHelp(self):
        """Данный метод открывает страницу помощи.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'help'
        
    def openFAQ(self):
        """Данный метод открывает FAQ
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'faq'
    
    def openNews(self):
        """Данный метод открывает страницу новостей
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'news'
        
    def openChat(self):
        """Данный метод открывает страницу чата
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'chat'
        