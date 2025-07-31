from moviesBooking.models import Movie
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class MovieRepository:

    def __init__(self, movie_repo: DataObjectLayerInterface = DataAccessService(Movie)):
        self.movie_repo = movie_repo
