from app import app
import flask
import sqlite3
import os

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        flask.session['username'] = username

        return flask.redirect(flask.url_for('index'))

    return flask.render_template('login.html')

@app.route('/')
def index():
     return flask.render_template('index.html')

    

    


# DATABASE_FILENAME = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
# 'var', 'study.sqlite3')

# def get_db():
#     """Open a new database connection."""
#     if not hasattr(flask.g, 'sqlite_db'):
#         flask.g.sqlite_db = sqlite3.connect(
#             DATABASE_FILENAME)
#         flask.g.sqlite_db.row_factory = dict_factory

#         # Foreign keys have to be enabled per-connection.  This is an sqlite3
#         # backwards compatibility thing.
#         flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

#     return flask.g.sqlite_db

# def dict_factory(cursor, row):
#     """Convert database row objects to a dictionary.

#     This is useful for building dictionaries
#     which are then used to render a template.
#     Note that this would be inefficient for large queries.
#     """
#     output = {}
#     for idx, col in enumerate(cursor.description):
#         output[col[0]] = row[idx]
#     return output


