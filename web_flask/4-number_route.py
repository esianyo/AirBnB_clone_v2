#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
@app.route('/c')
def c_text(text="is cool"):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>')
@app.route('/python')
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<n>')
def number(n):
    if not n.isdigit():
        return "n is not a number", 400
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
