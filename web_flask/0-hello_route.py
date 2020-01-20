#!/usr/bin/python3
# Script that starts a flask web application

from flask import Flask

app = Flask(__name__)
app.run(host='0.0.0.0', port=5000)


@app.route('/', strict_slashes=False)
def index():
    """
    Function that display Hello HBNB!
    """
    return 'Hello HBNB!'
