from datetime import datetime
from rest_framework import serializers
from Redis.BaseRedisRepository import BaseRedisRepository
from Redis.CacheInterface import CacheInterface
from moviesBooking.Repository.ShowSeatsRepository import ShowSeatsRepository
from moviesBooking.Service.BookingService import BookingService
from moviesBooking.Service.TicketsService import TicketService


class RedisBookingService(BookingService):
    __SEAT_LOCK_KEY_PREFIX = "seat_lock"
    DEFAULT_TTL = 60

    def __init__(self, redis_service: CacheInterface = BaseRedisRepository('locks')):
        self.redis_service = redis_service
        self.show_seat_repo = ShowSeatsRepository()
        self.ticket_service = TicketService()

    def get_key_prefix(self):
        return self.__SEAT_LOCK_KEY_PREFIX

    def block_seat(self, show_id: str, seat_id: list, user_id: str, ttl: int = DEFAULT_TTL) -> None:
        show_seat_id = self.show_seat_repo.find_show_by_show_seat_id(show_id=show_id, show_seat_id=seat_id)
        if len(show_seat_id) != len(seat_id):
            raise serializers.ValidationError("its seems seat is lock or already booked... Invalid seat selection.")

        for seat_id in show_seat_id:
            key = self.redis_service.make_key(self.get_key_prefix(), seat_id)
            locked_by = self.redis_service.get(key)
            if locked_by and locked_by != str(user_id):
                raise serializers.ValidationError("One or more seats are already locked by another user.")

        for seat_id in show_seat_id:
            seat_key = self.redis_service.make_key(self.get_key_prefix(), seat_id)
            self.redis_service.save(seat_key, user_id, nx=True, ex=ttl)

    def book_ticket(self, user_id, show_id, seat_id: list):
        tickets = self.ticket_service.book_ticket(user_id, show_id, seat_id)

        # release the lock
        self.release_seat(show_id, seat_id, user_id)

        return tickets

    def release_seat(self, user_id, show_id, show_seat_id, ):
        if self.redis_service.get(show_seat_id):
            self.redis_service.delete(show_seat_id)
            return True
        return False

    def bulk_unlock_seats(self, show_id, seat_id: list, user_id: str):
        show_seat_id = self.show_seat_repo.find_show_by_show_seat_id(show_id=show_id, show_seat_id=seat_id)
        for seat_id in show_seat_id:
            self.release_seat(user_id, show_id, seat_id)
