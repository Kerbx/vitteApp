import kivy
kivy.require('2.1.0')

from kivymd.app import MDApp

from kivy.lang import Builder
Builder.load_file('vitte.kv')

from kivymd.uix.screenmanager import ScreenManager

from calendarScreen import CalendarScreen
from calendarScreenTeacher import CalendarScreenTeacher
from loginScreen import LoginScreen
from mainScreen import MainScreen
from mainScreenTeacher import MainScreenTeacher
from settingsScreen import SettingsScreen
from settingsScreenTeacher import SettingsScreenTeacher
from tasksScreen import TasksScreen
from tasksScreenTeacher import TasksScreenTeacher


class MyApp(MDApp):
    def build(self):
        self.title = 'vitteApp'
        
        self.screenManager = ScreenManager()
        self.loginScreen = LoginScreen(name='login')
        self.mainScreen = MainScreen(name='main')
        self.mainTeacher = MainScreenTeacher(name='mainTeacher')
        self.calendarScreen = CalendarScreen(name='calendar')
        self.calendarTeacher = CalendarScreenTeacher(name='calendarTeacher')
        self.tasksScreen = TasksScreen(name='tasks')
        self.tasksTeacher = TasksScreenTeacher(name='tasksTeacher')
        self.settingsScreen = SettingsScreen(name='settings')
        self.settingsTeacher = SettingsScreenTeacher(name='settingsTeacher')
        
        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.mainScreen)
        self.screenManager.add_widget(self.mainTeacher)
        self.screenManager.add_widget(self.calendarScreen)
        self.screenManager.add_widget(self.calendarTeacher)
        self.screenManager.add_widget(self.tasksScreen)
        self.screenManager.add_widget(self.tasksTeacher)
        self.screenManager.add_widget(self.settingsScreen)
        self.screenManager.add_widget(self.settingsTeacher)

        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Orange"
        
        self.screenManager.current = 'login'
        return self.screenManager
    
    def switchThemeStyle(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

        
if __name__ == '__main__':
    MyApp().run()
    