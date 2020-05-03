from app import app
import flask
import sqlite3
import os
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        flask.session['username'] = username

        db = get_db()
        cursor = db.cursor()
        query = """INSERT INTO users (username) VALUES(?)"""
        cursor.execute(query, (username,))

        query2 = """SELECT * FROM users"""
        cursor.execute(query2)

        data = cursor.fetchall()

        for i in data:
            print(i)



        return flask.redirect(flask.url_for('index'))

    return flask.render_template('login.html')

@app.route('/')
def index():
     return flask.render_template('index.html')

@app.route('/api/usersonline', methods=['GET', 'POST', 'DELETE'])
def getUsers():
    var = {}
    db = get_db()
    cursor = db.cursor()
    query = "SELECT username FROM users"
    exCursor = cursor.execute(query)
    data = exCursor.fetchall()

    #print(data)

    peopleList = []
    for d in data:
        peopleList.append(d)

    var["people"] = peopleList
    
    return flask.jsonify(**var)

@app.route('/api/trees/alive', methods=['GET', 'POST'])
def trees():
    var = {}
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM rooms"
    exCursor = cursor.execute(query)
    data = exCursor.fetchall()
    for element in data:
        var["rooms"] = element
    #print(data)

    if flask.request.method == 'POST':

        query = "SELECT numAlive FROM rooms WHERE room = (?)"
        exCursor = cursor.execute(query, ("0"))
        data = exCursor.fetchall()[0]['numAlive'] + 1

        print("ALIVEEEEEEEEEEEEEEEEEEEEEEE", data)


        
        query = """UPDATE rooms
              SET numAlive = ?
              WHERE room = ?"""


        

        cursor.execute(query, (data, "0"))
    
    return flask.jsonify(**var)

@app.route('/api/trees/dead', methods=['GET', 'POST'])
def treesdead():
    var = {}
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM rooms"
    exCursor = cursor.execute(query)
    data = exCursor.fetchall()
    for element in data:
        var["rooms"] = element
    #print(data)

    if flask.request.method == 'POST':

        query = "SELECT numDead FROM rooms WHERE room = (?)"
        exCursor = cursor.execute(query, ("0"))
        data = exCursor.fetchall()[0]['numDead'] + 1

        print("deeeeeeeeeeeeeAAAAAAAAAAAD", data)


        
        query = """UPDATE rooms
              SET numDead = ?
              WHERE room = ?"""


        

        cursor.execute(query, (data, "0"))


    
    


    # peopleList = []
    # for d in data:
    #     peopleList.append(d)

    # var["people"] = peopleList
    
    return flask.jsonify(**var)

@app.template_filter()
def vue(item):
    # If you see anything about "raw", blame the blog engine, not me. If not,
    # ignore these comments.
    print("HELOOOOOOO")
    return "{{ " + item + " }}"


DATABASE_FILENAME = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
'var', 'study.sqlite3')

def get_db():
    """Open a new database connection."""
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = sqlite3.connect(
            DATABASE_FILENAME)
        flask.g.sqlite_db.row_factory = dict_factory

        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db

def dict_factory(cursor, row):
    """Convert database row objects to a dictionary.

    This is useful for building dictionaries
    which are then used to render a template.
    Note that this would be inefficient for large queries.
    """
    output = {}
    for idx, col in enumerate(cursor.description):
        output[col[0]] = row[idx]
    return output

@app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request."""
    # Assertion needed to avoid style error
    assert error or not error
    if hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db.commit()
        flask.g.sqlite_db.close()

