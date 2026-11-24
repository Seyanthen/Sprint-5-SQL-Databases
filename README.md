# Sprint-5-SQL-Databases
Movie Rating Database: A platform where users can track movies they've watched and give ratings.

Project Requirements:
1. Create a SQL database with at least one table.
2. Software should query data from the database.
3. Software should add new data to the database.
4. Software should update data from the database.
5. Software should delete data from the database.

Stretch Challenge:
- Use at least two of the aggregate functions to summarize numerical data in your database.


## Instructions for Build and Use

Steps to build and/or run the software:

1. Install Python 3.x if it is not already installed.
2. Activate the project virtual environment with `.\\.venv\\Scripts\\Activate.ps1`.
3. Install Flask in the virtual environment with `python -m pip install Flask` if it is not already installed.
4. From the project directory, run `python app.py`.
5. Open the local address shown by Flask, usually `http://127.0.0.1:5000/`. The application creates the local `movies.db` SQLite database and initializes the `movies` and `ratings` tables.

Instructions for using the software:

1. Run `python app.py` to start the web interface and initialize the database.
2. The browser interface currently displays the movie catalog, movie metadata, local ratings, watched dates, per-movie rating summaries, and title or genre search results.
3. The database layer supports adding, updating, and deleting movies and ratings, as well as calculating per-movie and catalog-wide rating summaries using `AVG` and `COUNT`.
4. Input validation rejects blank titles, invalid genres, invalid release years, non-positive IDs, ratings outside 1 through 5, malformed watched dates, future watched dates, and invalid input types. Release years are optional; watched dates may be omitted or cleared.
5. Browser forms, delete confirmation, and external movie information remain planned for later Step 7 stages.
6. Do not commit the generated `movies.db` file or API keys to source control.

## Development Environment

To recreate the development environment, you need the following software and/or libraries:

* Python 3.x
* Python's built-in `sqlite3` library
* SQLite database support, included with Python
* Flask 3.x
* A project virtual environment in `.venv`

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
* [SQL Database Wiki](https://en.wikipedia.org/wiki/Relational_database)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [Python sqlite3](https://docs.python.org/3.13/library/sqlite3.html)
* [TutorialsPoint: SQLite - Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

## Future Work

The following items reflect the current roadmap status and planned improvements:

* [x] Step 1: Create the SQLite database schema and initialization function
* [x] Step 2: Add database query functions
* [x] Step 3: Add movies and ratings
* [x] Step 4: Update existing movies and ratings
* [x] Step 5: Delete movies and ratings
* [x] Step 6: Add aggregate rating summaries using `AVG` and `COUNT`
* [ ] Step 7: Add the required web interface, delete confirmations, and movie posters
  * [x] Stage 7.1: Create a minimal Flask shell and catalog page
  * [x] Stage 7.2: Add movie details and title or genre search
  * [ ] Stage 7.3: Add movie and rating forms
  * [ ] Stage 7.4: Add editing and safe deletion with confirmation
  * [ ] Stage 7.5: Add catalog summaries and basic presentation
  * [ ] Stage 7.6: Add external movie information
  * [ ] Stage 7.7: Refactor and document the web version
