class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Database connection created")


def main() -> None:
    db1 = Database()
    db2 = Database()
    print(id(db1))
    print(id(db2))
    print(db1 == db2)
    print(db1 is db2)


if __name__ == '__main__':
    main()
