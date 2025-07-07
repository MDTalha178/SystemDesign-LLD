from Iterator.iterator_interface import UserIteratorInterface
from Iterator.user_iterator import UserIterator
from repository.user_repository import UserRepository
from repository.user_repository_interface import UserRepositoryInterface


class UserService:

    user_repository :UserRepositoryInterface = None
    user_iterator : UserIteratorInterface = None

    def __init__(self, user_repository: UserRepositoryInterface = UserRepository):
        self.user_repository = UserRepository()
        self.user_iterator = UserIterator(10)

    def get_user_list(self):
        while self.user_iterator.has_next():
            user = self.user_iterator.next()
            print(user)