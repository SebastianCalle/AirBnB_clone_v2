#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_cities(id=None):
    """
    Function that display a HTML page
    """
    states = storage.all("State")
    state_list1 = {}
    state_dict = {}
    cities = storage.all("City")
    cities_list = cities.values()
    for k, v in states.items():
        key = ((v.__dict__['name']), v.__dict__['id'])
        state_dict[key[0]] = key[1]
    state_list1 = sorted(state_dict.items())
    if id:
        cities_dict = {}
        for item in cities_list:
            if id == item.__dict__['state_id']:
                val = ((item.__dict__['id'], item.__dict__['state_id']))
                key = item.__dict__['name']
                cities_dict[key] = val
        cities_list = sorted(cities_dict.items())
        return render_template('9-states.html',
                               seq=state_list1, cities=cities_list, stid=id)
    else:
        return render_template('9-states.html',
                               seq=state_list1, cities=None)


@app.teardown_appcontext
def session_remove(exception=None):
    """
    Method that remove the session storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
