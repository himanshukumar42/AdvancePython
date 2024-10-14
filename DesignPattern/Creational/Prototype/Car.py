from copy import deepcopy
from abc import ABC, abstractmethod


class Prototype:
    @abstractmethod
    def clone(self) -> 'Prototype':
        pass


class Car(Prototype):
    def __init__(self, brand: str = None, model: str = None, color: str = None, top_speed: int = None):
        self._brand = brand
        self._model = model
        self._color = color
        self._top_speed = top_speed

    def clone(self) -> 'Car':
        return deepcopy(self)


def main() -> None:
    pass


if __name__ == '__main__':
    main()
