#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_list_route():
    """List all the State object alphabetically"""
    list_s = []
    dico = storage.all(State)
    for k, v in dico.items():
        list_s.append(dico[k])
    return render_template('8-cities_by_states.html', states=list_s)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
