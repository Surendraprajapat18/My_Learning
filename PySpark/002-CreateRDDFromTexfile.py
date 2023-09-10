# Databricks notebook source
help(sc.textFile)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/001_Textfile.txt")

# COMMAND ----------

rdd

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x : x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.map(lambda x : (x, 1))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd4 = rdd3.reduceByKey(lambda x,y : x+y)

# COMMAND ----------

rdd4.collect()

# COMMAND ----------

