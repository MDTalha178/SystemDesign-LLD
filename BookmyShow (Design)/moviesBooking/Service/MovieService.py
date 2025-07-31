from moviesBooking.Repository.MovieRepository import MovieRepository


class MovieService:

    def __init__(self, movie_repo=MovieRepository()):
        self.movie_repo = movie_repo

    def get_all_movie(self):
        return self.movie_repo.movie_repo.filter()

    def get_movie_by_id(self, movie_id):
        return self.movie_repo.movie_repo.get(id=movie_id)
