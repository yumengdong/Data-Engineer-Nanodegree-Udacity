## Summary of Project
In this project, I would be applying Data Modeling with Apache Cassandra and complete an ETL pipeline using Python. I am provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

## Dataset 
event_data. This is the directory of CSV files partitioned by date. 

## Files used in this Project
1. Project_1B_ Project_Template.ipynb: This is the final file provided in which all the queries have been written with importing the files, generating a new csv file and loading all csv files into one. All verifying the results whether all tables had been loaded accordingly as per requirement
2. Event_datafile_new.csv: This is the final combination of all the files which are in the folder event_data

##  ETL Pipeline
1. Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
2. Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model
3. Test by running SELECT statements after running the queries on your database


