import kivy
kivy.require('2.1.0')

from kivymd.uix.snackbar import Snackbar

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from database import Database


Builder.load_string("""
<LoginScreen>:
    GridLayout:
        cols: 1
        rows: 3
        spacing: '10dp'
        padding: dp(50), dp(200)
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            MDTextField:
                id: username
                multiline: False
                mode: "fill"
                hint_text: 'Введите ваш логин'
                required: True
                helper_text_mode: "on_error"
                on_text_validate: root.focus_passwd()
        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'top'
            MDTextField:
                id: passwd
                multiline: False
                mode: "fill"
                hint_text: 'Введите ваш пароль'
                password: True
                required: True
                helper_text_mode: "on_error"
                on_text_validate: root.on_login()
        AnchorLayout:
            anchor_x: 'center'
            MDFlatButton:
                text: 'Войти'
                on_press: root.on_login()
""")


class LoginScreen(Screen):
    def focus_passwd(self):
        self.ids.passwd.focus = True
    
    def on_login(self):
        username = self.ids.username.text
        passwd = self.ids.passwd.text
        
        if not username or not passwd:

            Snackbar(text="Введите логин и пароль!", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()
            return
        
        db = Database()
        if not db.checkLogin(username, passwd):
            Snackbar(text="Неправильный логин или пароль!", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (10 * 2)) / Window.width).open()

            return
        else:
            self.ids.passwd.text = ''
            self.manager.current = 'main'
            