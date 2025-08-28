import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

def sparkAggregate(glueContext, parentFrame, groups, aggs, transformation_ctx) -> DynamicFrame:
    aggsFuncs = []
    for column, func in aggs:
        aggsFuncs.append(getattr(SqlFuncs, func)(column))
    result = parentFrame.toDF().groupBy(*groups).agg(*aggsFuncs) if len(groups) > 0 else parentFrame.toDF().agg(*aggsFuncs)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1755082749060 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://aws-etl-project9/extract/"], "recurse": True}, transformation_ctx="AmazonS3_node1755082749060")

# Script generated for node Change Schema
ChangeSchema_node1756308318576 = ApplyMapping.apply(frame=AmazonS3_node1755082749060, mappings=[("passengerid", "string", "passengerid", "int"), ("survived", "string", "survived", "string"), ("pclass", "string", "pclass", "string"), ("name", "string", "name", "string"), ("sex", "string", "sex", "string"), ("age", "string", "age", "string"), ("sibsp", "string", "sibsp", "string"), ("parch", "string", "parch", "string"), ("ticket", "string", "ticket", "string"), ("fare", "string", "fare", "string"), ("cabin", "string", "cabin", "string"), ("embarked", "string", "embarked", "string")], transformation_ctx="ChangeSchema_node1756308318576")

# Script generated for node Drop Fields
DropFields_node1756307522247 = DropFields.apply(frame=ChangeSchema_node1756308318576, paths=[], transformation_ctx="DropFields_node1756307522247")

# Script generated for node Aggregate
Aggregate_node1756307530340 = sparkAggregate(glueContext, parentFrame = DropFields_node1756307522247, groups = ["passengerid"], aggs = [["name", "count"]], transformation_ctx = "Aggregate_node1756307530340")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Aggregate_node1756307530340, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1755082727272", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
if (Aggregate_node1756307530340.count() >= 1):
   Aggregate_node1756307530340 = Aggregate_node1756307530340.coalesce(1)
AmazonS3_node1755083267416 = glueContext.write_dynamic_frame.from_options(frame=Aggregate_node1756307530340, connection_type="s3", format="glueparquet", connection_options={"path": "s3://aws-etl-project9/load/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1755083267416")

job.commit()