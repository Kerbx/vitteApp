from typing import Union

import sqlite3


class Database():
    """Класс для работы с базой данных."""
    def __init__(self):
        """Инициализация подключения к базе данных, а также курсора для
        создания запросов.
        """
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        
    def __del__(self):
        """Деструктор класса."""
        self.connection.close()
        
    def createQuery(self, query: str) -> Union[list, bool]:
        """Метод для создания запросов в базу данных.
        Возвращает результат в виде списка значений или же в булевом виде -
        означает успех выполнения команды или неудачу.
        """
        try:
            answer = self.cursor.execute(query).fetchall()
            return answer
        except sqlite3.Error as error:
            return False
         
    def createUser(self, username: str, password: str, isTeacher: bool=False) -> bool:
        """Метод для создания пользователя в базе данных.
        """
        if not username or not password:
            return False
        
        try:
            for i in self.createQuery('select username from students;'):
                if username == i[0]:
                    return False
                
            self.cursor.execute(f'insert into students (username, password, isTeacher) values ("{username}", "{password}", {isTeacher});')
            self.connection.commit()
            return True
        
        except sqlite3.Error as error:
            return False
            
    def deleteUser(self, username: str, password: str) -> bool:
        """Метод для удаления пользователя из базы данных.
        """
        if not username or not password:
            return False
        try:
            for i in self.createQuery('select username from students;'):
                if username == i[0]:
                    self.cursor.execute(f'delete from students where username = "{username}";')
                    self.connection.commit()
                    return True
                else:
                    continue
            return False
        except sqlite3.Error as error:
            return False

    def checkIsTeacher(self, username: str) -> bool:
        """Метод для проверки, является ли пользователь преподавателем.
        """
        if not username:
            return False
        try:
            if self.createQuery(f'select isTeacher from students where username="{username}"')[0][0]:
                return True
            else:
                return False
        except:
            return False
        
    def checkLogin(self, username: str, password: str) -> bool:
        """Метод для проверки правильности введенной пары логин-пароль.
        """
        if not username or not password:
            return False
        try:
            if not self.cursor.execute(f'select username, password from students where username = "{username}" and password = "{password}";').fetchall():
                return False
            else:
                return True
        except sqlite3.Error as error:
            return False
        