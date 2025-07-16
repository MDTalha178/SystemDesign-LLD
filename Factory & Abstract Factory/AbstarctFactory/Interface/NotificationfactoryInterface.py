from abc import ABC, abstractmethod


class NotificationFactoryInterface(ABC):

    @abstractmethod
    def create_alter_notification(self):
        raise NotImplemented("Sub class should have to implement")

    @abstractmethod
    def create_welcome_notification(self):
        raise NotImplemented("Sub class should have to implement")