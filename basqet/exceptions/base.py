class BaseException(Exception):
    def __init__(self, errors={}):
        self.errors = errors

    def __str__(self):
        return str(self.errors)
