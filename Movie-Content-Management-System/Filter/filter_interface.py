from abc import ABC, abstractmethod
from typing import List

from Model.Movie import Movie


class FilterInterface(ABC):

    @abstractmethod
    def statisfy(self, movie:List[Movie]):
        raise NotImplemented("Subclass should have to implement this method!")