#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hnmn_filters(id=None):
    """
    Function that display a HTML page
    """
    states = storage.all("State")
    state_list1 = {}
    state_dict = {}
    for k, v in states.items():
        key = ((v.__dict__['name']), v.__dict__['id'])
        state_dict[key[0]] = key[1]
    state_list1 = sorted(state_dict.items())
    cities_dict = {}
    cities = storage.all("City")
    cities_list = cities.values()
    for item in cities_list:
        val = ((item.__dict__['id'], item.__dict__['state_id']))
        key = item.__dict__['name']
        cities_dict[key] = val
    cities_list = sorted(cities_dict.items())
    amenities = storage.all("Amenity")
    amenity_list = {}
    amenity_dict = {}
    for k, v in amenities.items():
        key = ((v.__dict__['name']), v.__dict__['id'])
        amenity_dict[key[0]] = key[1]
    amenity_list = sorted(amenity_dict.items())

    return render_template('10-hbnb_filters.html',
                           states=state_list1,
                           cities=cities_list,
                           amenities=amenity_list)


@app.teardown_appcontext
def session_remove(exception=None):
    """
    Method that remove the session storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
