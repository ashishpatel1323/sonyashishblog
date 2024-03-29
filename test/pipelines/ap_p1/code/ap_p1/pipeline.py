from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ap_p1.config.ConfigStore import *
from ap_p1.udfs.UDFs import *
from prophecy.utils import *
from ap_p1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds1_0 = ds1_0(spark)
    df_Reformat_1 = Reformat_1(spark, df_ds1_0)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ap_p1")
    
    MetricsCollector.start(spark = spark, pipelineId = spark.conf.get("prophecy.project.id") + "/" + "pipelines/ap_p1")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
