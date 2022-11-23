import kivy
kivy.require('2.1.0')

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class MainScreen(GridLayout):
    def __init__(self):
        self.cols = 1
        self.rows = 3
        super(MainScreen, self).__init__()
    