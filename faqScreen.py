import kivy
kivy.require('2.1.0')

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine


user = open('login.txt').read().split('\n')


class Q1(MDBoxLayout):
    pass


class Q2(MDBoxLayout):
    pass


class FAQScreen(MDScreen):
    def on_enter(self):
        self.ids.faq.add_widget(
            MDExpansionPanel(
                content=Q1(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Где вы находитесь?"
                )
            )
        )
        self.ids.faq.add_widget(
            MDExpansionPanel(
                content=Q2(),
                panel_cls=MDExpansionPanelOneLine(
                    text="Какие у вас есть специальности?"
                )
            )
        )
        
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
        