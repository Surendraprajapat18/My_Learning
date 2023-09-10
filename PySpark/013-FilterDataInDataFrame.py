# Databricks notebook source
df = (spark.read.format("csv")
     .option("path", "dbfs:/FileStore/tables/vgsales.csv")
     .option("header", "True").load()
     )
display(df)

# COMMAND ----------

df1 = df.filter("Rank==200")
display(df1)

# COMMAND ----------

df2 = df.filter("Publisher=='Electronic Arts'")
display(df2)

# COMMAND ----------

# DBTITLE 1,Remove Duplicates In DataFrame
display(df)

# COMMAND ----------

df4 = df.dropDuplicates()
display(df4)

# COMMAND ----------

df5 = df.dropDuplicates(['Publisher'])
display(df5)

# COMMAND ----------

# Find the unique Value
df6 = df.select("Publisher").distinct()
display(df6)

# COMMAND ----------

