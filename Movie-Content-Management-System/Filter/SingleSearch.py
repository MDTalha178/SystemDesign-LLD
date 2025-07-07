from typing import List
from Filter.filter_interface import FilterInterface
from Model.Movie import Movie


class SingleSearch(FilterInterface):

    def __init__(self, filter_list:List[FilterInterface]):
        self.filter_list = filter_list


    def statisfy(self, movie_list:List[Movie]):
       movie_list = []
       for movie in movie_list:
           for movie_filter in self.filter_list:
               movie = movie_filter.statisfy(movie)
               if movie:
                   movie_list.append(movie)
       return movie_list
