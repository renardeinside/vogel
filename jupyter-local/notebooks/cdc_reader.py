import pyspark

spark = pyspark.sql.SparkSession.builder \
        .master("local[1]") \
        .appName("cdc-reader") \
        .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

stream = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "dbserver1.inventory.customers") \
  .load()


updates = stream.selectExpr("CAST(key AS STRING) as record_key", "CAST(value AS STRING) as record_value")


query = updates \
    .writeStream \
    .format("console") \
    .start()

query.awaitTermination()
