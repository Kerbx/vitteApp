import kivy
kivy.require('2.1.0')

from kivymd.uix.screen import MDScreen


class SettingsScreenTeacher(MDScreen):
    def openMainTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'mainTeacher'
        
    def openCalendarTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'calendarTeacher'
        
    def openTasksTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasksTeacher'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettingsTeacher(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settingsTeacher'
        