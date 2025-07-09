from abc import ABC, abstractmethod
from typing import List



class MessageSubscriberInterface(ABC):
    @abstractmethod
    def start_process(self, message:List):
        raise NotImplemented("Sub class should have to implement this")