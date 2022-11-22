import kivy
kivy.require('2.1.0')

from kivy.uix.floatlayout import FloatLayout


class MainScreen(FloatLayout):
    def __init__(self):
        super(MainScreen, self).__init__()
    
    def menu_action(self):
        self.add_widget()