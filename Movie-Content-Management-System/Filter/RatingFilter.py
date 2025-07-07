from typing import List

from Filter.filter_interface import FilterInterface
from Model.Movie import Movie
from Strategy.MovieFilterStrategy import MovieFilterStrategy
from Strategy.TitleFilterStrategy import TitleFilterStrategy


class RatingFilter(FilterInterface):
    def __init__(self, rating):
        self.year = rating
        self.filter_strategy:MovieFilterStrategy = TitleFilterStrategy()

    def statisfy(self, movie: List[Movie]):
        return [
            movie for movie in movie
            if self.filter_strategy.compare(movie=movie, search_value=self.rating)
        ]