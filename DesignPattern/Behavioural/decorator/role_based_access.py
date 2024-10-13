def require_role(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            try:
                if user_role not in role:
                    raise PermissionError(f"{role} role is required")
                result = func(user_role, *args, **kwargs)
                return result
            except Exception as e:
                print(f"Exception Occurred: {str(e)}")
        return wrapper
    return decorator


@require_role(['Manager', 'Director', 'CTO', 'CEO'])
def approve_leave(user_role):
    print("Leave is Approved")


def main() -> None:
    approve_leave('CFO')


if __name__ == '__main__':
    main()
