# Databricks notebook source
lst = [1,2,3,4,5,6]

# COMMAND ----------

print(lst)

# COMMAND ----------

type(lst)

# COMMAND ----------

sparkC = spark.sparkContext

# COMMAND ----------

type(sparkC)

# COMMAND ----------

rdd = sparkC.parallelize(lst)

# COMMAND ----------

type(rdd)

# COMMAND ----------

print(rdd)

# COMMAND ----------

rdd.collect()

# COMMAND ----------

lst2 = [1,2,3,"India"]

# COMMAND ----------

rdd2 = sc.parallelize(lst2)

# COMMAND ----------

rdd.collect() # Collect is a action

# COMMAND ----------

rdd3 = sc.parallelize([1,2,3,4])
rdd3.collect()

# COMMAND ----------

