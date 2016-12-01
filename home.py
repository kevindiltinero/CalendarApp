from flask import Flask,url_for, render_template, request, g
import sqlite3
import json


app = Flask(__name__)

DATABASE = '/var/www/html/FlaskApps/CalendarApp/calendar.db'

app.config.from_object(__name__)

# def connect_to_database():
#     return sqlite3.connect(app.config['DATABASE'])
#
# def get_db():
#     db = getattr(g, 'db', None)
#     if db is None:
#         db = g.db = connect_to_database()
#     return db
#
# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()
#
# def execute_query(query, args=()):
#     cur = get_db().execute(query, args)
#     rows = cur.fetchall()
#     cur.close()
#     return rows


@app.route('/')
def home():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    # command = "SELECT * FROM calendarevents"
    # c.execute(command)
    # results = c.fetchall()
    # results = results[0][1]
    results = "goodbye"

    return results


if __name__ == "__main__":
    app.run()