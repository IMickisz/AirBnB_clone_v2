#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list_route():
    """List all the State object alphabetically"""
    list_s = []
    dico = storage.all(State)
    for k, v in dico.items():
        list_s.append(dico[k])
    return render_template('7-states_list.html', states=list_s)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
