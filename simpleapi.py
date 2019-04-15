import json

from flask import Flask, jsonify, request
from werkzeug.exceptions import InternalServerError
import time

app = Flask(__name__)

dataDic = {1: 'value1', 2: 'value2', 3: 'value3'}


@app.route("/")
def getAll():
    return jsonify(dataDic)


@app.route("/<int:id>")
def get(id):
    return dataDic[id]


@app.route("/", methods=['POST'])
def create():
    data = json.loads(request.data)
    dataDic[data['id']] = data['val']
    return data['val']


@app.route("/<int:id>", methods=['DELETE'])
def delete(id):
    del dataDic[id]
    return dataDic[id]


@app.route("/long")
def long():
    time.sleep(10)
    return "end long"


@app.route("/bad")
def bad():
    raise InternalServerError('err')


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0', port=5000)
