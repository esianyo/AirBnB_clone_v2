#!/usr/bin/python3
"""script that starts a web flask application"""

from flask import Flask

#create an instance of the flask
app = Flask(__name__)

#map root to function
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """functions that displays hello HBNB"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
