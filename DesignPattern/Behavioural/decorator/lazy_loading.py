def lazy_load(lazy: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@lazy_load(True)
def load_file_data(file_path):
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
