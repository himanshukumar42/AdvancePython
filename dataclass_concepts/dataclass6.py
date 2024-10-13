from dataclasses import dataclass, asdict, astuple


@dataclass
class Address:
    lat: float
    long: float
    city: str
    country: str


@dataclass
class Person:
    name: str
    address: Address
    age: int


if __name__ == '__main__':
    a = Address(28.75, 77.11, 'Jaipur', 'India')
    p = Person(name="Himanshu", address=a, age=26)
    print(p)
    print(p.address.city)
    print(asdict(p))
    print(astuple(p))
