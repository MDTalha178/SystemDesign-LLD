from abc import ABC, abstractmethod
from typing import List

from Model import Movie


class CacheInterface(ABC):

    @abstractmethod
    def get_data(self, **kwargs):
        raise NotImplemented("Subclass should have to implement this method!")

    @abstractmethod
    def save_data(self, movie:List[Movie], **kwargs):
        raise NotImplemented("Subclass should have to implement this method!")

    @abstractmethod
    def clear_cache(self):
        raise NotImplemented("Subclass should have to implement this method!")