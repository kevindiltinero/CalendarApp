from flask import Flask, g
import sqlite3

app = Flask(__name__)
DATABASE = 'dublinbikes_3.db'

#Connect to database
def connect_to_database():
    return sqlite3.connect(DATABASE)

#Get the database
def get_db():
    db = getattr(g, '_database',	None)
    if db is None:
        db = g._database = connect_to_database()
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database',	None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    conn = get_db()
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)