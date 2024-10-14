from copy import deepcopy


class GameCharacter:
    def __init__(self, name, health, attack, abilities, inventory):
        self.name = name
        self.health = health
        self.attack = attack
        self.abilities = abilities
        self.inventory = inventory

    def clone(self):
        return deepcopy(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.health}, {self.attack}, {self.abilities}, {self.inventory})"


def main() -> None:
    base_character = GameCharacter("Gues1234", 100, 10, ["Run", "Jump"], ["Sword", "Gun", "Bag"])

    warrior = base_character.clone()
    warrior.name = "Lucifer"
    warrior.attack = 15
    warrior.abilities.append("Shield Block")

    print(warrior)


if __name__ == '__main__':
    main()
