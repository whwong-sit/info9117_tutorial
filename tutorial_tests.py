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

if __name__ == '__main__':
    unittest.main()
