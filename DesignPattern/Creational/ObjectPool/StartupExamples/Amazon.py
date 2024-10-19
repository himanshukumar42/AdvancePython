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
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stripe.com/v1"

    def make_payment(self, amount, currency, source):
        url = f"{self.base_url}/charges"
        headers = {
            "Authorization": F"Bearer {self.api_key}"
        }
        data = {
            "amount": amount,
            "currency": currency,
            "source": source
        }
        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"Payment of {amount} {currency} successful.")
        else:
            print(f"Payment failed: {response.text}")

    def refund_payment(self, charge_id):
        url = f"{self.base_url}/refund"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "charge": charge_id
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"Refund for charge {charge_id} successful.")
        else:
            print(f"Refund failed: {response.text}")


class APIClientPool(metaclass=SingletonMeta):
    def __init__(self, api_key, max_clients):
        self.api_key = api_key
        self.lock = threading.Lock()
        self._pool = queue.Queue(max_clients)
        for _ in range(max_clients):
            self._pool.put(APIClient(api_key))

    def get_client(self):
        with self.lock:
            if not self._pool.empty():
                return self._pool.get()
            else:
                print("No client found in client pool")
                return None

    def release_client(self, client):
        with self.lock:
            if client:
                self._pool.put(client)


def process_payments(pool: APIClientPool, amount: int, currency: str, source: str):
    client: APIClient = pool.get_client()
    if client:
        client.make_payment(amount=amount, currency=currency, source=source)
        pool.release_client(client)
    else:
        print("Not enough client in client pool")


def main() -> None:
    api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    pool = APIClientPool(api_key=api_key, max_clients=5)

    threads = []
    for i in range(5):
        t = threading.Thread(target=process_payments, args=(pool, 1000+i*100, "USD", "tok_visa"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
