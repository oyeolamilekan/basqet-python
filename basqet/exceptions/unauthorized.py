from .base import BaseException as error


class UnauthorizedException(error):
    def __init__(self, errors):
        super().__init__(errors)
