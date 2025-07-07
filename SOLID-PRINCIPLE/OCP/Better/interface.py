from abc import ABC, abstractmethod

class NotificationServiceInterface(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass
