from Handler.AuthorisationHandler import AuthorisationHandler
from Handler.AutthenticationHandler import AuthenticationHandler
from Handler.BodyParamsHandler import BodyParamsHandler
from Handler.QueryParamsHandler import QueryParamsHandler
from Handler.FinishHandler import FinishHandler
from interfaces.interfaces import RequestHandlerInterface


class RequestHanlderFactory:
    def __init__(self, handler: RequestHandlerInterface = None):
        if handler is None:
            handler = [AuthenticationHandler, AuthorisationHandler, QueryParamsHandler, BodyParamsHandler]
        self.handlers = handler

    def add_handler(self, handler):
        self.handlers.append(handler)

    @staticmethod
    def create_chain():
        return AuthenticationHandler(
            nextHandler=AuthorisationHandler(
                nextHandler=QueryParamsHandler(
                    nextHandler=BodyParamsHandler(
                        nextHandler=FinishHandler()
                    )
                )
            )
        )
