from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from SignUpController import SignUpController
import json


app = Flask(__name__)


def to_json(self):
    return {"email": self.email}


@app.route('/', methods=['POST', 'GET'])
def index():
    sut = SignUpController()
    resultJson = json.loads(sut.handle(json.dumps(request.get_json())))
    return resultJson, resultJson["statusCode"]


if __name__ == "__main__":
    app.run(debug=True)
