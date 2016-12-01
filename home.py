from flask import Flask,url_for, render_template, request
import sqlite3
import json


app= Flask(__name__)



@app.route('/')
def home():
    conn = sqlite3.connect('calendar.db')
    c = conn.cursor()
    # command = "SELECT * FROM calendarevents"
    # c.execute(command)
    # results = c.fetchall()
    # results = results[0][1]
    results = "goodbye"

    return results

if __name__ == "__main__":
    app.run()