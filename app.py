"""
    Joshua Adams - CSE 310
    Sprint 5 SQL Databases
    Movie Rating Database

    app.py
    This module provides the Flask web interface for the movie rating database.
"""

# Import Flask utilities and the database functions used by the routes.
from flask import Flask, abort, render_template, request

from main import (
    get_all_movies,
    get_movie_by_id,
    get_movie_rating_summary,
    initialize_database,
    search_movies,
)

app = Flask(__name__)

initialize_database()


# Display the complete movie catalog on the home page.
@app.route('/')
def index():
    movies = get_all_movies()
    return render_template('movies.html', movies=movies)


# Display one movie's metadata and rating summary.
@app.route("/movies/<int:movie_id>")
def movie_detail(movie_id):
    try:
        movie = get_movie_by_id(movie_id)
    except ValueError:
        abort(404)

    if movie is None:
        abort(404)

    summary = get_movie_rating_summary(movie_id)

    return render_template(
        "movie_detail.html",
        movie = movie,
        summary = summary,
    )


# Search the catalog by movie title or genre.
@app.route("/search")
def search():
    search_term = request.args.get("q", "").strip()

    if search_term:
        movies = search_movies(search_term)
    else:
        movies = get_all_movies()

    return render_template(
        "movies.html",
        movies=movies,
        search_term=search_term,
    )


if __name__ == "__main__":
    app.run(debug=True)
