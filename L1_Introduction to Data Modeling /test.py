query = "CREATE TABLE IF NOT EXISTS songs "
query = query + "(year int, song_title text, artist_name text, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)


## TO-DO: Complete the query below
query = "CREATE TABLE IF NOT EXISTS songs "
query = query + "(year int, song_title text, artist_name test, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)
