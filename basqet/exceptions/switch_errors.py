from ..exceptions.forbidden import ForbiddenException
from ..exceptions.notacceptable import NotAcceptableException
from ..exceptions.notfound import NotFoundException
from ..exceptions.servererror import ServerErrorException
from ..exceptions.serviceunavailable import ServiceUnavailableException
from ..exceptions.unauthorized import UnauthorizedException
from ..exceptions.unprocessableentity import UnprocessableEntityException


class SwitchErrorStates:
    """_summary_
    A class for switching between various error status codes returned from the peer servers
    """

    def __init__(self, error):
        self.errordata = error.response

    def switch(self):
        status = self.errordata.status_code
        error_message = self.errordata.json().get('message', None)
        match status:
            case 401:
                raise UnauthorizedException({"message": error_message})
            case 403:
                raise ForbiddenException({"message": error_message})
            case 404:
                raise NotFoundException({"message": error_message})
            case 406:
                raise NotAcceptableException({"message": error_message})
            case 422:
                raise UnprocessableEntityException({"message": error_message})
            case 503:
                raise ServiceUnavailableException({"message": error_message})
            case _:
                raise ServerErrorException({"message": error_message})
