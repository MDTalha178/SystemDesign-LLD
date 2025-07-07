from abc import ABC, abstractmethod

from Model.Movie import Movie


class MovieFilterStrategy(ABC):

    @abstractmethod
    def compare(self, movie:Movie, search_value):
        raise NotImplemented("Subclass should have to implement this method!")