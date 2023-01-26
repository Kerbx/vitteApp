import kivy
kivy.require('2.1.0')

from kivymd.uix.screen import MDScreen


class HelpScreen(MDScreen):
    def on_enter(self, *args):
        self.user = open('login.txt').read().split('\n')
        
    def openMain(self):
        """Данный метод открывает главную страницу.
        """
        if self.user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'mainTeacher'
        else:
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'main'
        
    def openCalendar(self):
        """Данный метод открывает страницу календаря.
        """
        if self.user[-1] == 'True':
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'calendarTeacher'
        else:
            self.ids.nav_drawer.set_state("close")
            self.manager.current = 'calendar'
        
    def openTasks(self):
        """Данный метод открывает страницу с заданиями.
        """
        if self.user[-1] == 'True':
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
        if self.user[-1] == 'True':
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
        