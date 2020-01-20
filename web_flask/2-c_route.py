#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Function that display Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Function that display HBNB
    """
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def cprograming(text):
    """
    Function that display HBNB
    """
    string = text.replace('_', ' ')
    return 'C {}'.format(string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
