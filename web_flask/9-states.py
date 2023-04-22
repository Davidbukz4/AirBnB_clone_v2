#!/usr/bin/python3
"""
Flask web app
"""
from flask import Flask, render_template, Response
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/')
@app.route('/states/<state_id>')
def state_var(state_id='(nil)'):
    """ Returns the state info """
    items = storage.all('State').values()
    if state_id != '(nil)':
        val = "Not found!"
    else:
        val = state_id
    for item in items:
        if state_id == states.id:
            val = item
    return Response(render_template('9-states.html', items=items,
                                    state_id=val))


@app.teardown_appcontext
def teardown(exception):
    """ tearsdown connection """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
