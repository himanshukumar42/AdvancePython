from abc import ABC, abstractmethod


class DatabaseConnection:
    @staticmethod
    def create_connection(db_type):
        if db_type == "MySQL":
            return MySQL()
        elif db_type == "PostgreSQL":
            return PostgreSQL()
        else:
            raise ValueError("unknown database type")


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQL(Database):
    def connect(self):
        print("Connected to MySQL Database")


class PostgreSQL(Database):
    def connect(self):
        print("Connect to PostgreSQL Database")


def main() -> None:
    my_sql = DatabaseConnection.create_connection("PostgreSQL")
    my_sql.connect()


if __name__ == '__main__':
    main()
