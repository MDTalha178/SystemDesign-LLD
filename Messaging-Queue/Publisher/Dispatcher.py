from Queue.QueueManager import QueueManager


class Dispatcher:
    def __init__(self, queue_manager:QueueManager):
        self.queue_manager = queue_manager
        self.is_consuming = {}


    def start_consuming(self, queue_name):
        if queue_name not in self.queue_manager.queues:
            raise ValueError("Invalid Queue")

        try:
            self.is_consuming[queue_name] = True
            while self.is_consuming.get(queue_name, False):
                queue = self.queue_manager.queues.get(queue_name)

                if queue.head is None:
                    break

                subscriber = self.queue_manager.subscribers.get(queue_name)
                if subscriber is None:
                    print("No Subscriber Found")
                    break

                for subs in subscriber:
                    messages = []
                    for _ in range(subs.batch_size):
                        msg = queue.dequeue()
                        if msg:
                            messages.append(msg)
                    if messages:
                        try:
                            subs.start_process(messages)
                        except Exception as e:
                            print(f"Subscriber {subs.id} failed: {e}")
        except Exception as e:
            print(f"failed to consume a Message: {e}")
