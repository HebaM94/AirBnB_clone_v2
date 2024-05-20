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
    key = 'State.{}'.format(id)
    states = storage.all(State)
    state = states.get(key)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state,
                               cities=cities)
    else:
        return render_template('9-states.html', not_found=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)