from moviesBooking.Repository.ShowRepository import ShowRepository


class ShowService:

    def __init__(self, show_repo=ShowRepository()):
        self.show_repo = show_repo

