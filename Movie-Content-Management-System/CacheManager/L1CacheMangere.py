from typing import List
from CacheManager.CacheInterface import CacheInterface
from CacheManager.L2CacheManager import L2CacheManager
from Filter.filter_interface import FilterInterface
from Model import Movie
from Service.UserService import UserService


class L1CacheManager(CacheInterface):

    def __init__(self, movie_filter:FilterInterface):
        self.user_service = UserService()

        self.l1_cache_manager = {str:List[Movie]}
        self.nextHandler = L2CacheManager(
            movie_filter
        )

        self.movie_filter:FilterInterface = movie_filter

    def get_data(self, **kwargs):
        user_id = kwargs.get('user_id')
        if self.user_service.check_user_is_valid(user_id):
            movie_list = self.l1_cache_manager.get(user_id)
            if movie_list:
                movie_data = self.movie_filter.statisfy(movie_list)
                if movie_data:
                    print("Found data in L1Cache Manager")
                    return movie_data
            data = self.nextHandler.get_data()
            self.save_data(data, **kwargs)


    def save_data(self, movie:List[Movie], **kwargs):
        self.l1_cache_manager.update(
            {kwargs.get('user_id'):movie}
        )

    def clear_cache(self):
        self.l1_cache_manager.clear()