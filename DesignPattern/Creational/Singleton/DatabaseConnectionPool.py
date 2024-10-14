class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._connection = cls.connect_to_db()
        return cls._instance

    @staticmethod
    def connect_to_db():
        return "database connection established"


def main() -> None:
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(db1 is db2)


if __name__ == '__main__':
    main()
    
