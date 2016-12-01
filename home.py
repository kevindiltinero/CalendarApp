from flask import Flask,url_for, render_template, request
import sqlite3
import json


app= Flask(__name__)



@app.route('/')
def home():
    random = []
    dicty = {'hello':44, 'goodbye':77}
    for key, item in dicty.items():
        random.append(item)
    var = str(random) + "hello"
    return var

if __name__ == "__main__":
    app.run()