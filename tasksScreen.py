import kivy
kivy.require('2.1.0')

from kivymd.uix.screen import MDScreen


class TasksScreen(MDScreen):
    def openMain(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'main'
        
    def openCalendar(self):
        self.manager.current = 'calendar'
        self.ids.nav_drawer.set_state("close")
        
    def openTasks(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'tasks'
        
    def logout(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'login'

    def openSettings(self):
        self.ids.nav_drawer.set_state("close")
        self.manager.current = 'settings'
        