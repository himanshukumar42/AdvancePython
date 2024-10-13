def require_permission(permission, perm_object):
    def decorator(func):
        def wrapper(user: User, report_id: int, *args, **kwargs):
            if permission in user.permissions:
                result = func(user, report_id, *args, **kwargs)
                return result
            else:
                raise PermissionError(f"{user} do not have permission to {permission} {perm_object}")

        return wrapper

    return decorator


class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__permissions = []

    @property
    def permissions(self):
        return self.__permissions

    def __str__(self):
        return self.__username

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__username}, {self.__email}, {self.__permissions})"


@require_permission('view', 'reports')
def view_reports(user: User, report_id: int):
    print(f"{user} is Viewing Report and Analytics with id {report_id}")


@require_permission('delete', 'reports')
def delete_reports(user: User, report_id: int):
    print(f"{user} is Deleting Report and Analytics with id {report_id}")


def main() -> None:
    alice = User("alice_x", "alice@example.com", "alice123")
    alice.permissions.append('view')

    bob = User("itz_bob", "bob@example.com", "bob982")
    bob.permissions.append('delete')

    view_reports(alice, 101)
    delete_reports(bob, 101)


if __name__ == '__main__':
    main()
