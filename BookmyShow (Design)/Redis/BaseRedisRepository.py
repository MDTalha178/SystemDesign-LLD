import json
from abc import ABC, abstractmethod
from typing import Any

from Redis.CacheInterface import CacheInterface
from Redis.RedisManager import RedisManager


class BaseRedisRepository(CacheInterface):
    """Base class for Redis repositories"""

    def __init__(self, connection_name: str = 'default'):
        self.redis = RedisManager.get_connection(connection_name)

    def save(self, key, value, **kwargs):
        self.redis.set(key, value, **kwargs)

    def delete(self, key):
        self.redis.delete(key)

    def get(self, key):
        return self.redis.get(key)

    def make_key(self, prefix, *parts) -> str:
        """Create Redis key with prefix"""
        return f"{prefix}:{':'.join(str(p) for p in parts)}"

    def serialize(self, data: Any) -> str:
        """Simple JSON serialization"""
        if isinstance(data, str):
            return data
        return json.dumps(data)

    def deserialize(self, data: str) -> Any:
        """Simple JSON deserialization"""
        if not data:
            return None
        try:
            return json.loads(data)
        except (json.JSONDecodeError, TypeError):
            return data
