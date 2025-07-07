from abc import  ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def get_user_list(self, limit, offset):
        raise NotImplementedError('Sub class should have to implements')

    @abstractmethod
    def create_user(self):
        raise  NotImplementedError("Sub class should have to implement this method")