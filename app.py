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
    #result = sing.handle(request.form['email'], request.form[email_confirmation])
    body = request.get_json()
    result = sut.handle(body)
    print(f"veja o que deu {result}")
    return f"{result}"

if __name__ == "__main__":
    app.run(debug=True)    