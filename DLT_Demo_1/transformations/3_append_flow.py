import dlt
from pyspark.sql.functions import *

dlt.create_streaming_table(
    name="append_table"
)

@dlt.append_flow(target="append_table")
def flow_1():
    df = spark.readStream.format('cloudFiles')\
              .option('cloudFiles.format', 'csv')\
              .load('/Volumes/databricks_dinesh/bronze/auto_vol/flow_1/')
    return df

@dlt.append_flow(target="append_table")
def flow_2():
    df = spark.readStream.format('cloudFiles')\
              .option('cloudFiles.format', 'csv')\
              .load('/Volumes/databricks_dinesh/bronze/auto_vol/flow_2/')
    return df