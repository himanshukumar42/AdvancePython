import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self._token = None

    def get_tokn(self):
        if self._token is None:
            self._token = "fake_token_123"
        return self._token

    def get_data(self, endpoint):
        token = self.get_tokn()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.base_url}/endpoint", headers=headers)
        return response.json()


def main() -> None:
    client = APIClient("https://api.example.com")
    data = client.get_data("users/1")
    print(data)


if __name__ == '__main__':
    main()
