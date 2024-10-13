def add_underscore(func):
    def wrapper(text: str):
        result = func(text)
        result = result.replace(" ", "_")
        return result

    return wrapper


def add_hyphen(func):
    def wrapper(text: str):
        result = func(text)
        result = result.replace("_", "-")
        return result

    return wrapper


@add_hyphen
@add_underscore
def convert_to_uppercase(text: str):
    return text.upper()


def main() -> None:
    text = "my name is himanshu"
    print(convert_to_uppercase(text))


if __name__ == '__main__':
    main()
