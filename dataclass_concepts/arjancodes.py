from dataclasses import dataclass, field, asdict
from uuid import uuid4


# class Person:
#     def __init__(self, name: str, address: str) -> None:
#         self.name = name
#         self.address = address
#
#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}(name={self.name}, address={self.address})"

@dataclass
class Person:
    id: str = field(init=False, default_factory=uuid4)
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list)
    __search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__search_string = f"{self.name} {self.address}"


def main() -> None:
    person = Person(name="Himanshu", address="Jaipur Rajasthan")
    print(person)
    print(asdict(person))


if __name__ == '__main__':
    main()
