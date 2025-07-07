from abc import ABC, abstractmethod

from Subscriber.subscriber_interface import Subscriber


class PublisherInterface(ABC):

    @abstractmethod
    def get_match_data(self):
        raise NotImplementedError("Sub class should have implements")

    @abstractmethod
    def subscribe(self, subscriber: Subscriber):
        raise NotImplementedError("Sub class should have implements")

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber):
        raise NotImplementedError("Sub class should have implements")

    @abstractmethod
    def notify_subscriber(self):
        raise NotImplementedError("Sub class should have implements")
