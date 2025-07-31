from moviesBooking.models import ShowSeats
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class ShowSeatsRepository:

    def __init__(self, show_seats_repo: DataObjectLayerInterface = DataAccessService(ShowSeats)):
        self.show_seats_repo = show_seats_repo

    def find_all_show_by_id(self, show_id):
        return self.show_seats_repo.filter(show_id=show_id)

    def find_show_by_show_seat_id(self, show_id, show_seat_id:list):
        return self.show_seats_repo.filter(
            show_id=show_id, seats_id__in=show_seat_id,
            seat_status=ShowSeats.SeatType.AVAILABLE
        ).values_list('id', flat=True)
