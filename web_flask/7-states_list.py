#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Function that display a HTML page
    """
    seq = storage.all("State")
    state_list = []
    state_list1 = {}
    state_dict = {}
    for k, v in seq.items():
        key = ((v.__dict__['name']), v.__dict__['id'])
        state_dict[key[0]] = key[1]
    state_list1 = sorted(state_dict.items())
    return render_template('7-states_list.html', seq=state_list1)

@app.teardown_appcontext
def session_remove(exception=None):
    """
    Method that remove the session storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
