from pyspark.sql import SparkSession

spark_session = SparkSession.builder \
                    .appName("parquet_transformation") \
                    .master("spark://spark-master:7077") \
                    .getOrCreate()
                                    
path = "/datalake/staging/credit_card_transaction.csv"      
csv_dataframe = spark_session.read.format("csv").option("header", "true").option("inferSchema", "true").load("/datalake/staging/credit_card_transaction.csv")
cleaned_dataframe = csv_dataframe.drop(csv_dataframe.columns[0])
csv_dataframe.write.mode("overwrite").parquet("/datalake/storage/credit_card_transaction.parquet")
spark_session.stop()