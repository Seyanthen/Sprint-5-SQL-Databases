# Movie Rating Database Roadmap

This roadmap describes the planned implementation for the Python and SQLite movie-rating platform. The current repository contains a starter `main.py` with the `sqlite3` import and a `README.md` with the project requirements, so the implementation can be built incrementally from that starting point.

## Current Status

The first status update below and the stage status labels in Step 7 are the authoritative current status.

Status update: Steps 1-6 remain implemented. Stages 7.1 and 7.2 of the required web interface are now implemented and verified. The Flask application displays the catalog, movie metadata, local ratings, watched dates, per-movie rating summaries, title and genre search results, and clear 404 responses for invalid or nonexistent movie IDs. Validation now covers required text fields, optional genres and release years, release-year bounds, positive record IDs, ratings from 1 through 5, ISO watched dates, future-date rejection, and invalid input types including booleans. The next implementation step is Stage 7.3: adding browser forms for movies and ratings.

Steps 1–6 are implemented. Steps 4–6 have been verified with isolated assert-based tests covering successful updates and deletions, invalid input, nonexistent IDs, rating date preservation, date clearing, cascading deletion of ratings when a movie is deleted, empty summaries, unrated movies, per-movie summaries, catalog summaries, and alphabetical ordering. Confirmation for destructive actions will be implemented as part of the required Step 7 web interface. The next implementation step is Step 7: adding the required web interface.

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

**Testing task:** Create a test function that uses Python `assert` statements to verify the Step 3 insertion functions and the Step 4 update functions. Include successful inserts and updates, invalid input, nonexistent IDs, duplicate ratings, and confirmation that failed operations do not create unintended records.

**Requirement satisfied:** Provides software that updates data in the database.

**Suggested files or modules:** Add update functions to `movie_repository.py` or `database.py`; add update commands to the user interface in `main.py`.

### Step 4 Testing Checkpoint

Run the assert-based test function against an isolated test database and verify:

- A valid movie and rating can be inserted.
- Invalid movie and rating values are rejected.
- A movie and rating can be updated successfully.
- Updates to nonexistent IDs are reported correctly.
- Duplicate ratings are rejected according to the schema.
- Failed inserts and updates leave the database unchanged.

## 5. Delete Movies and Ratings

**Goal:** Allow users to remove incorrect or unwanted movie and rating records safely.

**Expected implementation tasks:**

- Create a function to delete a rating by ID.
- Create a function to delete a movie by ID.
- Defer user confirmation for destructive operations to the Step 7 web interface.
- Decide whether deleting a movie should also delete its ratings through an explicit cleanup operation or a cascading foreign key.
- Report whether the requested record was deleted.

**Relevant considerations:** Use parameterized `DELETE` statements with precise `WHERE` clauses. Preserve referential integrity with foreign keys and either `ON DELETE CASCADE` or an explicit delete order. Avoid deleting all records accidentally and handle missing IDs clearly.

**Requirement satisfied:** Provides software that deletes data from the database.

**Suggested files or modules:** Add delete functions to `movie_repository.py` or `database.py`; implement delete confirmation in the Step 7 web interface; update the schema if cascading deletes are selected.

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

## 7. Add the Required Web Interface and External Movie Information

**Goal:** Provide a browser-based way to manage the database, including confirmation for destructive actions, and display movie posters or ratings from an external source when available.

**Expected implementation tasks:**

- Choose a lightweight Python web framework such as Flask.
- Create routes or views for listing movies, viewing details, adding records, editing records, and deleting records.
- Add a confirmation step for destructive actions before submitting delete requests.
- Add a poster URL field or integrate a movie information API, subject to API terms and key requirements.
- Display local ratings alongside any external ratings, clearly labeling the source.
- Validate and sanitize form input, and keep API keys in environment variables rather than source control.

**Relevant considerations:** Reuse the database/repository functions instead of duplicating SQL in route handlers. Use templates for presentation, handle network failures gracefully, and protect destructive actions with confirmation and appropriate request methods. This required step should follow completion of the core database features.

**Requirement satisfied:** Provides the required web interface that can access movie posters and potentially other ratings.

**Suggested files or modules:** Add `app.py`, a `templates/` directory, a `static/` directory, and optionally `api_client.py` or `services/movie_metadata.py`. Update `README.md` with setup, API-key, and run instructions.

### Step 7 Implementation Path

The web interface will be implemented gradually so that each stage produces a usable and testable result. The existing database functions in `main.py` should be reused rather than rewritten in the web routes.

#### Stage 7.1: Create a Minimal Flask Shell

**Goal:** Start the web server and display the current movie catalog in a browser.

**Tasks:**

- Add Flask as a project dependency.
- Create `app.py` and configure a Flask application.
- Add a `/` route that calls `get_all_movies()` from `main.py`.
- Add `templates/movies.html` to display movie titles, genres, release years, and local ratings.
- Initialize the database when the application starts or document the required initialization command.
- Verify that an empty database and a database containing movies both render successfully.

**Checkpoint:** Running the Flask development server and opening the home page displays the catalog without duplicating SQL in `app.py`.

**Status:** Complete. The Flask shell and catalog page render successfully with empty and populated database states.

#### Stage 7.2: Add Movie Details and Search

**Goal:** Let users inspect individual movies and find movies by title or genre.

**Tasks:**

- Add a route such as `/movies/<int:movie_id>` that calls `get_movie_by_id()`.
- Add a search form that submits to a route using `search_movies()`.
- Handle nonexistent movie IDs with a clear page or 404 response.
- Display local rating details and per-movie summaries where appropriate.

**Checkpoint:** Users can open a movie detail page, search the catalog, and receive a useful result when no movies match.

**Status:** Complete. Detail pages, title and genre searches, no-match messaging, and 404 handling have been implemented and verified with Flask route tests.

#### Stage 7.3: Add Movie and Rating Forms

**Goal:** Move the existing create operations from Python-only usage into browser forms.

**Tasks:**

- Add a movie form that submits to a POST route calling `add_movie()`.
- Add a rating form that submits to a POST route calling `add_rating()`.
- Convert form values to the expected Python types before calling the database functions.
- Display validation errors from `main.py` in the form page.
- Redirect to the created movie or catalog after a successful submission.

**Checkpoint:** A user can add a movie and rating through the browser, while invalid input is rejected without creating partial records.

#### Stage 7.4: Add Editing and Safe Deletion

**Goal:** Provide the remaining CRUD operations with an intentional confirmation step for destructive actions.

**Tasks:**

- Add edit forms and POST routes that call `update_movie()` and `update_rating()`.
- Add a delete-confirmation page before calling `delete_movie()` or `delete_rating()`.
- Use POST for the final delete action rather than deleting from a link or GET request.
- Display success and error messages after updates and deletions.

**Checkpoint:** Users can edit records and must explicitly confirm before a movie or rating is deleted.

#### Stage 7.5: Add Catalog Summaries and Basic Presentation

**Goal:** Make the web interface communicate the aggregate information already supported by the database.

**Tasks:**

- Add catalog-wide `AVG` and `COUNT` results to the home page or a summary page.
- Display per-movie summary information where useful.
- Add a shared `templates/base.html` layout.
- Add `static/style.css` for readable tables, forms, navigation, and error messages.
- Test empty, unrated, and rated catalogs in the browser.

**Checkpoint:** The interface presents the catalog and rating summaries clearly across the supported empty and populated states.

#### Stage 7.6: Add External Movie Information

**Goal:** Display movie posters or external ratings when available without making the local application dependent on the external service.

**Tasks:**

- Select an API and review its request limits, terms, and API-key requirements.
- Add an `api_client.py` or `services/movie_metadata.py` module instead of placing API calls directly in routes.
- Store API keys in environment variables, never in source control.
- Decide whether poster URLs should be stored in the database or fetched when details are displayed.
- Handle missing results, timeouts, rate limits, and service failures gracefully.
- Clearly label local ratings separately from external ratings.

**Checkpoint:** A movie detail page can show external information when available and still works when the external service is unavailable.

#### Stage 7.7: Refactor and Document the Web Version

**Goal:** Make the completed application easier to maintain and use.

**Tasks:**

- If `main.py` becomes difficult to maintain, move database operations into `database.py` and validation helpers into `validation.py` without changing their behavior.
- Add a `requirements.txt` file with the web dependencies.
- Update the README build, use, and development-environment instructions with Flask setup and server commands.
- Add browser-level or route-level tests using an isolated temporary database.
- Confirm that `movies.db`, API keys, and other local secrets are excluded from source control.

**Final Step 7 checkpoint:** The browser interface supports querying, adding, updating, deleting with confirmation, aggregate summaries, and optional external movie information while preserving the existing database behavior.
