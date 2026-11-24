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
2. From the project directory, run `python main.py`.
3. The program creates the local `movies.db` SQLite database and initializes the `movies` and `ratings` tables.

Instructions for using the software:

1. Run `python main.py` to initialize the database.
2. The database layer currently supports retrieving all movies, retrieving a movie by ID, searching by title or genre, adding movies, adding ratings, updating movies and ratings, deleting movies and ratings, and calculating per-movie and catalog-wide rating summaries using `AVG` and `COUNT`.
3. Input validation rejects blank titles, invalid genres, invalid release years, non-positive IDs, ratings outside 1 through 5, malformed watched dates, future watched dates, and invalid input types. Release years are optional; watched dates may be omitted or cleared.
4. These functions can be called from Python code after importing `main.py`. An interactive command-line interface is not currently provided; the browser interface is planned for Step 7.
5. Step 7 will provide browser-based confirmation before destructive delete actions.
6. Do not commit the generated `movies.db` file to source control.

## Development Environment

To recreate the development environment, you need the following software and/or libraries:

* Python 3.x
* Python's built-in `sqlite3` library
* SQLite database support, included with Python

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
