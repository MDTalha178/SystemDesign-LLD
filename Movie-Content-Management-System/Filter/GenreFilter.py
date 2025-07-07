from typing import List

from Filter.filter_interface import FilterInterface
from Model.Movie import Movie
from Strategy.GenreFilterStrategy import GenreFilterStrategy


class GenreFilter(FilterInterface):

    def __init__(self, genre):
        self.genre = genre
        self.filter_strategy = GenreFilterStrategy()


    def statisfy(self, movie:List[Movie]):
        return [
            movie for movie in movie
            if self.filter_strategy.compare(movie=movie, search_value=self.genre)
        ]