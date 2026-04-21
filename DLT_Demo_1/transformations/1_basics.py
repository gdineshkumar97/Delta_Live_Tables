import dlt
from pyspark.sql.functions import *
# CREATE STREAMING TABLE demo_stream_table
@dlt.table(name= 'sales_stg')
def sales_stg():
    df = spark.readStream\
        .option('skipChangeCommits', True)\
        .table("databricks_dinesh.silver.sales_enr")
    return df

# CREATE MATERIALIZED VIEW
@dlt.table(name='sales_enr')
def sales_enr():
    df = spark.read.table("sales_stg")
    df = df.withColumn("priceAfterDiscount", col("total_amount") - col("discount"))
    return df

# CREATE MATERIALIZED VIEW
@dlt.table(name='sales_cur')
def sales_cur():
    df = spark.read.table("sales_enr")
    return df

# # TEMPORARY VIEW
# @dlt.view(name='demo_temp_view')
# def demo_temp_view():
#     df = spark.read.table("databricks_dinesh.silver.sales_enr")
#     return df

# # TEMPORARY STREAM VIEW
# @dlt.view(name='demo_temp_stream_view')
# def demo_temp_stream_view():
#     df = spark.readStream.table("databricks_dinesh.silver.sales_enr")
#     return df
