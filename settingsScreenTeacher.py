import kivy
kivy.require('2.1.0')

from kivymd.uix.screen import MDScreen


class SettingsScreenTeacher(MDScreen):
    """Класс для страницы настроек.
    """
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
        