import queue
import threading

import requests


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class APIClient:
    def __init__(self, client_id):
        self._client_id = client_id
        self._session = requests.Session()

    def get(self, url, **kwargs):
        print(f"API Client {self._client_id} sending GET request to {url}")
        try:
            response = self._session.get(url)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"API Client {self._client_id} failed: {e}")
            return None

    def close(self):
        self._session.close()
        print(f'API Client {self._client_id} closed')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._client_id})"


class APIClientPool(metaclass=SingletonMeta):
    def __init__(self, max_size):
        self._pool = queue.Queue(max_size)
        self._lock = threading.Lock()
        for i in range(max_size):
            self._pool.put(APIClient(i+1))

    def get_client(self):
        with self._lock:
            if not self._pool.empty():
                return self._pool.get()
            else:
                print("No available api client in pool")
                return None

    def release_client(self, client: APIClient):
        with self._lock:
            if client:
                self._pool.put(client)

    def close_all_clients(self):
        while not self._pool.empty():
            client = self._pool.get()
            client.close()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._pool})"


def main() -> None:
    pool: APIClientPool = APIClientPool(max_size=3)

    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5"
    ]

    for url in urls:
        client: APIClient = pool.get_client()
        if client:
            response = client.get(url)
            if response:
                print(f"Response from {url}: {response.json()}")
            pool.release_client(client)

    pool.close_all_clients()


if __name__ == '__main__':
    main()
