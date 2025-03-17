from pyexpat.errors import messages


class UIException(Exception):
    def __init__(self, message: str):
        self._message = message

    def __str__(self):
        return self._message