## Summary of Project
Create ETL data pipeline to load data in a S3 bucket and wrangle them into a star schema

## Files used in this Project
1. create_table.py: create your fact and dimension tables for the star schema in Redshift.
2. etl.py: load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
3. sql_queries.py: define  SQL statements, which will be imported into the two other files above.

## Run it
```bash
python create_tables.py
```

```bash
python etl.py
```
