from Model.Movie import Movie
from Strategy.MovieFilterStrategy import MovieFilterStrategy


class GenreFilterStrategy(MovieFilterStrategy):

    def compare(self, movie:Movie, search_value):
        return movie.genre == search_value