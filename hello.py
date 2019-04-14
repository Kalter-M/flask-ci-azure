from flask import Flask
from werkzeug.exceptions import InternalServerError
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/long")
def long():
    time.sleep(10)
    return "end long"


@app.route("/bad")
def bad():
    raise InternalServerError('err')