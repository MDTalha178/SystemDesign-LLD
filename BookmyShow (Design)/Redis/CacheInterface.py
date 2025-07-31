import json
from abc import ABC, abstractmethod
from typing import Any


class CacheInterface(ABC):
    """Base class for Redis repositories"""

    @abstractmethod
    def save(self, key, value, **kwargs):
        raise NotImplementedError("Sub class should have implements")

    @abstractmethod
    def delete(self, key):
        raise NotImplementedError("Sub class should have implements")

    def get(self, key):
        raise NotImplementedError("Sub class should have implements")


    @abstractmethod
    def make_key(self, prefix: str, *parts) -> str:
        """Create Redis key with prefix"""
        pass

    @abstractmethod
    def serialize(self, data: Any) -> str:
        """Simple JSON serialization"""
        pass

    @abstractmethod
    def deserialize(self, data: str) -> Any:
        """Simple JSON deserialization"""
        pass
