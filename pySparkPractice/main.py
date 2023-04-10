import os
import sys
from typing import List, Tuple

from pyspark.sql.column import Column
from pyspark.sql.functions import col

from utils.util_functions import df_cols_null_check

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


def explain_rdd(rdd):
    print(rdd.glom())
    print(str(rdd.toDebugString(), 'UTF-8'))


def find_in_col(col: Column, ind: int):
    print(col.name())
    print(ind)
    if (col == 'PushEvent'):
        return True
    return False



file_name = r'C:\Users\GokulReddy\PycharmProjects\pySparkPractice\data\ipl\IPL_Matches_2008_2022.csv'
player_file = r'C:\Users\GokulReddy\PycharmProjects\pySparkPractice\data\ipl\player\IPL_Player_Data.csv'

if __name__ == '__main__':
    from pyspark.sql import SparkSession, Column
    import pyspark.pandas as ps

    spark = SparkSession.builder.appName("example - pyspark - hdfs").master('local[4]').getOrCreate()
    sc = spark.sparkContext

    df = spark.read.options(header=True,inferSchema=True).csv(player_file)


    df.printSchema()

    df.select(col("Sport")).distinct().show()
