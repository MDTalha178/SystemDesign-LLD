from interfaces.interfaces import RequestHandlerInterface


class AuthorisationHandler(RequestHandlerInterface):
    nextHandler: RequestHandlerInterface = None

    def __init__(self, nextHandler: RequestHandlerInterface):
        """
        Construct a new AuthorisationHandler.

        Parameters
        ----------
        nextHandler : RequestHandlerInterface
            The next handler in the chain.
        """

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
        print("AuthorisationHandler Called")

        print("Calling next Handler")
        self.nextHandler.handle_request(request)

        return request
