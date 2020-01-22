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
    state_dict = {}
    for k, v in seq.items():
        state_list.append(v)
    return render_template('7-states_list.html', seq=state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
