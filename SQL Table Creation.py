# Databricks notebook source
# SQL Table Creation with the same columns mapped to the sales.csv file uploaded
%sql

CREATE OR REPLACE TABLE dev.sales_db.sales(
    OrderID INT,
    OrderDate DATE,
    CustomerID STRING,
    Product STRING,
    Category STRING,
    Region STRING,
    Quantity INT,
    UnitPrice DOUBLE
)