#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Hello HBNB! - Start"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """C followed by text"""
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
