import json
from flask import Flask, render_template, url_for, request, redirect, jsonify
from src.main.interface import RouteInterface
from src.presentation.helpers import HttpRequest, HttpResponse
from typing import Type
app = Flask(__name__)


class SignUpController(RouteInterface):
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        fields = ["name", "email", "email_confirmation",
                  "password", "password_confirmation"]

        response = {}
        response["status_code"] = 200
        response["data"] = ""
        return HttpResponse(
            status_code=response["status_code"], body=response["data"]
        )
