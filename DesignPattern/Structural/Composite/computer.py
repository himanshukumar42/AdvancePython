from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def show_price(self, indent: int = 0):
        pass


class Composite(Component):
    def __init__(self, name):
        self._name = name
        self._components = []

    def add_component(self, component: Component):
        self._components.append(component)

    def show_price(self, indent: int = 0):
        print(f"{' '* indent}{self._name}: ")
        for component in self._components:
            component.show_price(indent=indent+4)


class Leaf(Component):
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    def show_price(self, indent: int = 0):
        print(f"{' ' * indent}Price of {self._name} is: {self._price}")


def main() -> None:
    hard_drive = Leaf("Hard Drive", 8000)
    mouse = Leaf("Mouse", 1200)
    monitor = Leaf("Monitor", 25000)
    ram = Leaf("RAM", 3000)
    cpu = Leaf("CPU", 12000)

    peripheral = Composite("Peripheral")
    peripheral.add_component(mouse)
    peripheral.add_component(monitor)

    mother_board = Composite("MotherBoard")
    mother_board.add_component(cpu)
    mother_board.add_component(ram)

    cabinet = Composite("Cabinet")
    cabinet.add_component(hard_drive)
    cabinet.add_component(mother_board)

    computer = Composite("Computer")
    computer.add_component(cabinet)
    computer.add_component(peripheral)

    computer.show_price()


if __name__ == '__main__':
    main()
