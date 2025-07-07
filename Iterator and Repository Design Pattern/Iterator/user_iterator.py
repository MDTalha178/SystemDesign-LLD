from Iterator.iterator_interface import UserIteratorInterface
from repository.user_repository import UserRepository
from repository.user_repository_interface import UserRepositoryInterface


class UserIterator(UserIteratorInterface):

    user_repository: UserRepositoryInterface = None
    __limit = 10
    __offset = 0
    __current = []

    def __init__(self, limit):
        self.user_repository = UserRepository()
        self.__limit = limit
        self.__current = self.user_repository.get_user_list(self.__limit, self.__offset)

    def has_next(self):
        return len(self.__current) > 0

    def next(self):
        result = self.__current
        self.__offset += self.__limit
        self.__current = self.user_repository.get_user_list(self.__limit, self.__offset)
        return result

    def __iter__(self):
        pass