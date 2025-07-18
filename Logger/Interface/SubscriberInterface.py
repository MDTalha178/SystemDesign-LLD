from abc import ABC


class SubscriberInterface(ABC):

    def update(self, message:str):
        raise NotImplementedError("Sub class should have implement this method")