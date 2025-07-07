from interfaces.interfaces import RequestHandlerInterface


class QueryParamsHandler(RequestHandlerInterface):
    def __init__(self, nextHandler: RequestHandlerInterface):
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

        print("Query Params Handler Called")

        print("Calling next Handler")
        self.nextHandler.handle_request(request)

        return request
