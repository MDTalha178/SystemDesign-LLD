import json

class DataNode:

    def __init__(self, data, next_data=None):
        self.data = data
        self.next_data = next_data

class MessageQueue:

    def __init__(self, name):
        self.head = None
        self.tail = None
        self.size = 0
        self.name = name

    def enqueue(self, message):
        data_node:DataNode =  DataNode(message)

        if self.head is None:
            self.head = self.tail = data_node
        else:
            self.tail.next = data_node
            self.tail = data_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None

        message = self.head.data
        self.head = self.head.next_data

        if self.head is None:
            self.tail = None

        self.size -= 1
        return message