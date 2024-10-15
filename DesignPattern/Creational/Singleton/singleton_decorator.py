# Implement Singleton using Decoraor
import threading


def singleton(class_):
    instances = {}
    _lock = threading.Lock()

    def wrapper(*args, **kwargs):
        with _lock:
            if class_ not in instances:
                instances[class_] = class_(*args, **kwargs)
            return instances[class_]

    return wrapper


@singleton
class Database:
    pass


@singleton
class Redis:
    pass


@singleton
class Config:
    pass


@singleton
class Logger:
    pass


def main() -> None:
    db1 = Database()
    db2 = Database()
    print(db1 is db2)


if __name__ == '__main__':
    main()
