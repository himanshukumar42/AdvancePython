class AbstractMethodMeta(type):
    def __new__(cls, name, bases, dct):
        if 'connect' not in dct or 'disconnect' not in dct:
            raise TypeError(f"Class {name} must implement connect and disconnect method")
        return super().__new__(cls, name, bases, dct)


class DatabaseAdapter(metaclass=AbstractMethodMeta):
    def connect(self):
        pass

    def disconnect(self):
        pass


class MySQLAdapter(DatabaseAdapter):
    def connect(self):
        pass

    def disconnect(self):
        pass


def main() -> None:
    mysql_adapter = MySQLAdapter()


if __name__ == '__main__':
    main()
