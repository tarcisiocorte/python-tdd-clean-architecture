import json
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


class SignUpController:
    def handle(self, body):
        bodyJson = json.loads(body)
        fields = ["name", "email", "email_confirmation"]
        for field in fields:
            if bodyJson.get(field) == None:
                result = {"statusCode": 400,
                          "message": f"Missing param: '{field}'", "body": bodyJson}

        print(result)
        return json.dumps(result)
