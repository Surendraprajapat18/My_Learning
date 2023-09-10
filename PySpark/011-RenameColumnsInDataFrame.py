# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/vgsales.csv")
     .option("header", "True").load()
     )

# COMMAND ----------

display(df)

# COMMAND ----------

df1 = df.drop("Publisher", "EU_Sales", "JP_Sales", "NA_Sales", "Platform", "Genre", "Other_Sales")

# COMMAND ----------

display(df1)

# COMMAND ----------

df2 = df.withColumnRenamed("Rank", "Product_ID")

# COMMAND ----------

display(df2)

# COMMAND ----------

df3 = df2.selectExpr("Global_Sales as Sales")

# COMMAND ----------

display(df3)

# COMMAND ----------

df.columns

# COMMAND ----------

