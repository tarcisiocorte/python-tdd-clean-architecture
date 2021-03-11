from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.presentation.controllers.SignUpController import SignUpController
import json


app = Flask(__name__)


def to_json(self):
    return {"email": self.email}


@app.route('/', methods=['POST', 'GET'])
def index():
    sut = SignUpController()

    teste = {'email': 'ant_email@mail',
             'email_confirmation': 'any_email@mail.com', 'password': 'any_password'}

    result = sut.handle(teste)
    return result


if __name__ == "__main__":
    app.run(debug=True)
