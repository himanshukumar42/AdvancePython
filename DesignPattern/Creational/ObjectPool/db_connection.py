import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__( *args, **kwargs)
        return cls._instances[cls]


class DBConnection:
    def __repr__(self):
        return f"{self.__class__.__name__}()"


class DBConnectionPoolManager(metaclass=SingletonMeta):
    def __init__(self):
        self._INITIAL_POOL_SIZE = 3
        self._MAX_POOL_SIZE = 6
        self._connection_currently_free = set()
        self._connection_currently_in_use = set()
        self._lock = threading.Lock()
        self._set_connection_currently_free()

    def _set_connection_currently_free(self):
        for i in range(self._INITIAL_POOL_SIZE):
            self._connection_currently_free.add(DBConnection())

    def get_db_connection(self):
        with self._lock:
            if len(self._connection_currently_free) == 0 and len(self._connection_currently_in_use) < self._MAX_POOL_SIZE:
                self._connection_currently_free.add(DBConnection())
            elif len(self._connection_currently_free) == 0 and len(self._connection_currently_in_use) >= self._MAX_POOL_SIZE:
                raise RuntimeError("cannot create new DB Connection as MAX_POOL_SIZE limit reached")

            db_connection = self._connection_currently_free.pop()
            self._connection_currently_in_use.add(db_connection)
            return db_connection

    def release_db_connection(self, db_connection):
        with self._lock:
            if db_connection is not None:
                self._connection_currently_in_use.remove(db_connection)
                self._connection_currently_free.add(db_connection)


def main() -> None:
    pool_manager = DBConnectionPoolManager()

    db1 = pool_manager.get_db_connection()
    db2 = pool_manager.get_db_connection()
    db3 = pool_manager.get_db_connection()
    db4 = pool_manager.get_db_connection()
    db5 = pool_manager.get_db_connection()
    db6 = pool_manager.get_db_connection()

    print(db6)
    pool_manager.release_db_connection(db6)


if __name__ == '__main__':
    main()
