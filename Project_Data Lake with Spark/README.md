
# Project - Data Lake
A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to

## Project Datasets
Two datasets that reside in S3. Here are the S3 links for each:

- Song data: s3://udacity-dend/song_data
- Log data: s3://udacity-dend/log_data

## Star Schema
### Fact Table
- songplays - records in log data associated with song plays i.e. records with page NextSong

### Dimension Tables
- users - users in the app
- songs - songs in music database
- artists - artists in music database
- time - timestamps of records in songplays broken down into specific units

## Fils
- `etl.py` reads data from S3, processes that data using Spark and writes them back to S3
- `dl.cfg` contains AWS Credentials. 

## ETL Pipeline
- Load the credentials from `dl.cfg`
- Load the Data which are in JSON Files(Song Data and Log Data)
- After loading the JSON Files from S3 4.Use Spark process this JSON files and then generate a set of Fact and Dimension Tables
- Load back these dimensional process to S3

## Run it
- Replace AWS IAM Credentials in `dl.cfg`
- In the terminal, run python `etl.py`


