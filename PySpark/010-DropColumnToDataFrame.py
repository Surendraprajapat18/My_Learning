# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/vgsales.csv")
     .option("header", "True").load()
     )

# COMMAND ----------

display(df)

# COMMAND ----------

df1 = df.drop("Publisher")

# COMMAND ----------

display(df1)

# COMMAND ----------

# Remove two more columns
df2 = df.drop("Publisher", "EU_Sales", "JP_Sales", "NA_Sales")

# COMMAND ----------

display(df2)

# COMMAND ----------

