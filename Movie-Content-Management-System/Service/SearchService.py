from CacheManager.L1CacheMangere import L1CacheManager
from Filter.filter_interface import FilterInterface


class SearchService:

    @staticmethod
    def search(user_id, filter_movie):
        return L1CacheManager(filter_movie).get_data(user_id=user_id)