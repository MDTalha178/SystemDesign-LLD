from interfaces.interfaces import RequestInterface


class Request(RequestInterface):
    def __init__(self, data: dict, method):
        """
        Create a new Request object.

        Parameters
        ----------
        data : bytes
            The raw request data.
        method : str
            The request method (e.g. 'GET', 'POST', etc.).
        """
        self.data = data
        self.method = method

    def process_request(self, request):
        """
        Process a request and return the result. For now, this
        means simply returning the request data for POST requests.
        """
        if self.method == 'POST':
            return self.data
