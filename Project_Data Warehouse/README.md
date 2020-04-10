## Summary of Project
Create ETL data pipeline to load data in a S3 bucket and wrangle them into a star schema

## Dataset Source
Two datasets that reside in S3. Here are the S3 links for each:
- Song data: s3://udacity-dend/song_data
- Log data: s3://udacity-dend/log_data

## Schema 
Create start schema. <br>
Fact Table: 
- songplays

Dimension Tables:
- users, songs, artists, time

Create Table Schemas:
1. Design schemas for your fact and dimension tables
2. Write a SQL CREATE statement for each of these tables in `sql_queries.py`
3. Complete the logic in `create_tables.py` to connect to the database and create these tables
4. Write SQL DROP statements to drop tables in the beginning of `create_tables.py` if the tables already exist. This way, you can run `create_tables.py` whenever you want to reset your database and test your ETL pipeline.
5. Launch a redshift cluster and create an IAM role that has read access to S3.
6. Add redshift database and IAM role info to `dwh.cfg`.
7. Test by running `create_tables.py` and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

## Files used in this Project
- create_table.py: create your fact and dimension tables for the star schema in Redshift.
- etl.py: load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
- sql_queries.py: define  SQL statements, which will be imported into the two other files above.

## Build ETL Pipeline
- Implement the logic in `etl.py` to load data from S3 to staging tables on Redshift.
- Implement the logic in `etl.py` to load data from staging tables to analytics tables on Redshift.
- Test by running `etl.py` after running `create_tables.py` and running the analytic queries on your Redshift database to compare your results with the expected results.
- Delete your redshift cluster when finished.

## Steps
- Write the configuration of AWS Cluster, store the important parameter in some other file
- Configuration of boto3 which is an AWS SDK for Python
- Create an IAM User Role, Assign appropriate permissions and create the Redshift Cluster
- Get the Value of Endpoint and Role for put into main configuration file
- Authorize Security Access Group to Default TCP/IP Address
- Launch database connectivity configuration
- Go to Terminal write the command "python create_tables.py" and then "etl.py"

## Run it
```bash
python create_tables.py
```

```bash
python etl.py
```
