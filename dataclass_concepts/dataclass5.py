from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    city: str = field(init=False, default="Jaipur")
    dob: str = field(metadata={"Format": "YYYY-MM-DD"})


@dataclass
class Student(Person):
    grade: int
    subjects: list


@dataclass
class A:
    X: int = 10
    Y: int = 20

@dataclass
class B(A):
    Z: int = 30
    X: int = 40


if __name__ == '__main__':
    s1 = Student(name="Himanshu", dob="1998-07-25", grade=9, subjects=["Math", "Science"])
    print(s1)
    b = B()
    print(b)
