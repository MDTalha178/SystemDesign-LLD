from typing import List

from Interface.LogInterface import LogInterface
from Interface.PublisherInterface import PublisherInterface
from Interface.SubscriberInterface import SubscriberInterface


class PublisherImpl(PublisherInterface):

    def __init__(self):
        self.subscriber:List[SubscriberInterface] = []

    def publish(self, message:str):
        self.notify(message)

    def subscribe(self, subscriber:SubscriberInterface):
        self.subscriber.append(
            subscriber
        )
    def unsubscribe(self, subscriber:SubscriberInterface):
        if subscriber in self.subscriber:
            self.subscriber.remove(subscriber)
        raise ValueError("Invalid Subscriber")

    def notify(self, message:str):
        for sub in self.subscriber:
            sub.update(message)
