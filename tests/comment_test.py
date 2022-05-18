import unittest
from pitches.models import comment
Comment = comment.Comment

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


if __name__ == '__main__':
    unittest.main()