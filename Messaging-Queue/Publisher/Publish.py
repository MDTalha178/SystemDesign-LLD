from Publisher.PublisherInterface import PublisherInterface
from Queue.QueueManager import QueueManager


class MessagePublisher(PublisherInterface):

    def __init__(self, queue_manager:QueueManager):
        self.queue_manager = queue_manager

    def publish(self, queue_name, data):
        queues = self.queue_manager.queues.get(queue_name)

        if queues is None:
           raise ValueError("Queue Not Found!")

        queues.enqueue(data)

    def create_queue(self, queue_name: str):
        self.queue_manager.create_queue(queue_name)

