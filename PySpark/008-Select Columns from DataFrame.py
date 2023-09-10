# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/amazon_sales.csv")
     .option("header", "True").load()
     )

# COMMAND ----------

display(df)

# COMMAND ----------

df1 = df.select("product_id", "Product_name")

# COMMAND ----------

display(df1)

# COMMAND ----------

from pyspark.sql.functions import col


# COMMAND ----------

df1 = df.select(col("product_id"), col("Product_name"))

# COMMAND ----------

display(df1)

# COMMAND ----------

df2 = df.selectExpr("product_id", "Product_name")

# COMMAND ----------

display(df2)

# COMMAND ----------

df3 = df.selectExpr("product_id", "Product_name", "concat(product_id, '-ABC') AS ProductABC")
display(df3)

# COMMAND ----------

from pyspark.sql.functions import expr

# COMMAND ----------

df4 = df.select("product_id", "Product_name", expr("concat(product_id, '-ABC') AS ProductABC"))
display(df4)

# COMMAND ----------

