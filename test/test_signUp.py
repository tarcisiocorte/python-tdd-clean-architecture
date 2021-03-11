from flask import Flask, render_template, url_for, request, redirect, jsonify
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
    result = signUpController.handle(body)
    assert result['status_code'] == 400
    assert result['message'] == f"Missing param: 'name'"


def test_should_return_400_if_no_email_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password"
    }
    result = signUpController.handle(body)
    assert result['status_code'] == 400
    assert result['message'] == f"Missing param: 'email'"


def test_should_return_400_if_no_email_confirmation_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password"
    }
    result = signUpController.handle(body)
    assert result['status_code'] == 400
    assert result['message'] == f"Missing param: 'email_confirmation'"


def test_should_return_400_if_no_password_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password_confirmation": "any_password"
    }
    result = signUpController.handle(body)
    assert result['status_code'] == 400
    assert result['message'] == f"Missing param: 'password'"


def test_should_return_400_if_no_password_confirmation_is_provide():
    signUpController = SignUpController()
    body = {
        "name": "any_name",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password"
    }
    result = signUpController.handle(body)
    assert result['status_code'] == 400
    assert result['message'] == f"Missing param: 'password_confirmation'"
