from unittest import TestCase
from datetime import date
from asoiaf import ASongOfIceAndFire

class ASongOfIceAndFireTest(TestCase):

    def setUp(self):
        self.bf = None

    def test_asoiaf(self):
        self.bf = ASongOfIceAndFire()

        self.assertIsNone(self.bf.spark)
        self.assertIsNone(self.bf.schema)
        self.assertIsNone(self.bf.df)

    def tearDown(self):
        self.bf = None
