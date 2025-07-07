from Model.Movie import Movie
from MovieManager.MovieManager import MovieManager


class MovieService:

    def __init__(self):
       self.movie_manager = MovieManager()

    def create_movie(self, movie:Movie):
        self.movie_manager.add_movie(movie)
        print("Movie Created Successfully!")

    def get_movie(self):
        return self.movie_manager.get_movies()
