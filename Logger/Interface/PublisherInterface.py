from abc import ABC

from Interface.SubscriberInterface import SubscriberInterface


class PublisherInterface(ABC):

    def publish(self, message):
        raise NotImplementedError("Sub class should have to implement this")

    def subscribe(self, subscriber:SubscriberInterface):
        raise NotImplementedError("Sub class should have to implement this")

    def unsubscribe(self, subscriber:SubscriberInterface):
        raise NotImplementedError("Sub class should have to implement this")

    def notify(self, message):
        raise NotImplementedError("Sub class should have to implement this")