class ModelMeta(type):
    def __new__(cls, name, bases, dct):
        if 'fields' in dct:
            for field in dct['fields']:
                dct[field] = None
        return super().__new__(cls, name, bases, dct)


class DynamicModel(metaclass=ModelMeta):
    fields = ['name', 'age', ]


def main() -> None:
    model = DynamicModel()
    print(model.name)
    print(model.age)


if __name__ == '__main__':
    main()
