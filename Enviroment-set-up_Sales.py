# Databricks notebook source
''' Set Up Enviroment 
1. Setup Catalog, Database and Volume
Create a catalog - dev
Create a database - dev.spark_db
Create a volume - dev.spark_db.datasets'''
%sql
CREATE CATALOG IF NOT EXISTS dev;
CREATE DATABASE IF NOT EXISTS dev.sales_db;
CREATE VOLUME IF NOT EXISTS dev.sales_db.datasets;