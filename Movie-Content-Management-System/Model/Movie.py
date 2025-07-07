from Service.MovieService import MovieService


class Movie:

    def __init__(self, movie_id, title, genre, release_year, rating):
        self.movie_id = movie_id,
        self.title = title,
        self.genre = genre,
        self.release_year = release_year
        self.rating = rating

        self.movie_service = MovieService()


    def add_movie(self):
        self.movie_service.create_movie(
            self
        )
