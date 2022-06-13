from unittest import TestCase
from version import read_version
from version import VERSION, MAJOR, MINOR, REVISION

class ASongOfIceAndFireTest(TestCase):

    def setUp(self):
        self.app_version = read_version()

    def test_read_version(self):
        
        self.assertIsInstance(self.app_version, dict)
        self.assertEquals(VERSION, self.app_version.get('app_version'))
        self.assertEquals(MAJOR, self.app_version.get('major'))
        self.assertEquals(MINOR, self.app_version.get('minor'))
        self.assertEquals(REVISION, self.app_version.get('revision'))
        
    def tearDown(self):
        self.app_version = None