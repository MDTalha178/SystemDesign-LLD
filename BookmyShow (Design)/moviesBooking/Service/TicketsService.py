from moviesBooking.Repository.ShowSeatsRepository import ShowSeatsRepository
from moviesBooking.Repository.TicketsRepository import TicketRepository
from moviesBooking.models import ShowSeats


class TicketService:

    def __init__(self, ticket_repo: TicketRepository = TicketRepository()):
        self.ticket_repo = ticket_repo
        self.show_seat_repo = ShowSeatsRepository()

    def book_ticket(self, user_id, show_id, seat_id: list):
        show_seat = list(self.show_seat_repo.find_show_by_show_seat_id(show_id=show_id, show_seat_id=seat_id))
        tickets = self.ticket_repo.create_tickets(
            user_id=user_id,
            show_id=show_id,
            show_seats=show_seat,

        )
        self.show_seat_repo.show_seats_repo.idempotent_update(
            {'show_id': show_id, 'id__in': show_seat},
            seat_status=ShowSeats.SeatType.BOOKED

        )
        return tickets
