from moviesBooking.models import  Tickets
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class TicketRepository:

    def __init__(self, tickets_repo: DataObjectLayerInterface = DataAccessService(Tickets)):
        self.tickets_repo = tickets_repo

    def create_tickets(self, **kwargs):
        show_seats = kwargs.pop('show_seats')
        kwargs['ticket_status'] = Tickets.TicketStatus.BOOKED
        tickets = self.tickets_repo.create(**kwargs)
        tickets.show_seats.set(show_seats)
