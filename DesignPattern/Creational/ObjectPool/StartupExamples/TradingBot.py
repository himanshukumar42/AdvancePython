import threading
from copy import deepcopy
import queue
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
    def __init__(self, api_key: str = None):
        self._session = requests.Session()
        self._base_url = "https://www.alphavantage.co/query"
        self._api_key = api_key

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    def fetch_stock_price(self, symbol):
        url = self._base_url
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "1min",
            "apikey": self._api_key
        }
        response = self._session.get(url=url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Stock Data for {symbol}: {data}")
        else:
            print(f"failed to fetch stock data for {symbol}: {response.text}")

    def place_trade(self, symbol, action):
        print(f"Placing {action} order for{symbol} on url: {self._base_url}")

    def close(self):
        self._session.close()

    def clone(self):
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class APIClientPool(metaclass=SingletonMeta):
    def __init__(self, api_key, max_size=5):
        self._pool = queue.Queue(max_size)
        self._lock = threading.Lock()
        api_client_object = APIClient(api_key=api_key)
        for _ in range(max_size):
            self._pool.put(api_client_object.clone())

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


def bot_trading(pool: APIClientPool, symbol: str, action: str):
    client: APIClient = pool.get_client()
    if client:
        client.fetch_stock_price(symbol)
        client.place_trade(symbol, action)
        pool.release_client(client)


def main():
    API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
    pool = APIClientPool(api_key=API_KEY)

    bots = [
        {"symbol": "AAPL", "action": "buy"},
        {"symbol": "GOOGL", "action": "sell"},
        {"symbol": "TSLA", "action": "buy"},
    ]

    threads = []
    for bot in bots:
        t = threading.Thread(target=bot_trading, args=(pool, bot.get("symbol"), bot.get("action")))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
