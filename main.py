"""
    Joshua Adams - CSE 310
    Sprint 5 SQL Databases
    Movie Rating Database
"""

import sqlite3
from pathlib import Path

# 1. Design the SQLite database schema.
#    - Choose the database file location.
#    - Create movies and ratings tables with primary keys, foreign keys,
#      appropriate data types, and validation constraints.
#    - Initialize the tables when the program starts and enable foreign keys.

DATABASE_PATH = Path(__file__).parent / "movies.db"


def get_connection():
    """Create a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row  # Enable named column access
    connection.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support
    return connection


def initialize_database():
    """Initialize the database schema if it doesn't exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL CHECK (length(trim(title)) > 0),
                release_year INTEGER,
                genre TEXT
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS ratings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER NOT NULL,
                rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
                watched_date TEXT,
                UNIQUE(movie_id),
                FOREIGN KEY (movie_id)
                    REFERENCES movies(id)
                    ON DELETE CASCADE
            )
        """)


# Initialize the database when program starts
if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized at {DATABASE_PATH}")
    

# 2. Implement database queries.
#    - Retrieve all movies, individual movies, and movies searched by title or genre.
#    - Join movies and ratings when displaying rating information.
#    - Handle empty databases and missing movie IDs gracefully.

def get_all_movies():
    """Return all movies with their ratings."""
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT
                movies.id,
                movies.title,
                movies.release_year,
                movies.genre,
                ratings.rating,
                ratings.watched_date
            FROM movies
            LEFT JOIN ratings ON ratings.movie_id = movies.id
            ORDER BY movies.title
        """)
        return cursor.fetchall()


def get_movie_by_id(movie_id):
    """Return one movie with rating information, or None."""
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT
                movies.id,
                movies.title,
                movies.release_year,
                movies.genre,
                ratings.rating,
                ratings.watched_date
            FROM movies
            LEFT JOIN ratings ON ratings.movie_id = movies.id
            WHERE movies.id = ?
        """, (movie_id,))
        return cursor.fetchone()


def search_movies(search_term):
    """Search movie titles or genres"""
    pattern = f"%{search_term}%"

    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT
                movies.id,
                movies.title,
                movies.release_year,
                movies.genre,
                ratings.rating,
                ratings.watched_date
            FROM movies
            LEFT JOIN ratings ON ratings.movie_id = movies.id
            WHERE movies.title LIKE ?
               OR movies.genre LIKE ?
            ORDER BY movies.title
        """, (pattern, pattern))
        return cursor.fetchall()


# 3. Add movies and ratings.
#    - Validate required movie fields and rating values from 1 to 5.
#    - Insert movies and ratings with parameterized SQL statements.
#    - Use transactions, commit successful inserts, and roll back failures.   



# 4. Update existing movies and ratings.
#    - Update movie details and ratings by record ID.
#    - Validate changed values and report when a target record does not exist.





# 5. Delete movies and ratings.
#    - Confirm destructive actions before deleting records.
#    - Preserve referential integrity when deleting movies and related ratings.
#    - Report whether the requested record was deleted.





# 6. Add aggregate rating summaries.
#    - Use AVG and COUNT to summarize ratings for individual movies and the catalog.
#    - Optionally include minimum and maximum ratings.
#    - Handle cases where no ratings exist.





# 7. Optional: add a web interface and external movie information.
#    - Add web routes for viewing, adding, editing, and deleting records.
#    - Optionally integrate poster or external rating information securely.
#    - Reuse database functions, validate form input, and protect API keys.
