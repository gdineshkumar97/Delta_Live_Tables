import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="scd_stg"
)
def scd_stg():
    df = spark.read.table('databricks_dinesh.bronze.scd1_source')
    return df

dlt.create_streaming_table(
    name="scd1_table"
)

dlt.create_auto_cdc_flow(
    target="scd1_table",
    source="scd_stg",
    keys=["product_id"],
    sequence_by=col("load_time"),
    stored_as_scd_type=1

)

dlt.create_streaming_table(
    name="scd2_table"
)

dlt.create_auto_cdc_flow(
    target="scd2_table",
    source="scd_stg",
    keys=["product_id"],
    sequence_by=col("load_time"),
    stored_as_scd_type=2,
    

)