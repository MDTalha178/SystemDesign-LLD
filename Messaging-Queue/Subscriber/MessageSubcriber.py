
from typing import List
from Subscriber.SubscriberInterface import MessageSubscriberInterface


class MessageSubscriber(MessageSubscriberInterface):
    def __init__(self, subscriber_id: str, callback_function, batch_size: int = 1):
        self.id = subscriber_id
        self.callback = callback_function
        self.batch_size = batch_size
        self.retry_policy = None
    def start_process(self, messages: List):

        try:
            if self.batch_size == 1:
                for message in messages:
                    self.callback([message])
            else:
                for i in range(0, len(messages), self.batch_size):
                    msg = messages[i:i+self.batch_size]
                    self.callback(msg)
        except Exception as e:
            print(f"Subscriber {self.id} failed to process messages: {e}")
