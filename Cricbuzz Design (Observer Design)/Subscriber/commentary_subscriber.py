from Subscriber.subscriber_interface import Subscriber
from models.Match import Match
from publisher.publisher_interface import PublisherInterface


class CommentarySubscriber(Subscriber):
    match: Match
    commentaries: list

    def __init__(self, match: Match, producer: list[PublisherInterface]):
        self.match = match
        self.commentaries = []

        for prod in producer:
            prod.subscribe(self)

    def update(self, producer: PublisherInterface):
        comment = producer.get_match_data().get_commentary()
        self.commentaries.append(comment[-1])
