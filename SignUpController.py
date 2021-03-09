import json
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


class SignUpController:
    def handle(self, body):
        print(body)
        bodyJson = json.loads(body)
        if bodyJson.get('name') == None:
            result = {"statusCode": 400,
                      "message": "Missing param: 'name'", "body": bodyJson}

        if bodyJson.get('email') == None:
            result = {"statusCode": 400,
                      "message": "Missing param: 'email'", "body": bodyJson}

        return json.dumps(result)
