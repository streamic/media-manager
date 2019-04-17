import sqlite3

con = sqlite3.connect('media.db')

with con:
    # Create movies table
    con.execute('''CREATE TABLE IF NOT EXISTS movies(
                    id_movie INT PRIMARY KEY,
                    vote_average REAL,
                    poster_path TEXT,
                    original_title TEXT,
                    backdrop_path TEXT,
                    overview TEXT,
                    release_date TEXT,
                    file_path TEXT
                )''')

    # Create genres table
    con.execute('''CREATE TABLE IF NOT EXISTS genres(
                    id_genre INT PRIMARY KEY,
                    name TEXT
                )''')

    # Create movie_genres Many to Many relationship table
    con.execute('''CREATE TABLE IF NOT EXISTS movie_genres(
                    id_genre INT,
                    id_movie INT,
                        FOREIGN KEY (id_genre) REFERENCES genres(id_genre)  
                        FOREIGN KEY (id_movie) REFERENCES movies(id_movie)
                )''')
