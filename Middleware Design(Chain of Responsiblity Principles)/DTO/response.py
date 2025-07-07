from interfaces.interfaces import ResponseInterface


class Response(ResponseInterface):

    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def process_response(self, response):
        return {
            'status_code': self.code,
            'message': self.message,
            'data': self.data
        }
