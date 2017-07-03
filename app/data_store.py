import os
import redis
from redis import StrictRedis


class DataStore:
    def __init__(self):
        env = os.getenv('ENV', 'local')
        if env == 'local':
            self.client = StrictRedis(
                host=os.getenv('REDIS_HOST', 'localhost'),
                port=os.getenv('REDIS_PORT', 6379),
                db=os.getenv('REDIS_DB', 0)
            )
        elif env == 'heroku':
            self.client = redis.from_url(os.getenv('REDIS_URL'))

    def dict_set(self, key, dict):
        self.client.hmset(key, dict)

    def dict_get(self, key):
        self.client.hgetall(key)

    def set(self, key, field, value):
        self.client.hset(key, field, value)

    def get(self, key, field):
        self.client.hget(key, field)

    def exists(self, key, field):
        self.client.hexists(key, field)
