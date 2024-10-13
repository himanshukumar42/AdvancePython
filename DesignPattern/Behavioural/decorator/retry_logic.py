import requests


def retry_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Exception Occurred: {str(e)}")
                    print("Retrying.....")
        return wrapper
    return decorator


def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Exception Occurred: {str(e)}")
                print("Retrying.....")

    return wrapper


@retry_times(2)
def fetch_data(url: str):
    response = requests.get(url)
    return response.status_code


def main() -> None:
    API_URL = "https://googleafds.com"
    print(fetch_data(API_URL))


if __name__ == '__main__':
    main()
