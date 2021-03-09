from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import json

class SignUpController:
    def handle(self, body):
        print(body)
        if('name' not in body):            
            result = {"statusCode": 400, "message":"Missing param: 'name'", "body":body}       
                    
        return json.dumps(result)