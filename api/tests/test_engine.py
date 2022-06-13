import unittest

from mockupdb import MockupDB
from pymongo import MongoClient
from pymongo.cursor import Cursor

from exceptions import DataAccessError
from engine import MongoEngine


class MongoEngineTest(unittest.TestCase):

    def setUp(self):
        self.server = MockupDB(auto_ismaster=True)
        self.server.run()
        self.engine = MongoEngine(self.server.uri)

    def test_engine(self):
        
        self.assertIsInstance(self.engine.client, MongoClient)
        self.assertIsInstance(self.engine.database, type(None))
        self.assertIsInstance(self.engine.cursor, type(None))

    def test_insert_data(self):

        with self.assertRaises(DataAccessError):
            self.engine.insert_data('Foo', 'Bar', {})

    def test_get_data(self):
        
        cursor = self.engine.get_data('Foo', 'Bar', {'foo': 'bar'})
        self.assertIsInstance(cursor, Cursor)

    def tearDown(self):
        self.server.stop()