from Subscriber.subscriber_interface import Subscriber
from models.Match import Match
from publisher.publisher_interface import PublisherInterface


class BCCISubscriber(Subscriber):
    match: Match
    producers: list[PublisherInterface]

    def __init__(self, match: Match, producer: list[PublisherInterface]):
        self.match = match
        self.producers = producer

        for prod in self.producers:
            prod.subscribe(self)

    def update(self, producer: PublisherInterface):
        is_first_innings = producer.get_match_data().get_is_first_innings()

        innings_producer = (producer.get_match_data().get_innings1() if
                            is_first_innings else producer.get_match_data().get_innings2())

        innings_subscriber = self.match.get_innings1() if is_first_innings else self.match.innings2

        innings_subscriber.set_current_ball(innings_producer.get_current_over)
        innings_subscriber.set_current_wicket(innings_producer.get_current_wicket())
        innings_subscriber.set_current_score(innings_producer.get_current_score())
        innings_subscriber.set_current_over(innings_producer.get_current_over())

