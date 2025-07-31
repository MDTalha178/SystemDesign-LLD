from datetime import datetime

from Redis.BaseRedisRepository import BaseRedisRepository
from Redis.CacheInterface import CacheInterface


class RedisBookingService:

    def __init__(self, redis_service: CacheInterface = BaseRedisRepository('locks')):
        self.redis_service = redis_service

    def get_key_prefix(self) -> str:
        return "seat_lock"

    def lock_seat(self, show_seat_id: list, user_id: str, ttl=300):
        for seat_id in show_seat_id:
            seat_key = self.redis_service.make_key(self.get_key_prefix(), seat_id)

            seat_data = {
                'user_id': user_id,
                'show_id': show_seat_id,
                'locked_at': datetime.now().isoformat(),
                'status': 'locked'
            }

            self.redis_service.save(seat_key, self.redis_service.serialize(seat_data), nx=True, ex=ttl)

    def unlock_seat(self, show_seat_id, user_id):
        if self.redis_service.get(show_seat_id):
            self.redis_service.delete(show_seat_id)
            return True
        return False

    def bulk_unlock_seats(self, show_seat_id: list, user_id: str):
        for seat_id in show_seat_id:
            self.unlock_seat(seat_id, user_id)
