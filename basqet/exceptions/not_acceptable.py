from .base import BaseException as error


class NotAcceptableException(error):
    def __init__(self, errors):
        super().__init__(errors)
