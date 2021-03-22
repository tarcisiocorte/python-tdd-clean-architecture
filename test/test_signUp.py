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


def test_should_return_400_if_no_name_is_provide():
    sut = SignUpController()
    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }
    request = HttpRequest(body=attributes)
    httpResponse = sut.route(request)
    assert httpResponse.status_code == 200
