import kivy
kivy.require('2.1.0')
import socket

from kivymd.uix.screen import MDScreen


class TasksScreen(MDScreen):
    def update(self):
        separator = "<SEPARATOR>"
        bufferSize = 4096
        host = "0.0.0.0"
        port = 5555
        
    
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
        