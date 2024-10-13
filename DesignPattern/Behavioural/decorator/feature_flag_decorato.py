def feature_flag(flag: bool):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if flag:
                    return func(*args, **kwargs)
            except Exception as e:
                print(f"Exception Occurred {str(e)}")
        return wrapper
    return decorator


@feature_flag(True)
def new_feature():
    print("New feature is running")


def main() -> None:
    new_feature()


if __name__ == '__main__':
    main()
