from dataclasses import dataclass


# order = True implements __lt__, __gt__, __le__, __ge__
# frozen = True implements instance variables as immutable
@dataclass(order=True, unsafe_hash=True)
class Person:
    name: str
    age: int
    city: str


if __name__ == '__main__':
    p1 = Person("Nikhil", 20, "Jaipur")
    p2 = Person("Nikhil", 21, "Jaipur")
    print(p1)
    print(p1 == p2)
    # print(p1 is p2)

    print(p1 < p2)
    print(p1 > p2)

    print(hash(p1))
