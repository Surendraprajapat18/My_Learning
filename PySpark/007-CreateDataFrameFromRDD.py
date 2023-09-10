# Databricks notebook source
rdd = sc.parallelize([(1, "India"), (2,"UK"), (3,"Us"), (4, "JAPAN")])

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd.count()

# COMMAND ----------

help(rdd.toDF)

# COMMAND ----------

rdd.toDF()

# COMMAND ----------

df = rdd.toDF()

# COMMAND ----------

df.collect()

# COMMAND ----------

df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

df.count()

# COMMAND ----------

help(df.show)

# COMMAND ----------

df.show(3)

# COMMAND ----------

myschema=['ID', 'Country']

# COMMAND ----------

df2=rdd.toDF(myschema)

# COMMAND ----------

df2.show()

# COMMAND ----------

df3 = rdd.toDF("id integer, country string")

# COMMAND ----------

df3.show()

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, LongType, StringType, DateType

# COMMAND ----------

from pyspark import *

# COMMAND ----------

mydfschema = StructType([
    StructField("id", LongType(), True),
    StructField("Country", StringType(), True)
])

# COMMAND ----------

df4 = rdd.toDF(mydfschema)

# COMMAND ----------

df4.show()

# COMMAND ----------

help(spark.createDataFrame)

# COMMAND ----------

df5 = spark.createDataFrame(rdd)

# COMMAND ----------

df5.show()

# COMMAND ----------

df6 = spark.createDataFrame(rdd, mydfschema)

# COMMAND ----------

df6.show()

# COMMAND ----------

df7 = spark.createDataFrame(rdd, "id long, country string")

# COMMAND ----------

df7.show()

# COMMAND ----------

