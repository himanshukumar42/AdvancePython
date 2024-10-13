
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Called {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Executed {func.__name__}")
        return result
    return wrapper


@log
def convert_to_uppercase(text: str) -> str:
    return text.upper()


def main() -> None:
    print(convert_to_uppercase("Hello My name is Himanshu Kumar"))


if __name__ == '__main__':
    main()
