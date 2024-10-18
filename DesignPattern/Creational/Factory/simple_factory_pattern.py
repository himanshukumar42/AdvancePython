from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self, name):
        pass


class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")


class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")


class PersonFactory(object):
    @classmethod
    def createPerson(cls, designation, name):
        eval(designation)().create(name)


if __name__ == '__main__':
    instance_designation = "Engineer"
    instance_name = 'alice'
    PersonFactory.createPerson(instance_designation, instance_name)
