class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for key, val in attrs.items():
            if key.startswith("__"):
                a[key] = val
            else:
                a[key.upper()] = val
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hi")


def main() -> None:
    d = Dog()
    print(dir(d))
    print(d.X)


if __name__ == '__main__':
    main()
