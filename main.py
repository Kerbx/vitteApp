import kivy
kivy.require('2.1.0')

from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager

from calendarScreen import CalendarScreen
from loginScreen import LoginScreen
from mainScreen import MainScreen
from tasksScreen import TasksScreen


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'vitteApp'
        self.screenManager = ScreenManager()
        self.loginScreen = LoginScreen(name='login')
        self.mainScreen = MainScreen(name='main')
        self.calendarScreen = CalendarScreen(name='calendar')
        self.tasksScreen = TasksScreen(name='tasks')
        
        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.mainScreen)
        self.screenManager.add_widget(self.calendarScreen)
        self.screenManager.add_widget(self.tasksScreen)
        
    def build(self):
        self.screenManager.current = 'login'
        return self.screenManager
    
    
if __name__ == '__main__':
    MyApp().run()
    