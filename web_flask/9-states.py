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
    """ Returns the states created """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', items=states)


@app.route('/states/<state_id>')
def states_id(state_id):
    """ Returns the states created """
    for state in storage.all('State').values():
        if state.id == state_id:
            return render_template('8-cities_by_states.html', items=state)
    return render_template('8-cities_by_states.html', items=state)


@app.teardown_appcontext
def teardown(exception):
    """ tearsdown connection """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
