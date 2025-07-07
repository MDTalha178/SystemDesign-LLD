from Model.Movie import Movie
from Strategy.MovieFilterStrategy import MovieFilterStrategy


class TitleFilterStrategy(MovieFilterStrategy):

    def compare(self, movie:Movie, search_value):
        return movie.title == search_value
