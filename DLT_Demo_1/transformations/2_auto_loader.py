import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="autovol_table"
)
def autovol_table():
    df = spark.readStream.format('cloudFiles')\
        .option("cloudFiles.format", "csv")\
        .load('/Volumes/databricks_dinesh/bronze/bronze_volume/raw/')
    return df

@dlt.table(
    name= "autoval_table_enr"
)
def autoval_table_enr():
    df = spark.read.table("autovol_table")
    df = df.withColumn("flag", lit("Yes"))
    return df