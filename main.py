"""
    Joshua Adams - CSE 310
    Sprint 5 SQL Databases
    Movie Rating Database
"""

import sqlite3
from pathlib import Path
from contextlib import contextmanager

# 1. Design the SQLite database schema.
#    - Choose the database file location.
#    - Create movies and ratings tables with primary keys, foreign keys,
#      appropriate data types, and validation constraints.
#    - Initialize the tables when the program starts and enable foreign keys.

DATABASE_PATH = Path(__file__).parent / "movies.db"

# Shared Movie Query
MOVIE_WITH_RATING_QUERY = """
    SELECT
        movies.id,
        movies.title,
        movies.release_year,
        movies.genre,
        ratings.rating,
        ratings.watched_date
    FROM movies
    LEFT JOIN ratings ON ratings.movie_id = movies.id
"""


@contextmanager
def get_connection():
    """Open a database connection and close it automatically."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row  # Enable named column access
    connection.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support

    try:
        yield connection
        connection.commit()  # Commit changes if no exceptions occur
    except Exception:
        connection.rollback()  # Roll back changes on error
        raise
    finally:
        connection.close()  # Ensure the connection is closed


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
    query = MOVIE_WITH_RATING_QUERY + """
        ORDER BY movies.title
    """

    with get_connection() as connection:
        cursor = connection.execute(query)
        return cursor.fetchall()


def get_movie_by_id(movie_id):
    """Return one movie with rating information, or None."""
    query = MOVIE_WITH_RATING_QUERY + """
        WHERE movies.id = ?
    """

    with get_connection() as connection:
        cursor = connection.execute(query, (movie_id,))
        return cursor.fetchone()


def search_movies(search_term):
    """Search movie titles or genres."""
    pattern = f"%{search_term}%"

    query = MOVIE_WITH_RATING_QUERY + """
        WHERE movies.title LIKE ?
           OR movies.genre LIKE ?
        ORDER BY movies.title
    """
    
    with get_connection() as connection:
        cursor = connection.execute(query, (pattern, pattern))
        return cursor.fetchall()


# 3. Add movies and ratings.
#    - Validate required movie fields and rating values from 1 to 5.
#    - Insert movies and ratings with parameterized SQL statements.
#    - Use transactions, commit successful inserts, and roll back failures.   

def add_movie(title, release_year=None, genre=None):
    """Add a movie and return its generated ID."""
    if not title or not title.strip():
        raise ValueError("Movie title is required.")

    with get_connection() as connection:
        cursor = connection.execute("""
            INSERT INTO movies (title, release_year, genre)
            VALUES (?, ?, ?)
            """,
            (title.strip(), release_year, genre.strip() if genre else None)
        )
        return cursor.lastrowid


def add_rating(movie_id, rating, watched_date=None):
    """Add a rating for an existing movie."""
    if not isinstance(rating, int) or not 1 <= rating <= 5:
        raise ValueError("Rating must be an integer from 1 to 5.")

    with get_connection() as connection:
        # Check if the movie exists
        cursor = connection.execute("SELECT id FROM movies WHERE id = ?", (movie_id,))
        if cursor.fetchone() is None:
            raise ValueError(f"Movie with ID {movie_id} does not exist.")

        # Insert the rating
        connection.execute("""
            INSERT INTO ratings (movie_id, rating, watched_date)
            VALUES (?, ?, ?)
            """,
            (movie_id, rating, watched_date)
        )




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
