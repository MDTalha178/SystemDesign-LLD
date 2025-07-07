from typing import List

from Model.Movie import Movie


class Repository:

    def __init__(self):
        self.movie_list:List[Movie] = []

    def create_movie(self, movie:Movie):
        self.movie_list.append(movie)

    def get_movie(self):
        return self.movie_list