from abc import  ABC, abstractmethod

from publisher.publisher_interface import PublisherInterface


class Subscriber(ABC):

    @abstractmethod
    def update(self, producer: PublisherInterface):
        raise NotImplementedError("Sub class should have to implements this")