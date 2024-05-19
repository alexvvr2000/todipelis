from flask import Flask
from flask import json

app: Flask = Flask(__name__)


@app.route("/", methods=["GET"])
def ruta():
    return {"hola": "universo 7"}
