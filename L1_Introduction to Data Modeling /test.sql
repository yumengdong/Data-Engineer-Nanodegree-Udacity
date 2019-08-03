## TO-DO: Finish the INSERT INTO statement with the correct arguments

try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 ("Across The Universe", "The Beatles", 1970, "Let It Be", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single) \
                  VALUES (%s, %s, %s, %s, %s)", \
                  ("Think For Yourself", "The Beatles", 1965, "Rubber Soul", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)


try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 ("Across The Universe", "The Beatles", 1970, "Let It Be", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO songs (song_title, artist_name, year, album_name, single) \
                  VALUES (%s, %s, %s, %s, %s)",
                  ("Think For Yourself", "The Beatles", 1965, "Rubber Soul", False))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)