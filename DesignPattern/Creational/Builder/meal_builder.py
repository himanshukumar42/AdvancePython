class Order:
    def __init__(self, main_course=None, side_course=None, drink=None, dessert=None, extras=None):
        self.main_course = main_course
        self.side_course = side_course
        self.drink = drink
        self.dessert = dessert
        self.extras = extras

    def __repr__(self):
        return f"{self.__class__.__name__}({self.main_course}, {self.side_course}, {self.drink}, {self.dessert}, {self.extras})"


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_main_course(self, main_course):
        self.order.main_course = main_course
        return self

    def add_side_course(self, side_course):
        self.order.side_course = side_course
        return self

    def add_drink(self, drink):
        self.order.drink = drink
        return self

    def add_desert(self, desert):
        self.order.dessert = desert
        return self

    def add_extras(self, *args):
        self.order.extras = args
        return self

    def build(self):
        return self.order


def main() -> None:
    order: Order = OrderBuilder().add_main_course({
        "Butter Chicken": 1,
        "Butter Naan": 2,
        "Garlic Naan": 2,
        "Plain Chapati": 2
    }).add_side_course({
        "Chicken Burger": 2,
        "Chicken Wings": 2,
        "Paneer tikka": 2
    }).add_drink({
        "Sprite": 2,
        "Coke": 1
    }).add_desert({
        "Choco Pie": 1,
        "Gulab Jaamun": 2
    }).add_extras("Papad", "Aachar", "Mayonese", "Chilli Flakes").build()

    print(order)
    print(order.main_course)


if __name__ == '__main__':
    main()
