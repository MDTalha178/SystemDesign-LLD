from interfaces.interfaces import RequestHandlerInterface


class AuthenticationHandler(RequestHandlerInterface):
    nextHandler: RequestHandlerInterface = None

    def __init__(self, nextHandler: RequestHandlerInterface):
        self.nextHandler = nextHandler

    def handle_request(self, request):
        """
        Handle the given request.

        Parameters
        ----------
        request : RequestInterface
            The request to handle.

        Returns
        -------
        RequestInterface
            The request after it has been handled.
        """
        print("AuthenticationHandler Called")

        print("Calling next Handler")
        self.nextHandler.handle_request(request)

        return request
