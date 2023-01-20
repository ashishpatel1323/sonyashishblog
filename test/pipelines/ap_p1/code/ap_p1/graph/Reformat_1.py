from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ap_p1.config.ConfigStore import *
from ap_p1.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(lit(Config.ap1_v1).alias("_c0"))
