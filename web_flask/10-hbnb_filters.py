#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """ Displays an HTML page """
    s = storage.all('State')
    a = storage.all('Amenity')
    return render_template("10-hbnb_filters.html", states=s, amenities=a)


@app.teardown_appcontext
def teardown(exception):
    """ tearsdown connection """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
