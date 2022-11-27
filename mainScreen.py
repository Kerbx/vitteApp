import kivy
kivy.require('2.1.0')

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<MainScreen>:
    GridLayout:
        cols: 1
        rows: 3
        padding: 0
        
        Label:
            text: 'Main page.'
""")


class MainScreen(Screen):
    pass
