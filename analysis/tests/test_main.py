from unittest import TestCase
from main import read_args

class MainTest(TestCase):

    def setUp(self):
        self.parser = read_args().parse_args(['-c'])
    
    def test_read_args(self):

        self.assertTrue(self.parser.challenge)

    def tearDown(self):
        self.parser = None
