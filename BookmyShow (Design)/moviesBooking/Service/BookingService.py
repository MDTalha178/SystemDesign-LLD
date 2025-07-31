from abc import ABC, abstractmethod


class BookingService(ABC):

    @abstractmethod
    def block_seat(self, user_id, show_id, show_seat_id: list):
        raise NotImplementedError("Sub class should have to implements")

    @abstractmethod
    def release_seat(self, user_id,show_id, show_seat_id: list):
        raise NotImplementedError("Sub class should have to implements")

    @abstractmethod
    def book_ticket(self, user_id, show_id, show_seat_id: list):
        # raise NotImplementedError("Sub class should have to implements")
        pass
