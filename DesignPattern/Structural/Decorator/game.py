from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass


class BasicCharacter(Character):
    def __init__(self, name: str):
        self._name = name
        self._health = 100
        self.inventory = []

    def get_description(self):
        return f"Basic Character with name {self._name}"

    def get_damage(self):
        return 10


class CharacterDecorator(Character, ABC):
    def __init__(self, character: Character):
        self._character = character

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass


class DoubleDamageCharacter(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Double Damage Power"

    def get_damage(self):
        return self._character.get_damage()*2


class FireballDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Fireball Power"

    def get_damage(self):
        return self._character.get_damage() +  20


class InvisibilityDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Invisibility Power."

    def get_damage(self):
        return self._character.get_damage()


def main() -> None:
    character = BasicCharacter("LuciferOP")
    print(character.get_description())
    print(character.get_damage())

    double_damage_decorator = DoubleDamageCharacter(character)
    fireball_decorator = FireballDecorator(character)
    invisible_decorator = InvisibilityDecorator(character)

    print(double_damage_decorator.get_description())
    print(double_damage_decorator.get_damage())

    print(fireball_decorator.get_description())
    print(fireball_decorator.get_damage())

    print(invisible_decorator.get_description())
    print(invisible_decorator.get_damage())

    # combine Decorators

    fireball_invisible_character = InvisibilityDecorator(fireball_decorator)
    print(fireball_invisible_character.get_description())
    print(fireball_invisible_character.get_damage())


if __name__ == '__main__':
    main()
