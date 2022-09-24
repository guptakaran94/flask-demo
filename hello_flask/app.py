from flask import Flask
from pd import pandas

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/demo")
def test():
    return "Hello, Flask! Demo"


@app.route("/import")
def importFile():
    return "Hello, Flask! Demo"