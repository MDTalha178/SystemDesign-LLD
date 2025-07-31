import redis
import logging
from typing import Dict
from django.conf import settings

logger = logging.getLogger(__name__)


class RedisManager:
    """Simple Redis connection manager"""

    _connections: Dict[str, redis.Redis] = {}

    @classmethod
    def get_connection(cls, name: str = 'default') -> redis.Redis:
        """Get or create Redis connection"""
        if name not in cls._connections:
            config = settings.REDIS_CONFIG[name]

            cls._connections[name] = redis.Redis(
                host=config['HOST'],
                port=config['PORT'],
                db=config['DB'],
                # password=config['PASSWORD'],
                decode_responses=True,
                socket_connect_timeout=5,
                socket_timeout=5,
                retry_on_timeout=True,
                health_check_interval=30
            )

            # Test connection
            cls._connections[name].ping()
            logger.info(f"Redis '{name}' connected")

        return cls._connections[name]
