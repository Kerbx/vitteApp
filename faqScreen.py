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


class Q3(MDBoxLayout):
    pass


class Q4(MDBoxLayout):
    pass


class Q5(MDBoxLayout):
    pass


class Q6(MDBoxLayout):
    pass


questions = [
    "Где вы находитесь?",
    "Какие у вас есть специальности?",
    "Сколько стоит обучение?",
    "Есть ли общежитие?",
    "Какой диплом я получу?",
    "Помогают ли с трудоустройством?"
]

answers = [Q1, Q2, Q3, Q4, Q5, Q6]


class FAQScreen(MDScreen):
    def on_enter(self):
        for i in range(0, len(questions)):
            self.ids.faq.add_widget(
                MDExpansionPanel(
                    content=answers[i](),
                    panel_cls=MDExpansionPanelOneLine(
                        text=questions[i]
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
        