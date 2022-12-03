import kivy
kivy.require('2.1.0')

from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager

from calendarScreen import CalendarScreen
from loginScreen import LoginScreen
from mainScreen import MainScreen
from settingsScreen import SettingsScreen
from tasksScreen import TasksScreen


class MyApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"
        
        self.title = 'vitteApp'
        self.screenManager = ScreenManager()
        self.loginScreen = LoginScreen(name='login')
        self.mainScreen = MainScreen(name='main')
        self.calendarScreen = CalendarScreen(name='calendar')
        self.tasksScreen = TasksScreen(name='tasks')
        self.settingsScreen = SettingsScreen(name='settings')
        
        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.mainScreen)
        self.screenManager.add_widget(self.calendarScreen)
        self.screenManager.add_widget(self.tasksScreen)
        self.screenManager.add_widget(self.settingsScreen)
        
    def switchThemeStyle(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        self.theme_cls.primary_palette = "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        
    def build(self):
        self.screenManager.current = 'login'
        return self.screenManager
    
    
if __name__ == '__main__':
    MyApp().run()
    