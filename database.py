import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        
    def __del__(self):
        self.connection.close()
        
    def createQuery(self, query):
        return self.cursor.execute(query ).fetchall()
    
    def createUser(self, username, password):
        if not username or not password:
            return None
        try:
            for i in self.createQuery('select username from students;'):
                if username == i[0]:
                    return None
        except sqlite3.Error as error:
            return None
            
        else:
            self.cursor.execute(f'insert into students (username, password) values ("{username}", "{password}");')
            self.connection.commit()
        
    def deleteUser(self, username, password):
        if not username or not password:
            return None
        try:
            for i in self.createQuery('select username from students;'):
                if username == i[0]:
                    self.cursor.execute(f'delete from students where username = "{username}";')
                    self.connection.commit()
        except sqlite3.Error as error:
            return None

    def checkLogin(self, username, password):
        if not username or not password:
            return None
        try:
            if not self.cursor.execute(f'select username, password from students where username = "{username}" and password = "{password}";'):
                return None
            else:
                return True
        except sqlite3.Error as error:
            return None