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

help(rdd4.sortByKey)

# COMMAND ----------

rdd4.filter(lambda x: x[1]>1).collect()

# COMMAND ----------

rdd4.filter(lambda x: x[1]%2==0).collect()

# COMMAND ----------

rdd4.filter(lambda x: x[0]).collect()

# COMMAND ----------

rdd4.filter(lambda x : x[0].startswith("h")).collect()

# COMMAND ----------

rdd4.filter(lambda x : x[0].endswith("y")).collect()

# COMMAND ----------

rdd4.filter(lambda x : "e" in x[0]).collect()

# COMMAND ----------

rdd4.filter(lambda x : x[0].find("r")!=-1).collect()

# COMMAND ----------

"hello".find("o")

# COMMAND ----------

