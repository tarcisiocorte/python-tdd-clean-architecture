import json
from flask import Flask, render_template, url_for, request, redirect, jsonify
app = Flask(__name__)


class SignUpController:
    def handle(self, body):

        fields = ["name", "email", "email_confirmation",
                  "password", "password_confirmation"]

        response = {}

        for field in fields:
            if body.get(field) == None:
                response["status_code"] = 400
                response["message"] = f"Missing param: '{field}'"
                return response

    def handleRequest(self, body):

        response = {}
        if("name" not in body):
            response["status_code"] = 200
            response["mensagem"] = "deu certo o teste"

            return response
        else:
            response["status_code"] = 400
            response["mensagem"] = "deu certo o teste"

            return response
