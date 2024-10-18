from abc import ABCMeta, abstractmethod


class Module(metaclass=ABCMeta):
    def __repr__(self):
        return f"{self.__class__.__name__}()"


class ConceptModule(Module):
    pass


class DemoModule(Module):
    pass


class ExerciseModule(Module):
    pass


class IntroModule(Module):
    pass


class SummaryModule(Module):
    pass


class Course(metaclass=ABCMeta):
    def __init__(self):
        self.__modules = []

    @abstractmethod
    def create(self):
        pass

    @property
    def modules(self):
        return self.__modules


class HLD(Course):
    def create(self):
        self.modules.append(IntroModule())
        self.modules.append(DemoModule())
        self.modules.append(SummaryModule())


class LLD(Course):
    def create(self):
        self.modules.append(IntroModule())
        self.modules.append(ExerciseModule())
        self.modules.append(SummaryModule())


class CourseFactory:
    @staticmethod
    def getCourse(course):
        if course == "HLD":
            return HLD()
        elif course == "LLD":
            return LLD()
        else:
            return None


def main() -> None:
    hld = CourseFactory.getCourse("HLD")
    lld = CourseFactory.getCourse("LLD")

    hld.create()
    lld.create()

    print("HLD Modules: ", hld.modules)
    print("LLD Modules: ", lld.modules)


if __name__ == '__main__':
    main()
