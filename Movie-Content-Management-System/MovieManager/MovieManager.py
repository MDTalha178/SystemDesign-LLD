from Model.Movie import Movie
from Repository.MovieRepository import Repository


class MovieManager:

    def __init__(self):
        self.movie_repo = Repository()

    def add_movie(self, movie:Movie):
        self.movie_repo.create_movie(movie)

    def get_movies(self):
        return self.movie_repo.get_movie()