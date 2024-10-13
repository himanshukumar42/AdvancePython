class GameState:
    def __init__(self, level, health, inventory):
        self.__level = level
        self.__health = health
        self.__inventory = inventory

    def get_state(self):
        return self.__level, self.__health, self.__inventory


class Game:
    def __init__(self):
        self.level = 1
        self.health = 100
        self.inventory = []

    def save(self):
        return GameState(self.level, self.health, self.inventory.copy())

    def load(self, game_state):
        self.level, self.health, self.inventory = game_state.get_state()

    def play(self, level, health, item):
        self.level = level
        self.health = health
        self.inventory.append(item)

    def __str__(self):
        return f"Level: {self.level}, Health: {self.health}, Inventory: {self.inventory}"


class GameSaveManager:
    def __init__(self):
        self.saves = []

    def save_game(self, game_state):
        self.saves.append(game_state)

    def load_game(self, index):
        return self.saves[index]


def main() -> None:
    game = Game()
    save_manager = GameSaveManager()

    game.play(2, 80, "Sword")
    save_manager.save_game(game.save())
    game.play(3, 50, "Shield")
    save_manager.save_game(game.save())
    print(game)

    game.load(save_manager.load_game(0))
    print(game)


if __name__ == '__main__':
    main()
