import queue
import threading
import requests


class SingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class APIClient:
    def __init__(self, bearer_token):
        self.base_url = "https://api.twitter.com/2"
        self._session = requests.Session()
        self._bearer_token = bearer_token

    def fetch_user_tweets(self, username):
        url = f"{self.base_url}/tweets"
        headers = {
            "Authorization": f"Bearer {self._bearer_token}"
        }
        params = {
            "query": f"from:{username}",
            "tweet.fields": "created_at"
        }
        response = self._session.get(url, headers=headers, params=params)
        if response.status_code == 200:
            tweets = response.json()
            print(f"fetched tweets for {username}: {tweets}")
        else:
            print(f"failed to fetch tweet for {username}: {response.text}")

    def close(self):
        self._session.close()

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class APIClientPool(metaclass=SingletonMeta):
    def __init__(self, bearer_token, max_clients):
        self._pool = queue.Queue(max_clients)
        self._lock = threading.Lock()
        for _ in range(max_clients):
            self._pool.put(APIClient(bearer_token))

    def get_client(self):
        with self._lock:
            if not self._pool.empty():
                return self._pool.get()
            else:
                return None

    def release_client(self, client):
        with self._lock:
            if client:
                self._pool.put(client)

    def close_all_client(self):
        with self._lock:
            while not self._pool.empty():
                client = self._pool.get()
                client.close()

    def __repr__(self):
        return f"{self.__class__.__name__}()"


def process_twitter_requests(pool: APIClientPool, bearer_token: str):
    client: APIClient = pool.get_client()
    if client:
        client.fetch_user_tweets("himanshuk42")
        pool.release_client(client)
    else:
        print("No client found in the pool")


def main() -> None:
    bearer_token = "YOUR_TWITTER_BEARER_TOKEN"
    pool = APIClientPool(bearer_token=bearer_token, max_clients=5)

    threads = []
    for i in range(5):
        t = threading.Thread(target=process_twitter_requests, args=(pool, bearer_token, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    pool.close_all_client()


if __name__ == '__main__':
    main()
