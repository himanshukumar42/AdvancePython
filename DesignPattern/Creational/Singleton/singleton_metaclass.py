import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls].initialize_instance(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.host = None
        self.port = None
        self.user = None

    def initialize_instance(self, host: str = None, port: int = 0, user: str = None):
        self.host = host
        self.port = port
        self.user = user

    def get_instance(self):
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}({self.host}, {self.port}, {self.user})"


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.log_file = None

    def initialize_instance(self):
        pass


class Redis(metaclass=SingletonMeta):
    pass


class Config(metaclass=SingletonMeta):
    pass


def main() -> None:
    db1 = Database()
    db2 = Database()

    db1.initialize_instance("localhost", 3306, "root")
    db2.initialize_instance("localhost", 5432, "postgres")
    print(db1)
    print(db2)

    logger1 = Logger()
    logger2 = Logger()
    print(logger1 is logger2)


if __name__ == '__main__':
    main()
