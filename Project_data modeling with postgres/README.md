## Summary of Project
Create ETL data pipeline for analysis that transfer data from JSON files in Postgres using python and SQL

## Files used in this Project
1. test.ipynb: displays the first few rows of each table to let you check your database.
2. create_tables.py: drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. etl.ipynb: reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py: reads and processes files from song_data and log_data and loads them into your tables. 
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.


## Run it
```bash
python create_tables.py
```

```bash
python etl.py
```


