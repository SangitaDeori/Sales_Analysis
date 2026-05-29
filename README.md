# Mini Sales Data Analysis Project

A mini data engineering and analytics project that processes retail sales data using Databricks and PySpark.

## 📌 Project Overview
This project ingests a raw retail sales dataset (`.csv` format), cleans the data, handles missing values, and performs exploratory data analysis (EDA) inside Databricks. The goal is to extract key sales insights such as monthly revenue trends, top-selling products, and regional performance.

## 🛠️ Tech Stack & Tools
* **Platform:** Databricks Community Edition / Cloud
* **Language:** PySpark (Python) / Spark SQL
* **Storage:** Databricks File System (DBFS)
* **Data Format:** CSV

## 📂 Repository Structure
* `data/` - Contains the raw sales CSV dataset used for the analysis.
* `notebooks/` - Databricks notebook exports (HTML or Python scripts) containing the source code.
* `README.md` - Project documentation and setup guide.

## 📊 Dataset Description
The source file `[sales].csv` contains transactional retail data with the following key attributes:
* `Transaction_ID`: Unique identifier for each sale.
* `Date`: Date of the transaction.
* `Product_Category`: Grouping of items sold (e.g., Electronics, Clothing).
* `Quantity`: Number of units purchased.
* `Price_Per_Unit`: Price of a single item.
* `Total_Amount`: Total revenue generated from the transaction.

## 🚀 Key Insights & Analytics
The Databricks notebooks cover:
1. **Data Cleaning:** Removing duplicates and formatting date types.
2. **Sales Performance:** Identifying the highest-earning product categories.
3. **Time-Series Analysis:** Mapping revenue growth month-over-month.
4. **Customer Behavior:** Analyzing average order value (AOV) across different demographics.

## Business Insights

- Laptop generated the highest revenue.
- Electronics category outperformed Accessories.
- North region contributed the highest sales revenue.
- Revenue trends can be analyzed by Order Date.

## Architecture

1. Sales data is stored in a GitHub repository as a CSV file.
2. Databricks downloads the file from GitHub into a Unity Catalog Volume.
3. PySpark reads the CSV file and infers the schema.
4. Data is loaded into a Delta Table within Unity Catalog.
5. SQL queries are executed to analyze revenue and sales performance.
6. Databricks Dashboards visualize business insights.

## 🔧 How to Run the Project
1. Clone this repository to your local machine or download the files.
2. Log into your **Databricks** account.
3. Upload the `[sales].csv` file to **DBFS** via the Data Ingestion tab.
4. Import the provided notebook file from the `notebooks/` directory into your Databricks workspace.
5. Attach the notebook to an active Spark cluster and click **Run All**.
