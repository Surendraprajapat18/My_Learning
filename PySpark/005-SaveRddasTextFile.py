# Databricks notebook source
rdd = sc.textFile("/FileStore/tables/001_Textfile.txt")

# COMMAND ----------

rdd2 = rdd.flatMap(lambda x : x.split(" "))

# COMMAND ----------

rdd3 = rdd2.map(lambda x : (x, 1))

# COMMAND ----------

rdd4 = rdd3.reduceByKey(lambda x,y : x+y)

# COMMAND ----------

rdd4.collect()

# COMMAND ----------

help(rdd4.saveAsTextFile)

# COMMAND ----------

rdd4.saveAsTextFile("/FileStore/tables/PysparkFile1")

# COMMAND ----------

display(spark.read.text("/FileStore/tables/PysparkFile1"))

# COMMAND ----------

