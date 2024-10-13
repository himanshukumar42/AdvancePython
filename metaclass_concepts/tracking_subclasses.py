class TrackSubclasses(type):
    subclasses = []

    def __new__(cls, name, bases, dct):
        instance = super().__new__(cls, name, bases, dct)
        cls.subclasses.append(instance)
        return instance


class Service(metaclass=TrackSubclasses):
    pass


class EmailService(Service):
    pass


class PaymentService(Service):
    pass


def main() -> None:
    print(TrackSubclasses.subclasses)
    print(len(TrackSubclasses.subclasses))


if __name__ == '__main__':
    main()
