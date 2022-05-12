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
    remove_ = text.replace('_', ' ')
    return 'C %s' % remove_


if __name__ == '__main__':
    app.run(host='0.0.0.0')
