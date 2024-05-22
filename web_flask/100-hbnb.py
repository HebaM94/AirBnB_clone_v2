#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def states():
    """Loads dynamic HBNB page"""
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    states = storage.all(State)
    users = storage.all(User)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places,
                           users=users)


@app.teardown_appcontext
def tear_down(td):
    """close session when application context in popped"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)