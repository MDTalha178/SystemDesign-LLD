from Queue.MessageQueue import MessageQueue


class QueueManager:

    def __init__(self):
        self.queues: dict[str, MessageQueue] = {}
        self.subscribers: dict[str, list] = {}

    def create_queue(self, queue_name):

        if queue_name in self.queues:
            raise ValueError("Queue is Already Created!")

        self.queues[queue_name] = MessageQueue(queue_name)

        print("Queue is created {}".format(queue_name))


    def create_data(self, queue_name, data):
        queue:MessageQueue = self.queues.get(queue_name)

        if queue is None:
            raise ValueError("Invalid Queue {}".format(queue_name))

        queue.enqueue(data)

    def add_subscriber(self, queue_name, subscriber):

        if queue_name not in self.subscribers:
            self.subscribers[queue_name] = []


        print("Subscriber Added Successfully")
        self.subscribers[queue_name].append(subscriber)

    def unsubscribe(self, queue_name, subscriber_id):
         if queue_name not  in self.subscribers:
            raise ValueError("Invalid Queue")

         subscriber_list = self.subscribers.get(queue_name)
         for sub in subscriber_list:
             if sub.subscriber_id == subscriber_id:
                 subscriber_list.remove(sub)
         self.subscribers[queue_name] = subscriber_list

