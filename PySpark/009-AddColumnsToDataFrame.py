# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/vgsales.csv")
     .option("header", "True").load()
     )

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import lit, col

# COMMAND ----------

df1 = df.withColumn("Country", lit("India"))

# COMMAND ----------

display(df1)

# COMMAND ----------

df2 = df1.withColumn("Tax", col("Global_Sales") * 0.05)

# COMMAND ----------

display(df2)

# COMMAND ----------

df2.printSchema()

# COMMAND ----------

# chaging rank column datatype string to integer
df3 = df2.withColumn("Rank", col("Rank").cast("integer"))
display(df3)

# COMMAND ----------

df3.printSchema()

# COMMAND ----------

