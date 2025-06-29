import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# # Create table and insert data on it.
# with sqlite3.connect("db.sqlite3") as conn:
#     # Create the Movies table (adjust column types as needed)
#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS Movies (
#             id INTEGER PRIMARY KEY,
#             title TEXT NOT NULL,
#             year INTEGER NOT NULL
#         )
#     """)
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()
#     cursor = conn.execute("SELECT * FROM Movies")
#     print(cursor.fetchall())


# Read data from sqlite3 database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
