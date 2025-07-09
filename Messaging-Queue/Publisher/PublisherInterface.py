from abc import ABC ,abstractmethod


class PublisherInterface(ABC):

    @abstractmethod
    def publish(self, queue_name, message):
        raise NotImplemented("Sub clas should have to implement")

    @abstractmethod
    def create_queue(self, queue_name: str):
        pass
