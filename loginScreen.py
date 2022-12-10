import kivy
kivy.require('2.1.0')

from kivymd.uix.snackbar import Snackbar

from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

from database import Database


class LoginScreen(MDScreen):
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
            with open('login.txt.', 'w') as file:
                file.write(f'{username}\n{passwd}')
            if db.checkIsTeacher(username):
                self.manager.current = 'mainTeacher'
            else:
                self.manager.current = 'main'
            