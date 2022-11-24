import kivy
kivy.require('2.1.0')

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from database import Database


class LoginScreen(GridLayout):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.cols = 1
        self.rows = 4
        self.padding = 200
        
        self.username = TextInput(width=100, multiline=False, hint_text='Login')
        self.passwd = TextInput(width=100, multiline=False, hint_text='Password', password=True)
        self.button = Button(text="Click", width=100
                             )
        self.username.bind(on_text_validate=self.focus_passwd)
        self.passwd.bind(on_text_validate=self.on_login)
        self.button.bind(on_press=self.on_login)
        
        self.add_widget(Label(text="Sing in", width=100))
        self.add_widget(self.username)
        self.add_widget(self.passwd)
        self.add_widget(self.button)
        
    def focus_passwd(self, _):
        self.passwd.focus = True
    
    def on_login(self, _):
        username = self.username.text
        passwd = self.passwd.text
        
        if not username or not passwd:
            Popup(title='Login fail', content=Label(text='Введите логин и пароль!'), size_hint=(None, None), size=(250, 250)).open()
            return
        
        db = Database()
        if not db.checkLogin(username, passwd):
            Popup(title='Login fail', content=Label(text='Неправильный логин или пароль.'), size_hint=(None, None), size=(250, 250)).open()
            return
        else:
            Popup(title='Login fail', content=Label(text='ЕСТЬ КУРИТЬ.'), size_hint=(None, None), size=(250, 250)).open()
            