from moviesBooking.Repository.ShowSeatsRepository import ShowSeatsRepository


class ShowSeatsService:

    def __init__(self, show_seats_repo=ShowSeatsRepository()):
        self.show_seats_repo = show_seats_repo


    def find_available_seats(self, showId, seats:list):
        return self.show_seats_repo.show_seats_repo.filter()

