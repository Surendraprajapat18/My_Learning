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

rdd5 = rdd4.sortByKey()

# COMMAND ----------

rdd5.collect()

# COMMAND ----------

rdd6 = rdd4.sortByKey(False)

# COMMAND ----------

rdd6.collect()

# COMMAND ----------

rdd7 = rdd4.sortBy(lambda x : x[1])

# COMMAND ----------

rdd7.collect()

# COMMAND ----------

rdd8 = rdd4.sortBy(lambda x : x[1], False)

# COMMAND ----------

rdd8.collect()

# COMMAND ----------

x = rdd4.first()

# COMMAND ----------

type(x)

# COMMAND ----------

type(rdd4)

# COMMAND ----------

x[1]

# COMMAND ----------

rdd8 = rdd8.sortBy(lambda x: x[1], False)
rdd8.collect()

# COMMAND ----------

y = rdd8.take(3)

# COMMAND ----------

type(y)

# COMMAND ----------

rdd7.take(4)

# COMMAND ----------

rddKey = rdd4.keys()

# COMMAND ----------

rddKey.collect()

# COMMAND ----------

rddValue = rdd4.values()
rddValue.collect()

# COMMAND ----------

