from faker import Faker
from flask import Flask, render_template, url_for, request, redirect, jsonify
import json
from typing import Type

from src.presentation.controllers import SignUpController
from src.presentation.helpers import HttpRequest, HttpResponse

faker = Faker()


def makeSut():
    sut = SignUpController()
    return sut


def test_should_return_400_if_no_login_is_provide():
    sut = SignUpController()
    attributes = {
        "name": faker.word(),
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_400_if_no_name_is_provide():
    sut = SignUpController()
    attributes = {
        "login": "any_login",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_400_if_no_email_is_provide():
    sut = SignUpController()
    attributes = {
        "name": "any_name",
        "login": "any_login",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_400_if_no_email_confirmation_is_provide():
    sut = SignUpController()
    attributes = {
        "name": "any_name",
        "login": "any_login",
        "email": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_400_if_no_password_is_provide():
    sut = SignUpController()
    attributes = {
        "name": "any_name",
        "login": "any_login",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_400_if_no_password_confirmation_is_provide():
    sut = SignUpController()
    attributes = {
        "name": "any_name",
        "login": "any_login",
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 400


def test_should_return_200_if_valid_para_is_provided():
    sut = SignUpController()
    attributes = {
        "name": faker.word(),
        "login": faker.word(),
        "email": "any_email@mail.com",
        "email_confirmation": "any_email@mail.com",
        "password": "any_password",
        "password_confirmation": "any_password",
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 200
