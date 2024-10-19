import redis


class Cache:
    def __init__(self):
        self._redis = None

    def get_redis(self):
        if self._redis is None:
            self._redis = redis.Redis(host='localhost', port=6379, db=0)
            print("Redis connection established")
        return self._redis

    def get_value(self, key):
        r = self.get_redis()
        return r.get(key)

    def set_value(self, key, value):
        r = self.get_redis()
        r.set(name=key, value=value)


def main() -> None:
    cache = Cache()
    cache.set_value("age", 26)
    value = cache.get_value("age")
    print(value)


if __name__ == '__main__':
    main()
