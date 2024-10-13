from dataclasses import dataclass


def hello(name, age):
    @dataclass
    class Person:
        name: str
        age: int

    return Person(name=name, age=age)


class Test:
    pass


TestT = type('Test', (), {})
Point = type('Point', (), {"X": 2, "Y": 3})


def main() -> None:
    # p1 = hello("Himanshu", 25)
    # print(p1)
    print(Test)
    print(Test())
    print(type(Test))
    print(type(Test()))
    print(type(hello))
    p1 = Point()
    print(p1.X)


if __name__ == '__main__':
    main()
