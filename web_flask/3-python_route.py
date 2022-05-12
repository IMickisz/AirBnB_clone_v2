#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Returns 'Hello HBNB!' at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Returns 'HBNB' at the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """Returns “C” followed by the value of the text variable at the
    /c/<test> route"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Returns “python” followed by the value of the text variable or "is cool"
    by default at the /python/<text> route"""
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
