import kivy
kivy.require('2.1.0')

from kivymd.uix.snackbar import Snackbar

from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

from database import Database


class LoginScreen(MDScreen):
    def focus_passwd(self):
        """Метод вызывается при нажатии на enter для перехода
        к следующему полю ввода.
        """
        self.ids.passwd.focus = True
    
    def on_login(self):
        """Данный метод делает запрос на проверку данных в базу данных.
        При правильном вводе перекидывает на соответствующую главную страницу,
        в ином случае отображает всплывающее окно с ошибкой.
        """
        username = self.ids.username.text
        passwd = self.ids.passwd.text
        
        if not username or not passwd:

            Snackbar(text="Введите логин и пароль!",
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     size_hint_x= \
                         (Window.width - (10 * 2)) / Window.width).open()
            return
        
        db = Database()
        if not db.checkLogin(username, passwd):
            Snackbar(text="Неправильный логин или пароль!",
                     snackbar_x="10dp",
                     snackbar_y="10dp",
                     size_hint_x= \
                         (Window.width - (10 * 2)) / Window.width).open()

            return
        else:
            self.ids.passwd.text = ''
            # Тут в файл записывается логин-пароль, чтобы потом со стороны
            # студента при прикреплении файла отправлять также кем этот
            # файл был прикреплен.
            with open('login.txt', 'w') as file:
                file.write(f'{username}\n{passwd}\n{db.checkIsTeacher(username)}')
            if db.checkIsTeacher(username):
                self.manager.current = 'mainTeacher'
            else:
                self.manager.current = 'main'
            