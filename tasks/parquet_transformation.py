from pyspark.sql import SparkSession

spark_session = SparkSession.builder.appName("parquet_transformation") \
                                    .getOrCreate()
                                    
path = "/datalake/staging/credit_card_transaction.csv"      
csv_dataframe = spark_session.read.format("csv").option("header", "true").option("inferSchema", "true").load("/datalake/staging/credit_card_transaction.csv")
csv_dataframe.write.parquet("/datalake/storage/credit_card_transaction.parquet")
spark_session.stop()