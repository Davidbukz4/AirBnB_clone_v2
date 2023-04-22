#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """ Returns the state info """
    states = storage.all('State')
    return render_template('9-states.html', state=states)


@app.route('/states/<state_id>')
def states_slash(id):
    """ Returns the state info """
    for state in storage.all('State').values():
        if state.id == id
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """ tearsdown connection """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
