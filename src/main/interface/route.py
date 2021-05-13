from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers import HttpRequest, HttpResponse


class RouteInterface:
    """Interface to Routes"""

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
