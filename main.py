import kivy
kivy.require('2.1.0')

from kivy.app import App

from mainScreen import MainScreen


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'vitteApp'
        
    def build(self):
        return MainScreen()
    
    
if __name__ == '__main__':
    MyApp().run()