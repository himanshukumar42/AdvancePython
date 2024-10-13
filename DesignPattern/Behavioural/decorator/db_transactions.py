def transactional(func):
    def wrapper(*args, **kwargs):
        print("Starting Transaction...")
        try:
            result = func(*args, **kwargs)
            print("Committing transaction...")
            return result
        except Exception as e:
            print(f"Exception Occurred: {str(e)}")
            print("Rollback to previous state")
    return wrapper


class User:
    def __init__(self, username, email, password, permissions=[]):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__permissions = permissions

    @transactional
    def update(self, email=None, password=None):
        self.__email = email
        self.__password = password
        raise RuntimeError("somthing went wrong")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__username}, {self.__email})"


def main() -> None:
    alice = User("alice_x", "alice@example.com", "alice@123")
    print(alice)
    alice.update(email="new_alice@example.com")
    print(alice)


if __name__ == '__main__':
    main()
