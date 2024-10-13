class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__username}, {self.__email})"

    def delete(self):
        self.__username = None
        self.__email = None
        self.__password = None


def admin_required(func):
    def wrapper(user_role: str, user: User, *args, **kwargs):
        if user_role != "admin":
            raise PermissionError("Admin Access Required")
        result = func(user_role, user, *args, **kwargs)
        return result
    return wrapper


@admin_required
def delete_user(user_role: str, user: User):
    user.delete()
    return True


def main() -> None:
    new_user = User("itz_alice", "alice@example.coM", "alice123")
    print(new_user)
    delete_user(user_role="admin", user=new_user)
    print(new_user)


if __name__ == '__main__':
    main()
