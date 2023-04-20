#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'
