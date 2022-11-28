from database import Database

import unittest


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database()
        
    def testCreateUser(self):
        self.assertEqual(self.db.createUser('admin', 'admin'), False)
        self.assertEqual(self.db.createUser('', ''), False)
        self.assertEqual(self.db.createUser('admin', ''), False)
        self.assertEqual(self.db.createUser('', 'password'), False)
        self.assertEqual(self.db.createUser('usr', 'password'), True)
        
    def testCheckLogin(self):
        self.assertEqual(self.db.checkLogin('admin', 'admin'), True)
        self.assertEqual(self.db.checkLogin('username', 'password'), True)
        self.assertEqual(self.db.checkLogin('', ''), False)
        self.assertEqual(self.db.checkLogin('admin', ''), False)
        self.assertEqual(self.db.checkLogin('', 'password'), False)    
        
    def testDeleteUser(self):
        self.assertEqual(self.db.deleteUser('usr', 'password'), True)
        self.assertEqual(self.db.deleteUser('', ''), False)
        self.assertEqual(self.db.deleteUser('admin', ''), False)
        self.assertEqual(self.db.deleteUser('', 'password'), False)
        self.assertEqual(self.db.deleteUser('user', 'passwd'), False)
        
    def testCreateQuery(self):
        self.assertEqual(type(self.db.createQuery('select * from students')), list)
        self.assertEqual(type(self.db.createQuery('select username, password from students')), list)
        self.assertEqual(type(self.db.createQuery('select * from stra')), bool)
        self.assertEqual(type(self.db.createQuery('ale')), bool)
        self.assertEqual(type(self.db.createQuery('select user from students')), bool)
        
    
if __name__ == '__main__':
    unittest.main()