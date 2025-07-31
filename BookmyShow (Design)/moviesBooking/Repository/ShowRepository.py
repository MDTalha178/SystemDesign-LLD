from moviesBooking.models import Show
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class ShowRepository:

    def __init__(self, show_repo: DataObjectLayerInterface = DataAccessService(Show)):
        self.show_repo = show_repo

    def find_show_by_id(self, show_id):
        return self.show_repo.get(id=show_id)

    def get_all_show(self):
        return self.show_repo.filter()
