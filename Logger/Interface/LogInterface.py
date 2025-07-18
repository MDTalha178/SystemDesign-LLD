from abc import ABC, abstractmethod

from Enum.LoggerEnum import LoggerEnum


class LogInterface(ABC):

    @abstractmethod
    def log(self, loglevel:LoggerEnum, message:str):
        raise NotImplementedError("Sub class should have to implement this method")