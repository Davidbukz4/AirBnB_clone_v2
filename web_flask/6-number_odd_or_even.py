#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, escape, redirect, url_for, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Returns the string """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns the string """
    return 'HBNB'


@app.route('/c/<text>')
def cee(text):
    """ Returns the string """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """ Returns the string """
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>')
def number(n):
    """ Returns the string """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_temp(n):
    """ Returns a string """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """ Returns a string """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
