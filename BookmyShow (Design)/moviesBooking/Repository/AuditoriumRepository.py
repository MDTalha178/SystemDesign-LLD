from moviesBooking.models import Auditorium
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class AuditoriumRepository:

    def __init__(self, auditorium_repo: DataObjectLayerInterface = DataAccessService(Auditorium)):
        self.auditorium_repo = auditorium_repo
