from moviesBooking.models import  User
from utils.Repository.DataAccessService import DataAccessService
from utils.Repository.Interface import DataObjectLayerInterface


class UserRepository:

    def __init__(self, user_repo: DataObjectLayerInterface = DataAccessService(User)):
        self.user_repo = user_repo
