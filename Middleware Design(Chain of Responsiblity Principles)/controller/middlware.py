from interfaces.interfaces import RequestInterface
from factory.hanlder_factory import RequestHanlderFactory
from DTO.request import Request


class MiddleWare:
    def execute(self, request: RequestInterface):
        RequestHanlderFactory().create_chain().handle_request(request)


request = Request({'name': 'John'}, 'POST')
MiddleWare().execute(request)
