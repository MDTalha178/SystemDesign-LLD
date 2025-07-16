from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send_notification(self):
        raise NotImplemented("Sub class should have to implements")