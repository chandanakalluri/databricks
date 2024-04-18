# Databricks notebook source
# MAGIC %run "/Users/kalluri.chandana@diggibyte.com/assignment/source_to_bronze/utils"

# COMMAND ----------

# DBTITLE 1,reading_csv_files
employee_read_path = 'dbfs:/FileStore/resource/Employee_Q1.csv'
department_read_path = 'dbfs:/FileStore/resource/Department_Q1.csv'
country_read_path = 'dbfs:/FileStore/resource/Country_Q1.csv'

# COMMAND ----------

employee_df = read_csv(employee_read_path)
department_df = read_csv(department_read_path)
country_df = read_csv(country_read_path)

# COMMAND ----------

employee_write_path = 'dbfs:/FileStore/assignment/source_to_bronze/employee'
department_write_path = 'dbfs:/FileStore/assignment/source_to_bronze/department'
country_write_path = 'dbfs:/FileStore/assignment/source_to_bronze/country'

# COMMAND ----------

# DBTITLE 1,write csv
write_csv(employee_df, employee_write_path)
write_csv(department_df, department_write_path)
write_csv(country_df, country_write_path)