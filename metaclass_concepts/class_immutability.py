class ImmutableMeta(type):
    def __setattr__(cls, key, value):
        raise AttributeError(f"Cannot modify class {cls.__name__}")


class Config(metaclass=ImmutableMeta):
    API_URL = "https://api.example.com/"


def main() -> None:
    Config.API_URL = "https://newapi.example.com/"


if __name__ == '__main__':
    main()
