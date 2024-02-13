import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df1=spark.read.csv("s3://s3bcketname-s3bucket-rdkefn7n0vul/chocolate.csv")
df1.coalesce(1).write.parquet("s3://group05islauoutput/datawarehouse")

job.commit()
