# Databricks notebook source
# Data Cleaning from target location before injestion and Data Injestion 
class DataLoader():

    def __init__(self):
        self.catalog = "dev"
        self.db = "sales_db"
        self.volume_name = "datasets"

    def cleanup_dir(self, dest_path):
        print(f"Cleaning {dest_path}...", end="")
        dbutils.fs.rm(dest_path, recurse=True)
        dbutils.fs.mkdirs(dest_path)
        print("Done")

    def clean_ingest_data(self, source, dest):

        import requests

        dest_path = f"/Volumes/{self.catalog}/{self.db}/{self.volume_name}/{dest}"

        self.cleanup_dir(dest_path)

        download_url = "https://raw.githubusercontent.com/SangitaDeori/Sales_Analysis/main/sales.csv"

        filename = "sales.csv"

        print("Downloading file...", end="")

        with requests.get(download_url, stream=True) as r:
            with open(f"{dest_path}/{filename}", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print("Done")

# COMMAND ----------

DL = DataLoader()

DL.clean_ingest_data("", "sales")

# COMMAND ----------

display(
    dbutils.fs.ls("/Volumes/dev/sales_db/datasets/sales")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE dev.sales_db.sales(
# MAGIC     OrderID INT,
# MAGIC     OrderDate DATE,
# MAGIC     CustomerID STRING,
# MAGIC     Product STRING,
# MAGIC     Category STRING,
# MAGIC     Region STRING,
# MAGIC     Quantity INT,
# MAGIC     UnitPrice DOUBLE
# MAGIC )

# COMMAND ----------

display(
    dbutils.fs.ls("/Volumes/dev/sales_db/datasets/sales")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO dev.sales_db.sales
# MAGIC
# MAGIC SELECT *
# MAGIC FROM csv.`/Volumes/dev/sales_db/datasets/sales/sales.csv`

# COMMAND ----------

sales_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("/Volumes/dev/sales_db/datasets/sales/sales.csv")

display(sales_df)

# COMMAND ----------

sales_df.createOrReplaceTempView("sales_csv")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO dev.sales_db.sales
# MAGIC
# MAGIC SELECT *
# MAGIC FROM sales_csv

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM dev.sales_db.sales

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     Product,
# MAGIC     SUM(Quantity * UnitPrice) AS Revenue
# MAGIC FROM dev.sales_db.sales
# MAGIC GROUP BY Product
# MAGIC ORDER BY Revenue DESC