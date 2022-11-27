import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.config import Config

from kivy.uix.screenmanager import ScreenManager

from loginScreen import LoginScreen
from mainScreen import MainScreen


Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'vitteApp'
        self.screenManager = ScreenManager()
        self.loginScreen = LoginScreen(name='login')
        self.mainScreen = MainScreen(name='main')
        
        self.screenManager.add_widget(self.loginScreen)
        self.screenManager.add_widget(self.mainScreen)
        
    def build(self):
        self.screenManager.current = 'login'
        return self.screenManager
    
    
if __name__ == '__main__':
    MyApp().run()
    