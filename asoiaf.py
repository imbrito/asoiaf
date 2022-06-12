import string
import os
import logging

from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import functions as F

from engine import SparkBuilder

logger = logging.getLogger(__name__)


class ASongOfIceAndFire(SparkBuilder):

    def __init__(self):
        super().__init__()
        self.df = None
    
    def _builder(self, app_name: str) -> None:
        schema = StructType([
            StructField("character1", StringType(), True),
            StructField("character2", StringType(), True),
            StructField("weight", IntegerType(), True),
            StructField("book", IntegerType(), True),
        ])

        super().builder(app_name, schema)

    def _first_challenge(self, output: str) -> None:
        logger.info(f"init first challenge")
        grouped = []
        for i in [1,2]:
            grouped.append(
                self.df
                .groupBy(
                    F.column(f'character{i}').alias('character'), 
                    F.column('book')
                )
                .agg(
                    F.sum('weight').alias('weightByBook')
                )
            )
        logger.info(f"grouped data by character and book for sum weight")

        character_df = grouped[0].unionByName(grouped[1])
        logger.info(f"union grouped data")

        pivot_df = (
            character_df
            .groupBy('character')
            .pivot('book')
            .sum('weightByBook')
        )
        logger.info(f"pivot data by book and weightByBook")

        pivot_df = pivot_df.na.fill(value=0, subset=['1','2','3'])
        logger.info(f"replace null by 0")
        
        pivot_df = pivot_df.withColumn(
            'w', 
            F.lit(
                F.column('1') + F.column('2') + F.column('3')
            )
        )
        logger.info('calulates a sum of total weight')

        pd = pivot_df.toPandas()
        logger.info('converts to pandas dataframe')

        pd['character_tab_1'] =  pd.character + '\t' + pd['1'].map(str)
        pd = pd[['character_tab_1', '2', '3', 'w']]
        pd = pd.sort_values(by=['w'], ascending=False)
        logger.info('format output file')

        self.write_csv(pd, output)
        logger.info(f"finish first challenge")

    def _second_challenge(self, output: str) -> None:
        logger.info(f"init second challenge")
        
        c1 = (
            self.df
            .groupby(F.column('character1').alias('character'))
            .agg(F.collect_list('character2').alias('friends'))
        )
        logger.info('grouped friends for character1')
        
        c2 = (
            self.df
            .groupby(F.column('character2').alias('character'))
            .agg(F.collect_list('character1').alias('friends'))
        )
        logger.info('grouped friends for character2')

        c3 = c1.unionByName(c2)
        logger.info(f"union grouped data")

        c4 = c3.select(F.column('character'), F.explode(F.column('friends')).alias('friends'))
        c5 = c4.groupBy('character').agg(F.collect_set(F.column('friends')).alias('friends'))
        logger.info(f"re-grouped data by all characters and friends")

        c6 = c5.crossJoin(c5.select(c5.character.alias('target'), c5.friends.alias('target_friends')))
        logger.info(f"crossing data")

        c7 = c6.filter(c6.character != c6.target)
        c7 = c7.withColumn('common_friends', F.array_intersect(c7.friends, c7.target_friends))
        c8 = c7.select(c7.character, c7.target, c7.common_friends).filter(F.size(c7.common_friends) > 0)
        logger.info(f"filter data by common friends more than zero")

        pd = c8.toPandas()
        logger.info('converts to pandas dataframe')

        pd['list_of_common_friends'] = pd['common_friends'].apply(lambda x: ','.join(map(str, x)))
        pd['formatter_output'] = pd.character + '\t' + pd.target + '\t' + pd.list_of_common_friends
        pd = pd[['formatter_output']]
        logger.info('format output file')

        self.write_csv(pd, output)
        logger.info(f"finish second challenge")


    def run(self, filepath: str, output: str) -> None:
        self._builder("A Song of Ice and Fire")
        
        self.df = self.spark.read.csv(path=filepath, schema=self.schema)
        logger.info(f"read input file: {filepath}")

        self._first_challenge(os.path.join(output, 'challenge1.csv'))
        self._second_challenge(os.path.join(output, 'challenge2.csv'))
        