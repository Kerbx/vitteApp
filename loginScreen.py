import kivy
kivy.require('2.1.0')

from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from database import Database


Builder.load_string("""
<LoginScreen>:
    GridLayout:
        cols: 1
        rows: 3
        padding: 50, 250
        
        TextInput:
            id: username
            width: 100
            multiline: False
            hint_text: 'Login'
            on_text_validate: root.focus_passwd()
        TextInput:
            id: passwd
            width: 100
            multiline: False
            hint_text: 'Password'
            on_text_validate: root.on_login()
        Button:
            text: 'Click'
            width: 100
            on_press: on_login()
                    """)


class LoginScreen(Screen):
    def focus_passwd(self):
        self.ids.passwd.focus = True
    
    def on_login(self):
        username = self.ids.username.text
        passwd = self.ids.passwd.text
        
        if not username or not passwd:
            Popup(title='Login fail', content=Label(text='Введите логин и пароль!'), size_hint=(None, None), size=(250, 250)).open()
            return
        
        db = Database()
        if not db.checkLogin(username, passwd):
            Popup(title='Login fail', content=Label(text='Неправильный логин или пароль.'), size_hint=(None, None), size=(250, 250)).open()
            return
        else:
            self.manager.current = 'main'