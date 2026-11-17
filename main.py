"""
    Joshua Adams - CSE 310
    Sprint 5 SQL Databases
    Movie Rating Database
"""

import sqlite3
print("sqlite3 imported.\n")

# 1. Design the SQLite database schema.
#    - Choose the database file location.
#    - Create movies and ratings tables with primary keys, foreign keys,
#      appropriate data types, and validation constraints.
#    - Initialize the tables when the program starts and enable foreign keys.





# 2. Implement database queries.
#    - Retrieve all movies, individual movies, and movies searched by title or genre.
#    - Join movies and ratings when displaying rating information.
#    - Handle empty databases and missing movie IDs gracefully.





# 3. Add movies and ratings.
#    - Validate required movie fields and rating values from 1 to 10.
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
