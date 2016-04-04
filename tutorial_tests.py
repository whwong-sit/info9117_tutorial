import os
import tutorial
import unittest
import tempfile

class UserLoginTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, tutorial.app.config['DATABASE'] = tempfile.mkstemp()
        tutorial.app.config['TESTING'] = True
        self.app = tutorial.app.test_client()

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(tutorial.app.config['DATABASE'])
        pass

    def test_root_path(self):
        rv = self.app.get('/')
        assert b'Hello World' in rv.data

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_login_success(self):
        rv = self.login('test', 'test123')
        assert b'Success' in rv.data

    def test_login_fail(self):
        rv = self.login('superman', 'superman')
        assert b'Fail' in rv.data

if __name__ == '__main__':
    unittest.main()
