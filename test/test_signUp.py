from flask import Flask, render_template, url_for, request, redirect
import json

from src.presentation.controllers.SignUpController import SignUpController


def test_should_return_400_if_no_name_is_provide():
    signUpController = SignUpController()
    body = {
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password"
    }
    bodyJson = json.dumps(body)

    result = signUpController.handle(bodyJson)
    resultJson = json.loads(result)

    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'name'"


def test_should_return_400_if_no_email_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password"
    }
    resultJson = json.loads(signUpController.handle(json.dumps(body)))
    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'email'"


def test_should_return_400_if_no_email_confirmation_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password"
    }
    resultJson = json.loads(signUpController.handle(json.dumps(body)))
    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'email_confirmation'"


def test_should_return_400_if_no_password_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password_confirmation": "any_password"
    }
    resultJson = json.loads(signUpController.handle(json.dumps(body)))
    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'password'"


def test_should_return_400_if_no_password_confirmation_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password"
    }
    resultJson = json.loads(signUpController.handle(json.dumps(body)))
    assert resultJson['statusCode'] == 400
    assert resultJson['message'] == "Missing param: 'password_confirmation'"
