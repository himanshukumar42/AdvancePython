class House:
    def __init__(self, builder):
        self.stories = builder.stories
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type

    def __repr__(self):
        return f"{self.__class__.__name__}({self.stories}, {self.door_type}, {self.roof_type})"


class HouseBuilder:
    def __init__(self):
        self.stories = None
        self.door_type = None
        self.roof_type = None

    def set_stories(self, stories):
        self.stories = stories

    def set_door_type(self, door_type):
        self.door_type = door_type

    def set_roof_type(self, roof_type):
        self.roof_type = roof_type

    def build(self):
        return House(self)


class Director:
    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def build_one_story_house(self):
        self.builder.set_stories(1)
        self.builder.set_door_type("Single")
        self.builder.set_roof_type("Pointy")
        return self.builder.build()

    def build_two_story_house(self):
        self.builder.set_stories(2)
        self.builder.set_door_type("Double")
        self.builder.set_roof_type("Flat")
        return self.builder.build()


def main() -> None:
    house_builder = HouseBuilder()
    director = Director(house_builder)

    one_story_house = director.build_one_story_house()
    two_story_house = director.build_two_story_house()

    print(one_story_house)
    print(two_story_house)


if __name__ == '__main__':
    main()
