
class Person:
    def __init__(self, name, age, city) -> None:
        self.name = name
        self.age = age
        self.city =  city

    def __str__(self) -> str:
        return self.name 
    
    def __repr__(self) -> str:
        return "Person(name={}, age={}, city={})".format(self.name, self.age, self.city)
    
    def __eq__(self, other: object) -> bool:
        return (self.name, self.age, self.city) == (other.name, other.age, other.city)


if __name__ == '__main__':
    # p = Person("Nikhil", 20, "Jaipur")
    # print(p.name, p.age, p.city)
    # print(p)

    p1 = Person("Nikhil", 20, "Jaipur")
    p2 = Person("Nikhil", 20, "Jaipur")
    p3 = Person("Nikhil", 20, "Delhi")
    print(p1)
    print(p1 == p2)
    print(p1 == p3)
    print(p1 is p2)
