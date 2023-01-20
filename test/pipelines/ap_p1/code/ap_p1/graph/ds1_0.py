from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ap_p1.config.ConfigStore import *
from ap_p1.udfs.UDFs import *

def ds1_0(spark: SparkSession) -> DataFrame:
    return spark.read.option("header", True).option("sep", ",").csv("dbfs:/Prophecy/qa_data/csv/all_type_no_partition")
