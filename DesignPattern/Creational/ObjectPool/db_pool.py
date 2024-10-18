import queue


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection():
    def __init__(self, connection_id):
        self._connection_id = connection_id

    def connect(self):
        print(f"Connecting to database with connection id {self._connection_id}")

    def execute_query(self, query):
        print(f"Executing query: {query} by using {self._connection_id}")

    def close(self):
        print(f"Closing DB Connection {self._connection_id}")

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class DBConnectionPool(metaclass=SingletonMeta):
    def __init__(self, max_connections):
        self.pool = queue.Queue(max_connections)
        for i in range(max_connections):
            self.pool.put(DBConnection(i+1))

    def get_connection(self):
        if not self.pool.empty():
            return self.pool.get()
        else:
            print("No available connections")
            return None

    def release_connections(self, connection: DBConnection):
        connection.close()
        self.pool.put(connection)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.pool})"


def main() -> None:
    pool = DBConnectionPool(5)
    conn1 = pool.get_connection()
    conn1.execute_query("SELECT * from users")
    pool.release_connections(conn1)


if __name__ == '__main__':
    main()
