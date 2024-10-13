from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Person:
    name: str = field(k)
    city: str =field(init=False, default="Jaipur")
    dob: str
    age: int = field(init=False)

    def __post_init__(self):
        dob_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()

        self.age = today.year - dob_date.year
        if (today.month, today.day) < (dob_date.month, dob_date.day):
            self.age -= 1


if __name__ == '__main__':
    p1 = Person(name="Himanshu", dob="1998-07-25")
    p2 = Person(name="Arun", dob="1997-10-10")
    print(p1)
