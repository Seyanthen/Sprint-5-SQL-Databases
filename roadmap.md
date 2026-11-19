# Movie Rating Database Roadmap

This roadmap describes the planned implementation for the Python and SQLite movie-rating platform. The current repository contains a starter `main.py` with the `sqlite3` import and a `README.md` with the project requirements, so the implementation can be built incrementally from that starting point.

## 1. Design the SQLite Database Schema

**Goal:** Create a persistent SQLite database with tables that represent movies and user ratings.

**Expected implementation tasks:**

- Decide on the database file location, such as `movies.db` in the project directory.
- Create a `movies` table with fields such as `id`, `title`, `release_year`, and `genre`.
- Create a `ratings` table with fields such as `id`, `movie_id`, `rating`, and `watched_date` if separating ratings from movie records.
- Add primary keys, foreign keys, appropriate data types, and validation constraints such as a rating range from 1 to 5.
- Write an initialization function that creates the tables when the program starts.

**Relevant considerations:** Use Python's built-in `sqlite3` module, parameterized SQL statements, and a connection helper that closes connections safely. Enable foreign-key enforcement with `PRAGMA foreign_keys = ON` when related tables are used.

**Requirement satisfied:** Establishes a SQLite database with at least one movie-related table.

**Suggested files or modules:** Expand `main.py` initially; optionally create `database.py` for connection and schema initialization logic. Add `movies.db` to `.gitignore` if the database is generated locally.

## 2. Implement Database Queries

**Goal:** Allow users to view movies and ratings stored in the database.

**Expected implementation tasks:**

- Add a function to retrieve all movies, ordered by title or release year.
- Add a function to retrieve one movie by its ID.
- Add a function to search movies by title or genre.
- Join `movies` and `ratings` when displaying a movie's rating information.
- Format query results into readable console output or data structures for a future interface.

**Relevant considerations:** Use `SELECT` statements with placeholders for user-provided values. Handle an empty database and missing movie IDs gracefully. Use `sqlite3.Row` or explicit column names to make results easier to read.

**Requirement satisfied:** Provides software that queries data from the database.

**Suggested files or modules:** Add query functions to `database.py` or create `movie_repository.py`; update `main.py` with a simple menu or command-line entry point.

## 3. Add Movies and Ratings

**Goal:** Let users add movies they have watched and record their ratings.

**Expected implementation tasks:**

- Create an `add_movie` function that inserts a title and any available metadata.
- Create an `add_rating` function that associates a numeric rating with an existing movie.
- Validate required fields, rating limits, and numeric values before inserting records.
- Use transactions and commit successful inserts.
- Prevent duplicate records where appropriate, such as duplicate movie titles and release years.

**Relevant considerations:** Use parameterized `INSERT` statements and never concatenate raw user input into SQL. Return the inserted record ID so a rating can be associated with the correct movie. Roll back failed transactions and show useful validation messages.

**Requirement satisfied:** Provides software that adds new data to the database.

**Suggested files or modules:** Add insert functions to `movie_repository.py` or `database.py`; add input validation to `main.py` or a separate `validation.py` module.

### Step 2 Query Testing Checkpoint

After Step 3 adds movie and rating insertion functions, test the Step 2 query functions with:

- An empty database.
- Movies with and without ratings.
- Existing and nonexistent movie IDs.
- Partial title and genre searches.
- Searches with no matches.
- Case-insensitive searches where supported by SQLite.
- Alphabetical ordering.
- SQL-injection-safe search values using parameterized queries.

## 4. Update Existing Movies and Ratings

**Goal:** Allow users to correct or revise movie information and ratings.

**Expected implementation tasks:**

- Create an `update_movie` function for editable fields such as title, release year, and genre.
- Create an `update_rating` function for changing an existing rating.
- Identify records by ID and verify that the target exists before updating.
- Display the updated record after a successful operation.
- Track or display the last updated value if that is useful to the user experience.

**Relevant considerations:** Use `UPDATE` statements with parameters and a `WHERE` clause based on the record ID. Check `cursor.rowcount` so the program can distinguish a successful update from a nonexistent record. Validate changed values using the same rules as inserts.

**Requirement satisfied:** Provides software that updates data in the database.

**Suggested files or modules:** Add update functions to `movie_repository.py` or `database.py`; add update commands to the user interface in `main.py`.

## 5. Delete Movies and Ratings

**Goal:** Allow users to remove incorrect or unwanted movie and rating records safely.

**Expected implementation tasks:**

- Create a function to delete a rating by ID.
- Create a function to delete a movie by ID.
- Ask for confirmation before destructive operations.
- Decide whether deleting a movie should also delete its ratings through an explicit cleanup operation or a cascading foreign key.
- Report whether the requested record was deleted.

**Relevant considerations:** Use parameterized `DELETE` statements with precise `WHERE` clauses. Preserve referential integrity with foreign keys and either `ON DELETE CASCADE` or an explicit delete order. Avoid deleting all records accidentally and handle missing IDs clearly.

**Requirement satisfied:** Provides software that deletes data from the database.

**Suggested files or modules:** Add delete functions to `movie_repository.py` or `database.py`; add confirmation and delete commands to `main.py`; update the schema if cascading deletes are selected.

## 6. Add Aggregate Rating Summaries

**Goal:** Summarize numerical rating data so users can understand overall movie and catalog performance.

**Expected implementation tasks:**

- Use `AVG(rating)` to calculate the average rating for a movie or the entire catalog.
- Use `COUNT(rating)` to show how many ratings a movie or the catalog has received.
- Optionally use `MAX(rating)` and `MIN(rating)` to show rating ranges.
- Add a summary command that displays aggregate results in a readable format.
- Handle `NULL` results when no ratings exist.

**Relevant considerations:** Use SQL aggregate functions directly in queries and use `GROUP BY` for per-movie summaries. Consider rounding averages for display while preserving the database's numeric value. Test summaries with no rows, one rating, and multiple ratings.

**Requirement satisfied:** Uses at least two aggregate functions - `AVG` and `COUNT` - to summarize numerical data.

**Suggested files or modules:** Add summary queries to `movie_repository.py` or a separate `reports.py`; add a summary option to `main.py`; document example output in `README.md` after implementation.

## 7. Add an Optional Web Interface and External Movie Information

**Goal:** Provide a browser-based way to manage the database and optionally display movie posters or ratings from an external source.

**Expected implementation tasks:**

- Choose a lightweight Python web framework such as Flask if a web interface is desired.
- Create routes or views for listing movies, viewing details, adding records, editing records, and deleting records.
- Add a poster URL field or integrate a movie information API, subject to API terms and key requirements.
- Display local ratings alongside any external ratings, clearly labeling the source.
- Validate and sanitize form input, and keep API keys in environment variables rather than source control.

**Relevant considerations:** Reuse the database/repository functions instead of duplicating SQL in route handlers. Use templates for presentation, handle network failures gracefully, and protect destructive actions with confirmation and appropriate request methods. This step is optional and should follow completion of the core database features.

**Requirement satisfied:** Provides the optional web interface that can access movie posters and potentially other ratings.

**Suggested files or modules:** Add `app.py`, a `templates/` directory, a `static/` directory, and optionally `api_client.py` or `services/movie_metadata.py`. Update `README.md` with setup, API-key, and run instructions.
