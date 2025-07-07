from abc import ABC, abstractmethod


class RequestInterface(ABC):

    @abstractmethod
    def process_request(self, request):
        raise NotImplementedError("Subclasses must implement this method")


class ResponseInterface(ABC):

    @abstractmethod
    def process_response(self, response):
        raise NotImplementedError("Subclasses must implement this method")


class RequestHandlerInterface(ABC):

    @abstractmethod
    def handle_request(self, request):
        raise NotImplementedError("Subclasses must implement this method")
