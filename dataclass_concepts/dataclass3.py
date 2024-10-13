from dataclasses import dataclass, field
from datetime import datetime


def calculate_age(dob: str) -> str:
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - dob_date.year
    if (today.month, today.day) < (dob_date.month, dob_date.day):
        age -= 1
    return age


def get_default_age():
    ages = [12, 34, 56, 34, 12]
    return sum(ages) // len(ages)


@dataclass(unsafe_hash=True)
class Person:
    name: str = field(compare=False)
    dob: str = field(metadata={"format": "YYYY-MM-DD"})
    city: str = field(init=False, default="Jaipur", repr=False, hash=False, compare=False)
    age: int = field(default_factory=get_default_age)


if __name__ == '__main__':
    # p = Person("Himanshu", 26, "Jaipur")
    # p = Person("Arun", "Jaipur")
    # print(p.__dataclass_fields__['age'])
    p = Person(name="Himanshu", dob="1998-07-25")
    print(p)
    print(hash(p))
    p2 = Person(name="Arun", dob="1993-10-10")
    print(p.__dataclass_fields__['dob'].metadata['format'])
