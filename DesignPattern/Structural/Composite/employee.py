from abc import ABC, abstractmethod


class EmployeeComponent(ABC):
    @abstractmethod
    def show_details(self, indent: int = 0):
        pass


class Employee(EmployeeComponent):
    def __init__(self, name, position):
        self._name = name
        self._position = position

    def show_details(self, indent: int = 0):
        print(f"{' '* indent}{self._name}: {self._position}")


class Manager(EmployeeComponent):
    def __init__(self, name, position):
        self._name = name
        self._position = position
        self._subordinates = []

    def add(self, employee: EmployeeComponent):
        self._subordinates.append(employee)

    def remove(self, employee: EmployeeComponent):
        self._subordinates.remove(employee)

    def show_details(self, indent: int = 0):
        print(f"{' ' * indent}{self._name}: {self._position}")
        for subordinate in self._subordinates:
            subordinate.show_details(indent+4)


def main() -> None:
    ceo = Manager("Ajay Dubedi", "CEO")
    cto = Manager("Akshay Dhiman", "CTO")
    director = Manager("Suraj Tripathi", "Director")
    head_hr = Manager("Divya Dang", 'HEAD HR')
    manager1 = Manager("Abhishek Sing", "ReportingManager")
    manager2 = Manager("Kishor Yadav", "ReportingManager")
    employee1 = Employee("Ayush Jain", "ReactNative Developer")
    employee2 = Employee("Poonam Nishad", "MERN Developer")
    employee3 = Employee("Arun Saharan", "Full Stack Developer")
    employee4 = Employee("Himanshu Kumar", "Full Stack Developer")

    ceo.add(cto)
    ceo.add(head_hr)
    cto.add(director)
    director.add(manager1)
    director.add(manager2)

    manager2.add(employee1)
    manager2.add(employee2)

    manager1.add(employee3)
    manager1.add(employee4)

    ceo.show_details()


if __name__ == '__main__':
    main()
