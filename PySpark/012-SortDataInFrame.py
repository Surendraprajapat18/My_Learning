# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/vgsales.csv")
     .option("header", "True").load()
     )
display(df)

# COMMAND ----------

df1 = df.sort("Year")

# COMMAND ----------

display(df1)

# COMMAND ----------

df2 = df.sort("Year", "Rank")
display(df2)

# COMMAND ----------

from pyspark.sql.functions import col
df3 = df2.sort(col("Rank"))
display(df3)

# COMMAND ----------

df4 = df.sort(col("Rank").desc())
display(df4)

# COMMAND ----------

