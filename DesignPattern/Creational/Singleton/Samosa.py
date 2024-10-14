# Never create a init and override __new__ dunder method

class Samosa:
    _samosa = None

    def __new__(cls, *args, **kwargs):
        if cls._samosa is None:
            cls._samosa = super(Samosa, cls).__new__(cls, *args, **kwargs)
        return cls._samosa

    def __repr__(self):
        return f"{self.__class__.__name__}()"


def main() -> None:
    samosa = Samosa()
    samosa1 = Samosa()
    print(samosa == samosa1)
    print(samosa is samosa1)
    print(hash(samosa))
    print(hash(samosa1))


if __name__ == '__main__':
    main()
