import time

import requests


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__} is {end - start}")
        return result
    return wrapper


@log_time
def fetch_data(url: str) -> int:
    response = requests.get(url=url, timeout=10)
    return response.status_code


def main() -> None:
    API_URL = "https://google.com"
    print("Status Code: ", fetch_data(API_URL))


if __name__ == '__main__':
    main()
