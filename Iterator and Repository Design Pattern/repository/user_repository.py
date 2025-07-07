from InMemorydatabase.inMemoryDatabase import InMemoryDatabase
from repository.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):

    db :InMemoryDatabase = None

    def __init__(self):
        self.db = InMemoryDatabase()

    def get_user_list(self, limit, offset):
        list_of_user = self.db.user_list()
        start = limit + offset
        end = min((start + limit), len(list_of_user))

        if start >= len(list_of_user):
            return []
        return list_of_user[start:end+1]


    def create_user(self):
        pass