from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

class SignUpController:
    def handle(self, body):
        print(body)
        if('name' not in body):
            statusCode = 400
        else:
            statusCode = 200
                    
        return statusCode