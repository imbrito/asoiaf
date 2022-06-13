import os

from datetime import datetime

from unittest import TestCase
from pyspark.sql import types as T
from pyspark.sql import SparkSession
from engine import SparkBuilder

class SparkBuilderTest(TestCase):

    def setUp(self):
        self.sb = SparkBuilder()
        self.output = os.path.join(os.getcwd(), 'tests', 'test_engine.csv')
        self.app_name = "test"
        self.schema = T.StructType([T.StructField("test", T.StringType(), True),])

    def test_spark_builder(self):
        self.assertIsNone(self.sb.spark)
        self.assertIsNone(self.sb.schema)

    def test_builder(self):

        self.sb.builder(self.app_name, self.schema)

        self.assertIsInstance(self.sb.schema, T.StructType)
        self.assertIsInstance(self.sb.spark, SparkSession)

    def test_write_csv(self):
        
        self.sb.builder(self.app_name, self.schema)

        df = self.sb.spark.createDataFrame([(datetime.today(),)], ['time']).toPandas()

        self.sb.write_csv(df, self.output)

        self.assertTrue(os.path.isfile(self.output))
        os.remove(self.output)

    def tearDown(self):
        self.sb = None
        self.output = None
        self.app_name = None
        self.schema = None
