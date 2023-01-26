import kivy
kivy.require('2.1.0')

from kivymd.uix.screen import MDScreen

import config


class SettingsScreenTeacher(MDScreen):
    """Класс для страницы настроек.
    """
    def updateIP(self):
        """Метод для обновления IP-адреса в файле config.py.
        """
        ip = self.ids.ip.text
        if not ip:
            return
        
        config.SERVER_IP = ip
        
    def openMainTeacher(self):
        """Данный метод открывает главную страницу.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'mainTeacher'
        
    def openCalendarTeacher(self):
        """Данный метод открывает страницу календаря.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendarTeacher'
        
    def openTasksTeacher(self):
        """Данный метод открывает страницу с заданиями.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasksTeacher'
        
    def logout(self):
        """Данный метод открывает страницу логина.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettingsTeacher(self):
        """Данный метод открывает страницу настроек.
        """
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settingsTeacher'
    
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
        