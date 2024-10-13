import time


def rate_limit(calls, period):
    def decorator(func):
        last_called = [0]

        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] >= period:
                last_called[0] = now
                return func(*args, **kwargs)
            else:
                print("Rate limit exceeded! Please try again")

        return wrapper

    return decorator


@rate_limit(1, 5)
def send_message():
    print("Message sent....")


def main() -> None:
    send_message()
    send_message()


if __name__ == '__main__':
    main()
