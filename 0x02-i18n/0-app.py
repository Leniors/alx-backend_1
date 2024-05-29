#!/usr/bin/env python3
""" simple app """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    """ root """
    return render_template("0-index.html")

if "__main__" == __name__:
    app.run()
