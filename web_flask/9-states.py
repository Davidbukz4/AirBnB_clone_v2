#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states", strict_slashes=False)
def states():
    """ Returns an html page """
    states = storage.all("State")
    return render_template("9-states.html", items=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", items=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """ tearsdown connection """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
