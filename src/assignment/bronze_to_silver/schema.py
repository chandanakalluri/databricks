# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql import *
country_schema=StructType([
    StructField("country_code",StringType(),True),
    StructField("country_name",StringType(),True)
])

# COMMAND ----------

employee_schema=StructType([
    StructField("employee_id",IntegerType(),True),
    StructField("employee_name",StringType(),True),
    StructField("department", StringType(), True),
    StructField("State",StringType(), True),
    StructField("Salary",IntegerType(), True),
    StructField("Age",IntegerType(), True)
])

# COMMAND ----------

department_schema=StructType([
    StructField("dept_id",StringType(),True),
    StructField("dept_name",StringType(),True),
])
