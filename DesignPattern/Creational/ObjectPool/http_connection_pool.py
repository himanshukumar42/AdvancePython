import queue
import random
import threading
import time

import requests


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HTTPConnection:
    def __init__(self, connection_id):
        self._connection_id = connection_id
        self.session = requests.session()

    def send_request(self, method, url, **kwargs):
        print(f"Connection {self._connection_id} sending request to {url}")
        try:
            response = self.session.request(method, url, **kwargs)
            return response
        except requests.RequestException as e:
            print(f"Connection {self._connection_id} failed: {e}")
            return None

    def close(self):
        self.session.close()
        print(f"Connection {self._connection_id} closed.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self._connection_id})"


class HTTPConnectionPool(metaclass=SingletonMeta):
    def __init__(self, max_connections):
        self.pool = queue.Queue(max_connections)
        for i in range(max_connections):
            self.pool.put(HTTPConnection(i + 1))

    def get_connection(self):
        if not self.pool.empty():
            connection = self.pool.get()
            print(f"Acquired connection {connection}")
            return connection
        else:
            print("No available connection in the pool")
            return None

    def release_connection(self, connection: HTTPConnection):
        if connection:
            print(f"Releasing connection {connection}")
            self.pool.put(connection)

    def close_all_connection(self):
        while not self.pool.empty():
            connection = self.pool.get()
            connection.close()


def fetch_data(url: str, pool: HTTPConnectionPool):
    time.sleep(random.uniform(5, 8))
    connection: HTTPConnection = pool.get_connection()
    if connection:
        response = connection.send_request("GET", url)
        if response:
            print(f"Connection {connection} get Response from {url}: {response.json()}")
        pool.release_connection(connection)


def main() -> None:
    pool = HTTPConnectionPool(max_connections=1)

    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
    ]
    threads = []
    for url in urls:
        t1 = threading.Thread(target=fetch_data, args=(url, pool))
        threads.append(t1)
        t1.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
