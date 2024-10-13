import time


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memoize
def fibonacci(n: int):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    start = time.time()
    print(fibonacci(10))
    end = time.time()
    print(f"Execution time of {fibonacci.__name__} is: {end - start}")


if __name__ == '__main__':
    main()
