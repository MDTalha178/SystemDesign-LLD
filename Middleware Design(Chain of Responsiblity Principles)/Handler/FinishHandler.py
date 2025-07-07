from interfaces.interfaces import RequestHandlerInterface


class FinishHandler(RequestHandlerInterface):
    def __init__(self, nextHandler: RequestHandlerInterface = None):
        """
        Construct a new BodyParamsHandler.

        Parameters
        ----------
        nextHandler : RequestHandlerInterface
            The next handler in the chain.
        """
        self.nextHandler = nextHandler

    def handle_request(self, request):
        """
        Handle the given request by processing body parameters.

        Parameters
        ----------
        request : RequestInterface
            The request to handle.

        Returns
        -------
        RequestInterface
            The request after it has been handled.
        """

        print("Body Params Handler Called")

        print("This is Finish Handler")

        return request
