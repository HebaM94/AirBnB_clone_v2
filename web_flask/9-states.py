#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)