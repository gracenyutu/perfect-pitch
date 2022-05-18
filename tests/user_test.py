import unittest
from pitches.models import user
User = user.User

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the User class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User("1","jamesm","james@ms.com","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))


if __name__ == '__main__':
    unittest.main()