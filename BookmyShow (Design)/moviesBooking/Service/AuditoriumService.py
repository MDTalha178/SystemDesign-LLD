from moviesBooking.Repository.AuditoriumRepository import AuditoriumRepository


class AuditoriumService:

    def __init__(self, auditorium_repo=AuditoriumRepository()):
        self.auditorium_repo = auditorium_repo

    def get_auditorium_by_show_id(self, show_id):
        return self.auditorium_repo.auditorium_repo.filter(show__id=show_id)

    def get_movie_by_id(self, movie_id):
        return self.auditorium_repo.auditorium_repo.filter(id=movie_id)
