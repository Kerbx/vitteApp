import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class SideMenu():
    pass


class MyApp(App):
    def build(self):
        return Label(text='KURWA KRET')
    
    
if __name__ == '__main__':
    MyApp().run()