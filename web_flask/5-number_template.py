#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask, render_template

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
    Function that display C
    """
    string = text.replace('_', ' ')
    return 'C {}'.format(string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyhthon_programming(text="is cool"):
    """
    Function that display Python
    """
    string = text.replace('_', ' ')
    return 'Python {}'.format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Function that display number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Function that display number
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
