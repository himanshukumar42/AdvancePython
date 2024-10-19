import threading
import queue
import time
from copy import deepcopy
import websocket


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class WebsocketClient:
    def __init__(self, uri):
        self._uri = uri
        self.ws = None

    def connect(self):
        self.ws = websocket.WebSocket()
        self.ws.connect(self._uri)
        print(f"Connected to websocket server at {self._uri}")

    def send_message(self, message):
        self.ws.send(message)
        print(f"Sent message: {message}")

    def receive_message(self):
        response = self.ws.recv()
        print(f"Received message: {response}")
        return response

    def clone(self):
        return deepcopy(self)

    def close(self):
        self.ws.close()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._uri})"


class WebsocketClientPool:
    def __init__(self, uri, max_connection):
        self._pool = queue.Queue(max_connection)
        self.lock = threading.Lock()
        websocket_object = WebsocketClient(uri=uri)
        for _ in range(max_connection):
            self._pool.put(websocket_object.clone())

    def get_connection(self):
        with self.lock:
            if not self._pool.empty():
                return self._pool.get()
            else:
                return None

    def release_connection(self, connection):
        with self.lock:
            if connection:
                self._pool.put(connection)

    def close_all_connection(self):
        with self.lock:
            while not self._pool.empty():
                connection = self._pool.get()
                connection.close()

    def __repr__(self):
        return f"{self.__class__.__name__}()"


def handle_stock_price_updates(pool: WebsocketClientPool, stock_symbol: str):
    client: WebsocketClient = pool.get_connection()
    if client:
        client.connect()
        client.send_message(f"Subscribe: {stock_symbol}")
        for _ in range(3):
            client.receive_message()
            time.sleep(1)
        pool.release_connection(client)


def main() -> None:
    websocket_uri = "wss://demo.piesocket.com/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV"
    pool = WebsocketClientPool(uri=websocket_uri, max_connection=2)

    stock_symbols = ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT"]

    threads = []
    for symbol in stock_symbols:
        t = threading.Thread(target=handle_stock_price_updates, args=(pool, symbol))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    pool.close_all_connection()


if __name__ == '__main__':
    main()
