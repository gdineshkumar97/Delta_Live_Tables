import dlt
from pyspark.sql.functions import *
table_name = spark.conf.get("table_name")

expectations = {
    "rule1": "product_id IS NOT NULL",
    "rule2": "category IS NOT NULL"
}

@dlt.table(
    name="expect_table"
)
@dlt.expect_all_or_drop(expectations)
def expect_table():
    tbl_nm = f"databricks_dinesh.silver.{table_name}"
    df = spark.read.table(tbl_nm)
    return df