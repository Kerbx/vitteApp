import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        
    def createUser(self, username, password):
        for i in self.createQuery('select username from students;'):
            if username == i:
                return None
            
        self.cursor.execute(f'insert into students (username, password) values ({username}, {password});')
    
    def createQuery(self, query):
        return self.cursor.execute(query).fetchall()

