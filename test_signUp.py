from flask import Flask, render_template, url_for, request, redirect
import json

from SignUpController import SignUpController

def test_should_return_400_if_no_name_is_provide():
    signUpController = SignUpController()
    body = {        
        "email":"any_email@mail.com", 
        "email_confirmation":"any_email@mail.com",
        "password":"any_password",
        "password_confirmation": "any_password"
        }
    bodyJson = json.dumps(body)       
    
    result  = signUpController.handle(bodyJson)
    resultJson = json.loads(result)

    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'name'"
    