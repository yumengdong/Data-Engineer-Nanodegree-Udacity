import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

IAM_ROLE = config['IAM_ROLE']['ARN']
LOG_DATA = config['S3']['LOG_DATA']
SONG_DATA = config['S3']['SONG_DATA']
LOG_JSONPATH = config['S3']['LOG_JSONPATH']


# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events_table"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs_table"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES
#stage table for events.json/log_data and song_data

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events(
                                        event_id        INT IDENTITY(0, 1)  NOT NULL    SORTKEY DISTKEY,
                                        artist          VARCHAR,
                                        auth            VARCHAR,
                                        firstname       VARCHAR,
                                        gender          VARCHAR,
                                        itemInSession   INTEGER,
                                        lastname        VARCHAR,
                                        length          FLOAT,
                                        level           VARCHAR,
                                        location        VARCHAR,
                                        method          VARCHAR,
                                        page            VARCHAR,
                                        registrtion     BIGINT,
                                        sessionId       INTEGER,
                                        song            VARCHAR,
                                        status          INTEGER,
                                        ts              TIMESTAMP,
                                        userAgent       VARCHAR,
                                        userId          INTEGER)                                      
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs(
                                        num_songs INTEGER SORTKEY DISTKEY,
                                        artist_id VARCHAR,
                                        artist_latitude NUMERIC,
                                        artist_longitude NUMERIC,
                                        artist_location VARCHAR,
                                        artist_name VARCHAR,
                                        song_id VARCHAR,
                                        title VARCHAR,
                                        duration NUMERIC,
                                        year INTEGER)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table(
                                        songplay_id     INTEGER IDENTITY(0,1) PRIMARY KEY SORTKEY,
                                        start_time      timestamp, 
                                        user_id         varchar, 
                                        level           varchar, 
                                        song_id         varchar, 
                                        artist_id       varchar,
                                        session_id      varchar,
                                        location        varchar,
                                        user_agent      varchar)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table(
                                        user_id         INTEGER PRIMARY KEY DISTKEY,
                                        first_name      varchar,
                                        last_name       varchar,
                                        gender          varchar, 
                                        level           varchar)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table(
                                        song_id         varchar NOT NULL PRIMARY KEY,
                                        title           varchar,
                                        artist_id       varchar DISTKEY,
                                        year            int,
                                        duration        NUMERIC)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table(
                                        artist_id       varchar NOT NULL PRIMARY KEY DISTKEY,
                                        name            varchar,
                                        location        varchar,
                                        latitude        NUMERIC,
                                        longitude       NUMERIC)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table(
                                        start_time      TIMESTAMP PRIMARY KEY DISTKEY, 
                                        hour            int,
                                        day             int,
                                        week            int,
                                        month           int,
                                        year            int,
                                        weekday         int)
""")



# STAGING TABLES

staging_events_copy = ("""
                COPY staging_events
                FROM {}
                iam_role {}
                JSON {};
""").format(LOG_DATA, IAM_ROLE, LOG_JSONPATH)


staging_songs_copy = ("""
                COPY staging_songs
                FROM {}
                iam_role {}
                JSON 'auto';
""").format(SONG_DATA, IAM_ROLE)

# FINAL TABLES

songplay_table_insert = ("""INSERT INTO songplay(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            SELECT  timestamp 'epoch' + se.ts/1000 * interval '1 second' as start_time, se.user_id, se.level, 
                                    ss.song_id, ss.artist_id, se.session_id, se.location, se.user_agent
                            FROM staging_events se, staging_songs ss
                            WHERE se.page = 'NextSong' AND
                            se.song =ss.title AND
                            se.artist = ss.artist_name AND
                            se.length = ss.duration
""")

user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
                        SELECT distinct  user_id, first_name, last_name, gender, level
                        FROM staging_events
                        WHERE page = 'NextSong'
""")

song_table_insert = ("""INSERT INTO song(song_id, title, artist_id, year, duration)
                        SELECT song_id, title, artist_id, year, duration
                        FROM staging_songs
                        WHERE song_id IS NOT NULL
""")

artist_table_insert = ("""INSERT INTO artist(artist_id, name, location, latitude, longitude)
                          SELECT distinct artist_id, artist_name, artist_location , artist_latitude, artist_longitude 
                          FROM staging_songs
                          WHERE artist_id IS NOT NULL
""")

time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekDay)
                        SELECT start_time, extract(hour from start_time), extract(day from start_time),
                                extract(week from start_time), extract(month from start_time),
                                extract(year from start_time), extract(dayofweek from start_time)
                        FROM songplay
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
