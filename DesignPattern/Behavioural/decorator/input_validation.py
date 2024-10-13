
def validate(func):
    def wrapper(*args):
        if any(a <= 0 for a in args):
            raise ValueError("Values must be greater than 0")
        result = func(*args)
        return result
    return wrapper


@validate
def multiply(*args):
    mul = 1
    for a in args:
        mul *= a
    return mul


def main() -> None:
    print(multiply(1, 2, 3, 7, 5, 10))


if __name__ == '__main__':
    main()
