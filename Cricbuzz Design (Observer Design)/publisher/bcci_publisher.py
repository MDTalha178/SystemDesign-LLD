from Subscriber.subscriber_interface import Subscriber
from models.Match import Match
from publisher.publisher_interface import PublisherInterface


class BCCIPublisher(PublisherInterface):
    match: Match
    subscriber: list

    def __init__(self, match: Match):
        self.match = match
        self.subscriber = []

    def score_update(self):
        # here we will do the API call to get the data
        self.notify_subscriber()

    def get_match_data(self) -> Match:
        return self.match

    def subscribe(self, subscriber: Subscriber):
        self.subscriber.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscriber.remove(subscriber)

    def notify_subscriber(self):
        for sub in self.subscriber:
            sub.update(self)
