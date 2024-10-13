import warnings


def deprecated(func):
    def wrapper(*args, **kwargs):
        warnings.warn(f"{func.__name__} is deprecated")
        return func(*args, **kwargs)
    return wrapper


@deprecated
def old_function():
    print("This is an old function")


def main() -> None:
    old_function()


if __name__ == '__main__':
    main()
