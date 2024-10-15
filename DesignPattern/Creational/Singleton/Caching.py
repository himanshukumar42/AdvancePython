import threading

class CacheService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(CacheService, cls).__new__(cls, *args, **kwargs)
                cls._instance._initialize_cache()
            return cls._instance

    def _initialize_cache(self):
        self.cache = {}

    def put(self, key, value):
        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)


def main() -> None:
    cache1 = CacheService()
    cache2 = CacheService()

    cache1.put("user1", "John doe")
    print(cache2)


if __name__ == '__main__':
    main()
