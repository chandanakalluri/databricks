# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

# DBTITLE 1,reading files
def read_csv(path):
    df=spark.read.csv(path,header=True)
    return df
def write_csv( df , path):
    df.write.format('csv').mode("ignore").save(path)

# COMMAND ----------


# def write_csv( df , path):
    #df.write.format('csv').mode("ignore").save(path)

# COMMAND ----------

# DBTITLE 1,reading_schema
def read_schema(path,schema):
    df=spark.read.csv(path=path,header="false",schema=schema)
    return df

# COMMAND ----------

# DBTITLE 1,read_scheme_options
def read_schema_options(path,schema):
    df=spark.read.format("csv").options(header=False).schema(schema).load(path)
    return df

# COMMAND ----------

def change_column_case_to_snake_case(df):
    
    def camel_to_snake_case(column_name):
        return ''.join(['_' + c.lower() if c.isupper() else c for c in column_name]).lstrip('_')
    
    for column in df.columns:
        new_column_name = camel_to_snake_case(column)
        df = df.withColumnRenamed(column, new_column_name)
    
    return df

# COMMAND ----------

def write_delta_table(df, database, table, primary_key, path):
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {database}")
    df.write.format("delta") \
        .mode("overwrite") \
        .option("mergeSchema", "true") \
        .option("path", path) \
        .saveAsTable(f"{database}.{table}")
    
    return df




# COMMAND ----------

def read_with_custom_schema(data, schema):
    df = spark.read.csv(data, schema)
    return df

# COMMAND ----------

def read_with_custom_schema_format(data, schema):
    df = spark.read.format('csv').schema(schema).load(data)
    return df

# COMMAND ----------

#DBTITLE 1,Adding withColumn
def add_current_date(df):
    df = df.withColumn("load_date", current_date())
    return df


# COMMAND ----------

employee = ["employee_id"]