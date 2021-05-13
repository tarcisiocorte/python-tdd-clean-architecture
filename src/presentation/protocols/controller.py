from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers import HttpRequest, HttpResponse


class Controller(ABC):
    """Interface to Controller"""

    @abstractmethod
    def handle(self, http_request: Type[HttpResponse]) -> HttpResponse:
        """Defining Controller"""

    raise Exception("Should implement method: handl")
