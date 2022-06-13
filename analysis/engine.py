import logging

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

import pandas as pd

logger = logging.getLogger(__name__)


class SparkBuilder(object):

    def __init__(self):
        self.spark = None
        self.schema = None

    def _spark_builder(self, app_name: str) -> None:
        self.spark = (
            SparkSession.builder.appName(app_name).getOrCreate()
        )
        logger.info(f"create sparkSession")
        logger.info(f'version: {self.spark.version}')
        logger.info(f'appName: {self.spark.sparkContext.appName}')

    def _schema_builder(self, schema: StructType) -> None:
        self.schema = schema

    def builder(self, app_name: str, schema: StructType) -> None:
        self._spark_builder(app_name)
        self._schema_builder(schema)

    def write_csv(self, df: pd.DataFrame, output: str) -> None:
        df.to_csv(output, index=False, header=False, doublequote=False)
        logger.info(f"write output file: {output}")
