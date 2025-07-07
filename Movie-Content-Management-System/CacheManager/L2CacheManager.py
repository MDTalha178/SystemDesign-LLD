from typing import List
from CacheManager.CacheInterface import CacheInterface
from Filter.filter_interface import FilterInterface
from Model.Movie import Movie
from MovieManager.MovieManager import MovieManager


class L2CacheManager(CacheInterface):

    def __init__(self, movie_filter: FilterInterface):
        self.l2_cache_manager: List[Movie] = []

        self.movie_filter: FilterInterface = movie_filter

        self.nextHandler = MovieManager()

    def get_data(self, **kwargs):
        if self.l2_cache_manager:
            movie_list = self.movie_filter.statisfy(self.l2_cache_manager)
            if movie_list:
                movie_data = self.movie_filter.statisfy(movie_list)
                if movie_data:
                    print("Found data in L2Cache Manager")
                    return movie_data
        data = self.nextHandler.get_movies()
        if data:
            data = self.movie_filter.statisfy(data)
            self.save_data(data, **kwargs)


    def save_data(self, movie:List[Movie], **kwargs):
        self.l2_cache_manager.extend(
            movie
        )

    def clear_cache(self):
        self.l2_cache_manager.clear()