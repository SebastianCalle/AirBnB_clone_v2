#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Function that display a HTML page
    """
    states = storage.all("State")
    cities = storage.all("City")
    state_list1 = {}
    state_dict = {}
    cities_list = cities.values()
    cities_dict = {}
    for item in cities_list:
        val = ((item.__dict__['id'], item.__dict__['state_id']))
        key = item.__dict__['name']
        cities_dict[key] = val
    cities_list = sorted(cities_dict.items())
    for k, v in states.items():
        key = ((v.__dict__['name']), v.__dict__['id'])
        state_dict[key[0]] = key[1]
    state_list1 = sorted(state_dict.items())
    return render_template('8-cities_by_states.html',
                           seq=state_list1, cities=cities_list)


@app.teardown_appcontext
def session_remove(exception=None):
    """
    Method that remove the session storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
