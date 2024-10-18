class Car:
    def __init__(self, engine=None, color=None, wheels=None, interior=None):
        self.engine = engine
        self.color = color
        self.wheels = wheels
        self.interior = interior

    def __str__(self):
        return (f"Car Details:\n Engine: {self.engine}\n Color: "
                f"{self.color}\n Wheels: {self.wheels}\n Interior: {self.interior}")


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_interior(self, interior):
        self.car.interior = interior
        return self

    def build(self):
        return self.car


def main() -> None:
    car = CarBuilder().set_engine("V8 Turbo").set_color("Metallic Blue").set_wheels(4).set_interior("Leather").build()

    print(car)


if __name__ == '__main__':
    main()
